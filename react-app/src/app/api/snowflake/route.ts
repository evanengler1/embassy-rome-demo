import { NextRequest, NextResponse } from "next/server";
import { executeQuery } from "@/lib/snowflake";
import { cortexComplete, cortexSearch, parseLlmJson, sqlEscape } from "@/lib/cortex";
import type {
  CrmContact,
  ActivityLog,
  SectorIntel,
  SummitAttendee,
  MissionPriority,
  PolicyDocument,
  EnrichmentResult,
  PrioritizationResult,
  AlignmentResult,
  OverviewStats,
  ContactDetail,
  ApiRequest,
} from "@/lib/types";

const BRONZE = "DOS_ROME_DEMO.BRONZE";
const POLICY_SEARCH = "DOS_ROME_DEMO.SILVER.POLICY_DOCS_SEARCH";
const SECTOR_SEARCH = "DOS_ROME_DEMO.SILVER.SECTOR_INTEL_SEARCH";

const ENRICH_SYSTEM_PROMPT =
  "You are a diplomatic intelligence analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You assess private-sector and multilateral stakeholders against U.S. strategic priorities: critical minerals supply chain diversification away from China, WFP/FAO accountability reform, and AI-diplomacy alignment. You are precise, sober, and action-oriented. You output ONLY valid JSON — no prose, no markdown fences.";

const PRIORITIZE_SYSTEM_PROMPT =
  "You are a strategic scheduling analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You match summit attendees against a stated mission priority and rank the highest-value engagements for the Ambassador. You are precise and output ONLY valid JSON — no prose, no markdown fences.";

const ALIGNMENT_SYSTEM_PROMPT =
  "You are a senior policy alignment analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You compare a U.S./administration policy document against an external or partner policy document, quantify alignment, and produce diplomatic guidance the Ambassador can act on. You are candid about genuine tensions rather than papering over them. You output ONLY valid JSON — no prose, no markdown fences.";

async function getContacts(): Promise<CrmContact[]> {
  return executeQuery<CrmContact>(
    `SELECT * FROM ${BRONZE}.CRM_CONTACTS ORDER BY ORG_NAME`
  );
}

async function getAttendees(): Promise<SummitAttendee[]> {
  return executeQuery<SummitAttendee>(
    `SELECT * FROM ${BRONZE}.SUMMIT_ATTENDEES ORDER BY ATTENDEE_NAME`
  );
}

async function getPriorities(): Promise<MissionPriority[]> {
  return executeQuery<MissionPriority>(
    `SELECT * FROM ${BRONZE}.MISSION_PRIORITIES ORDER BY PRIORITY_ID`
  );
}

async function getDocuments(): Promise<PolicyDocument[]> {
  return executeQuery<PolicyDocument>(
    `SELECT DOC_ID, DOC_TITLE, DOC_TYPE, ISSUER, ISSUE_DATE, CLASSIFICATION, SUMMARY FROM ${BRONZE}.POLICY_DOCUMENTS ORDER BY DOC_ID`
  );
}

async function enrichContact(orgName: string): Promise<EnrichmentResult> {
  const escaped = sqlEscape(orgName);
  const [activities, intel, contact] = await Promise.all([
    executeQuery<ActivityLog>(
      `SELECT * FROM ${BRONZE}.CRM_ACTIVITY_LOG WHERE ORG_NAME = '${escaped}' ORDER BY ACTIVITY_DATE DESC LIMIT 5`
    ),
    executeQuery<SectorIntel>(
      `SELECT * FROM ${BRONZE}.SECTOR_INTELLIGENCE WHERE ORG_NAME = '${escaped}' ORDER BY INTEL_DATE DESC LIMIT 3`
    ),
    executeQuery<CrmContact>(
      `SELECT * FROM ${BRONZE}.CRM_CONTACTS WHERE ORG_NAME = '${escaped}' LIMIT 1`
    ),
  ]);

  const sector = contact[0]?.SECTOR || "";
  const policyContext = await cortexSearch(
    POLICY_SEARCH,
    `${orgName} ${sector}`,
    ["doc_title", "full_text"],
    3
  );

  const activityText = activities
    .map((a) => `- ${a.ACTIVITY_DATE}: [${a.ACTIVITY_TYPE}] ${a.SUMMARY}`)
    .join("\n");

  const intelText = intel
    .map((i) => `- ${i.INTEL_DATE}: ${i.HEADLINE} (${i.SOURCE}) — ${i.SUMMARY}`)
    .join("\n");

  const policyText = policyContext
    .map((p) => `- ${p.doc_title}: ${(p.full_text || "").slice(0, 500)}`)
    .join("\n");

  const userPrompt = `Analyze the following stakeholder organization and return a JSON object with keys: sector_rank (string), relationship_signal (one of Warm/Neutral/Cool/Strategic), alignment_score (int 0-100), intelligence_summary (3-4 sentences), recommended_action (string).

Organization: ${orgName}
Sector: ${sector}
Country: ${contact[0]?.COUNTRY || ""}
Description: ${contact[0]?.ORG_DESCRIPTION || ""}
Current Relationship: ${contact[0]?.RELATIONSHIP_STATUS || ""}

Recent Activity:
${activityText || "No recent activity on record."}

Sector Intelligence:
${intelText || "No recent intelligence on record."}

Relevant Policy Context:
${policyText || "No relevant policy context found."}`;

  const response = await cortexComplete(ENRICH_SYSTEM_PROMPT, userPrompt);
  return parseLlmJson<EnrichmentResult>(response);
}

