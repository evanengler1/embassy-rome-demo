export interface CrmContact {
  ORG_NAME: string;
  SECTOR: string;
  COUNTRY: string;
  HQ_CITY: string;
  PRIMARY_CONTACT_NAME: string;
  PRIMARY_CONTACT_TITLE: string;
  LAST_INTERACTION_DATE: string;
  RELATIONSHIP_STATUS: string;
  ORG_DESCRIPTION: string;
}

export interface ActivityLog {
  ACTIVITY_ID: number;
  ORG_NAME: string;
  ACTIVITY_TYPE: string;
  ACTIVITY_DATE: string;
  SUMMARY: string;
  PARTICIPANTS: string;
  CLASSIFICATION: string;
}

export interface SectorIntel {
  INTEL_ID: number;
  ORG_NAME: string;
  INTEL_TYPE: string;
  INTEL_DATE: string;
  HEADLINE: string;
  SUMMARY: string;
  SOURCE: string;
  RELEVANCE_SCORE: number;
}

export interface SummitAttendee {
  ATTENDEE_NAME: string;
  ORGANIZATION: string;
  COUNTRY: string;
  TITLE: string;
  SECTOR: string;
}

export interface MissionPriority {
  PRIORITY_ID: number;
  PRIORITY_NAME: string;
  DESCRIPTION: string;
  WEIGHT: number;
  STATUS: string;
}

export interface PolicyDocument {
  DOC_ID: number;
  DOC_TITLE: string;
  DOC_TYPE: string;
  ISSUER: string;
  ISSUE_DATE: string;
  CLASSIFICATION: string;
  FULL_TEXT: string;
  SUMMARY: string;
}

export interface EnrichmentResult {
  sector_rank: string;
  relationship_signal: string;
  alignment_score: number;
  intelligence_summary: string;
  recommended_action: string;
}

export interface RankedContact {
  rank: number;
  name: string;
  org: string;
  score: number;
  rationale: string;
  opening_line: string;
}

export interface PrioritizationResult {
  ranked: RankedContact[];
  deprioritized_note: string;
}

export interface AlignmentResult {
  alignment_score: number;
  label: string;
  agreements: string[];
  tensions: string[];
  diplomatic_approach: string;
  talking_points: string[];
}

export interface OverviewStats {
  contact_count: number;
  activity_count: number;
  intel_count: number;
  policy_count: number;
  activity_by_type: { ACTIVITY_TYPE: string; CNT: number }[];
  relationship_dist: { RELATIONSHIP_STATUS: string; CNT: number }[];
  recent_activities: ActivityLog[];
}

export interface ContactDetail {
  contact: CrmContact;
  activities: ActivityLog[];
  intel: SectorIntel[];
}

export type ApiAction =
  | "getContacts"
  | "getAttendees"
  | "getPriorities"
  | "getDocuments"
  | "getOverviewStats"
  | "getContactDetail"
  | "getActivities"
  | "getIntelligence"
  | "enrichContact"
  | "prioritize"
  | "analyzeAlignment";

export interface ApiRequest {
  action: ApiAction;
  orgName?: string;
  priorityId?: number;
  internalDocId?: number;
  externalDocId?: number;
}