async function prioritize(priorityId: number): Promise<PrioritizationResult> {
  const priorities = await executeQuery<MissionPriority>(
    `SELECT * FROM ${BRONZE}.MISSION_PRIORITIES WHERE PRIORITY_ID = ${priorityId}`
  );

  const priority = priorities[0];
  if (!priority) throw new Error("Priority not found");

  const [attendees, policyContext] = await Promise.all([
    executeQuery<SummitAttendee>(
      `SELECT * FROM ${BRONZE}.SUMMIT_ATTENDEES ORDER BY ATTENDEE_NAME`
    ),
    cortexSearch(POLICY_SEARCH, priority.PRIORITY_NAME, ["doc_title", "full_text"], 3),
  ]);

  const roster = attendees
    .map((a) => `- ${a.ATTENDEE_NAME} | ${a.ORGANIZATION} | ${a.COUNTRY} | ${a.TITLE} | ${a.SECTOR}`)
    .join("\n");

  const policyText = policyContext
    .map((p) => `- ${p.doc_title}: ${(p.full_text || "").slice(0, 500)}`)
    .join("\n");

  const userPrompt = `Given the following mission priority and summit attendee roster, rank the TOP 8 contacts the Ambassador should prioritize. Return a JSON object with keys: ranked (array of 8 objects with rank, name, org, score 0-100, rationale, opening_line) and deprioritized_note (string explaining how remaining attendees are handled).

Mission Priority: ${priority.PRIORITY_NAME}
Description: ${priority.DESCRIPTION}

Summit Roster (${attendees.length} attendees):
${roster}

Relevant Policy Context:
${policyText || "No relevant policy context found."}`;

  const response = await cortexComplete(PRIORITIZE_SYSTEM_PROMPT, userPrompt, 0.1, 1500);
  return parseLlmJson<PrioritizationResult>(response);
}

async function analyzeAlignment(
  internalDocId: number,
  externalDocId: number
): Promise<AlignmentResult> {
  const [internalDocs, externalDocs] = await Promise.all([
    executeQuery<PolicyDocument>(
      `SELECT * FROM ${BRONZE}.POLICY_DOCUMENTS WHERE DOC_ID = ${internalDocId}`
    ),
    executeQuery<PolicyDocument>(
      `SELECT * FROM ${BRONZE}.POLICY_DOCUMENTS WHERE DOC_ID = ${externalDocId}`
    ),
  ]);

  const internal = internalDocs[0];
  const external = externalDocs[0];
  if (!internal || !external) throw new Error("Document not found");

  const userPrompt = `Compare the following two policy documents and return a JSON object with keys: alignment_score (int 0-100), label (descriptive label like "Strong Alignment" or "Moderate Tension"), agreements (array of strings), tensions (array of strings), diplomatic_approach (string paragraph), talking_points (array of exactly 3 strings).

--- INTERNAL DOCUMENT ---
Title: ${internal.DOC_TITLE}
Type: ${internal.DOC_TYPE}
Issuer: ${internal.ISSUER}

${internal.SUMMARY}

--- EXTERNAL DOCUMENT ---
Title: ${external.DOC_TITLE}
Type: ${external.DOC_TYPE}
Issuer: ${external.ISSUER}

${external.SUMMARY}`;

  const response = await cortexComplete(ALIGNMENT_SYSTEM_PROMPT, userPrompt, 0.1, 1500);
  return parseLlmJson<AlignmentResult>(response);
}

async function getOverviewStats(): Promise<OverviewStats> {
  const [counts, byType, relDist, recent] = await Promise.all([
    executeQuery<Record<string, number>>(
      `SELECT
        (SELECT COUNT(*) FROM ${BRONZE}.CRM_CONTACTS) as CONTACT_COUNT,
        (SELECT COUNT(*) FROM ${BRONZE}.CRM_ACTIVITY_LOG) as ACTIVITY_COUNT,
        (SELECT COUNT(*) FROM ${BRONZE}.SECTOR_INTELLIGENCE) as INTEL_COUNT,
        (SELECT COUNT(*) FROM ${BRONZE}.POLICY_DOCUMENTS) as POLICY_COUNT`
    ),
    executeQuery<{ ACTIVITY_TYPE: string; CNT: number }>(
      `SELECT ACTIVITY_TYPE, COUNT(*) as CNT FROM ${BRONZE}.CRM_ACTIVITY_LOG GROUP BY ACTIVITY_TYPE ORDER BY CNT DESC`
    ),
    executeQuery<{ RELATIONSHIP_STATUS: string; CNT: number }>(
      `SELECT RELATIONSHIP_STATUS, COUNT(*) as CNT FROM ${BRONZE}.CRM_CONTACTS GROUP BY RELATIONSHIP_STATUS ORDER BY CNT DESC`
    ),
    executeQuery<ActivityLog>(
      `SELECT * FROM ${BRONZE}.CRM_ACTIVITY_LOG ORDER BY ACTIVITY_DATE DESC LIMIT 10`
    ),
  ]);
  const c = counts[0];
  return {
    contact_count: c.CONTACT_COUNT,
    activity_count: c.ACTIVITY_COUNT,
    intel_count: c.INTEL_COUNT,
    policy_count: c.POLICY_COUNT,
    activity_by_type: byType,
    relationship_dist: relDist,
    recent_activities: recent,
  };
}

async function getContactDetail(orgName: string): Promise<ContactDetail> {
  const escaped = sqlEscape(orgName);
  const [contacts, activities, intel] = await Promise.all([
    executeQuery<CrmContact>(
      `SELECT * FROM ${BRONZE}.CRM_CONTACTS WHERE ORG_NAME = '${escaped}' LIMIT 1`
    ),
    executeQuery<ActivityLog>(
      `SELECT * FROM ${BRONZE}.CRM_ACTIVITY_LOG WHERE ORG_NAME = '${escaped}' ORDER BY ACTIVITY_DATE DESC LIMIT 5`
    ),
    executeQuery<SectorIntel>(
      `SELECT * FROM ${BRONZE}.SECTOR_INTELLIGENCE WHERE ORG_NAME = '${escaped}' ORDER BY INTEL_DATE DESC LIMIT 3`
    ),
  ]);
  return { contact: contacts[0], activities, intel };
}

async function getAllActivities(): Promise<ActivityLog[]> {
  return executeQuery<ActivityLog>(
    `SELECT * FROM ${BRONZE}.CRM_ACTIVITY_LOG ORDER BY ACTIVITY_DATE DESC`
  );
}

async function getAllIntelligence(): Promise<SectorIntel[]> {
  return executeQuery<SectorIntel>(
    `SELECT * FROM ${BRONZE}.SECTOR_INTELLIGENCE ORDER BY INTEL_DATE DESC`
  );
}

export async function POST(request: NextRequest) {
  try {
    const body: ApiRequest = await request.json();

    switch (body.action) {
      case "getContacts":
        return NextResponse.json(await getContacts());
      case "getAttendees":
        return NextResponse.json(await getAttendees());
      case "getPriorities":
        return NextResponse.json(await getPriorities());
      case "getDocuments":
        return NextResponse.json(await getDocuments());
      case "getOverviewStats":
        return NextResponse.json(await getOverviewStats());
      case "getContactDetail":
        if (!body.orgName) return NextResponse.json({ error: "orgName required" }, { status: 400 });
        return NextResponse.json(await getContactDetail(body.orgName));
      case "getActivities":
        return NextResponse.json(await getAllActivities());
      case "getIntelligence":
        return NextResponse.json(await getAllIntelligence());
      case "enrichContact":
        if (!body.orgName) return NextResponse.json({ error: "orgName required" }, { status: 400 });
        return NextResponse.json(await enrichContact(body.orgName));
      case "prioritize":
        if (body.priorityId == null) return NextResponse.json({ error: "priorityId required" }, { status: 400 });
        return NextResponse.json(await prioritize(body.priorityId));
      case "analyzeAlignment":
        if (body.internalDocId == null || body.externalDocId == null)
          return NextResponse.json({ error: "internalDocId and externalDocId required" }, { status: 400 });
        return NextResponse.json(await analyzeAlignment(body.internalDocId, body.externalDocId));
      default:
        return NextResponse.json({ error: "Unknown action" }, { status: 400 });
    }
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal server error";
    console.error("API error:", err);
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
