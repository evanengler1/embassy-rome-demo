# USUN Rome — Snowflake AI Data Cloud Demo

**Audience:** Department of State technical team evaluating Snowflake's AI Data Cloud for diplomatic operations
**Account:** Snowflake (<YOUR_ACCOUNT>)

---

## What This Demo Shows

This demo presents three AI-powered use cases built entirely on Snowflake, designed for the U.S. Mission to the UN Agencies in Rome (USUN Rome). It demonstrates how Snowflake's AI Data Cloud can transform diplomatic operations — turning raw CRM data, policy documents, and sector intelligence into actionable stakeholder assessments, event prioritization, and policy alignment analysis.

All data is **synthetic** but realistic for the USUN Rome diplomatic context, covering critical minerals supply chain diplomacy, FAO/WFP accountability reform, AI governance alignment, and U.S.-Italy bilateral relations.

### Use Case 1: CRM Enrichment Pipeline

**Problem:** Diplomatic CRM records contain basic contact information but lack the intelligence needed for strategic engagement.

**Solution:** Select any stakeholder organization and Snowflake automatically cross-references internal activity history, external sector intelligence, and relevant policy context to produce an enriched profile. The output includes:
- **Sector Rank** — the organization's position and relevance
- **Relationship Signal** — Warm, Neutral, Cool, or Strategic
- **Alignment Score** — 0-100 score measuring strategic alignment with U.S. priorities
- **Intelligence Summary** — synthesized assessment from multiple data sources
- **Recommended Action** — specific next steps for diplomatic engagement

**Snowflake Features:** Cortex Complete (LLM), Cortex Search (semantic retrieval), structured data queries

### Use Case 2: Event Prioritization Engine

**Problem:** The Ambassador has limited time at a 28-person summit. Who should they meet, and what should they say?

**Solution:** Given the summit attendee list and a selected mission priority scenario (e.g., "Lithium Supply Chain Security" or "FAO/WFP Accountability"), Cortex AI ranks the top 8 contacts the Ambassador should prioritize, with:
- **Priority Score** — weighted relevance to the selected scenario
- **Rationale** — why this person matters for this specific priority
- **Suggested Opening Line** — a tailored conversation starter

**Snowflake Features:** Cortex Complete (LLM), Cortex Search (context retrieval), structured data queries

### Use Case 3: Policy Alignment Analyzer

**Problem:** Before diplomatic engagement, staff need to understand how U.S. policy positions align with partner documents — identifying both common ground and tension points.

**Solution:** Select an internal U.S. policy document and an external partner document. Cortex AI cross-references both texts and produces:
- **Alignment Score** — 0-100% with a descriptive label
- **Points of Agreement** — shared positions that enable cooperation
- **Points of Tension** — areas requiring careful diplomatic framing
- **Recommended Diplomatic Approach** — how to navigate the engagement
- **Ambassador Talking Points** — ready-to-use language

**Snowflake Features:** Cortex Complete (LLM), full-text document analysis

### Cortex Agent (Snowflake Intelligence)

In addition to the dashboard, a conversational Cortex Agent provides natural-language access to the same data and capabilities. Staff can ask questions like:
- "What do we know about Enel Green Power?"
- "Who should the Ambassador prioritize at the summit for critical minerals?"
- "How does our AI executive order align with the Vatican's Rome Call?"
- "Which CRM contacts have a relationship gap we should address?"

The agent routes questions to the appropriate tool — structured data queries via a semantic view, or unstructured search across policy documents and sector intelligence.

---

## Architecture

```
  ┌─────────────────────── GOLD ───────────────────────────┐
  │                                                         │
  │  ┌────────────────────────────────────────────────────┐ │
  │  │        Streamlit Dashboard (SiS)                   │ │
  │  │   CRM Enrichment | Prioritization | Policy Align  │ │
  │  └───────────────────────┬────────────────────────────┘ │
  │                          │                              │
  │  ┌───────────────────────┴────────────────────────────┐ │
  │  │  Cortex Agent (DOS_ROME_AGENT)                    │ │
  │  │  Semantic View (DOS_ROME_SV)                      │ │
  │  └───────────────────────┬────────────────────────────┘ │
  └──────────────────────────┼──────────────────────────────┘
                             │
       ┌─────────────────────┼──────────────────────┐
       │          CORTEX.COMPLETE()                  │
       │         (mistral-large2 LLM)                │
       └─────────────────────┬──────────────────────┘
                             │
  ┌──────────────────────────┼──────────────────────────────┐
  │                       SILVER                            │
  │    ┌─────────────────┐     ┌──────────────────┐         │
  │    │  Cortex Search  │     │  Cortex Search   │         │
  │    │  POLICY_DOCS    │     │  SECTOR_INTEL    │         │
  │    └─────────┬───────┘     └────────┬─────────┘         │
  └──────────────┼──────────────────────┼───────────────────┘
                 │                      │
  ┌──────────────┼──────────────────────┼───────────────────┐
  │                       BRONZE                            │
  │  ┌───────────┴──────┐  ┌────────────┴────────┐          │
  │  │ POLICY_DOCUMENTS │  │ SECTOR_INTELLIGENCE │          │
  │  │ (6 docs)         │  │ (59 records)        │          │
  │  └──────────────────┘  └─────────────────────┘          │
  │  ┌──────────────────┐  ┌─────────────────────┐          │
  │  │ CRM_CONTACTS     │  │ CRM_ACTIVITY_LOG    │          │
  │  │ SUMMIT_ATTENDEES │  │ MISSION_PRIORITIES  │          │
  │  └──────────────────┘  └─────────────────────┘          │
  └─────────────────────────────────────────────────────────┘
```

---

## Snowflake Objects Created

| Object | Type | Schema | Description |
|--------|------|--------|-------------|
| `DOS_ROME_DEMO_ROLE` | Role | — | Dedicated demo role with all required grants |
| `DOS_ROME_DEMO_WH` | Warehouse (XS) | — | Dedicated demo warehouse, auto-suspend 120s |
| `DOS_ROME_DEMO` | Database | — | All demo objects live here |
| `CRM_CONTACTS` | Table (25 rows) | BRONZE | Diplomatic stakeholder organizations |
| `CRM_ACTIVITY_LOG` | Table (108 rows) | BRONZE | Interaction history (meetings, cables, calls, events, emails) |
| `SECTOR_INTELLIGENCE` | Table (59 rows) | BRONZE | External intel records per organization |
| `SUMMIT_ATTENDEES` | Table (28 rows) | BRONZE | Critical Minerals Summit roster |
| `MISSION_PRIORITIES` | Table (4 rows) | BRONZE | USUN Rome strategic priorities with weights |
| `POLICY_DOCUMENTS` | Table (6 rows) | BRONZE | Internal and external policy documents with full text |
| `POLICY_DOCS_SEARCH` | Cortex Search Service | SILVER | Semantic search over policy document text |
| `SECTOR_INTEL_SEARCH` | Cortex Search Service | SILVER | Semantic search over sector intelligence |
| `DOS_ROME_SV` | Semantic View | GOLD | Semantic model over CRM data for the Cortex Agent |
| `DOS_ROME_AGENT` | Cortex Agent | GOLD | Conversational AI assistant with 3 tools |
| `DOS_ROME_DASHBOARD` | Streamlit App | GOLD | Interactive dashboard (3 tabs) |
| `STREAMLIT_STAGE` | Stage | GOLD | Internal stage for Streamlit app files |

---

## Medallion Architecture

This demo organizes objects into three schemas following the **medallion architecture** pattern — BRONZE, SILVER, and GOLD — to separate raw data, processed/indexed data, and consumption-ready objects.

**BRONZE** holds the raw ingested data: CRM contacts, activity logs, summit rosters, mission priorities, and full-text policy documents. These tables represent the source-of-truth as received from CRM systems and external sources, with no transformation applied.

**SILVER** contains Cortex Search services that index and make the raw data semantically searchable. The two search services (policy documents and sector intelligence) process BRONZE data into vector-indexed form, enabling the LLM layer to retrieve relevant context via natural-language queries.

**GOLD** is the consumption layer — the semantic view, Cortex Agent, and Streamlit dashboard that analysts and diplomats interact with directly. These objects query across BRONZE (structured data) and SILVER (search services) to deliver enriched intelligence, event prioritization, and policy analysis.

---

## Data Overview

### CRM Contacts (25 organizations)

Stakeholders across critical minerals, food security, AI ethics, and bilateral energy — including Enel Green Power, ENI S.p.A., Albemarle Corporation, WFP, FAO PSAG, Pontifical Academy for Life, and Italian Ministry of Environment (MASE).

### Activity Log (108 interactions)

Diplomatic interaction history spanning June 2025 to August 2026: Ambassador meetings, diplomatic cables, DCM calls, ministerial events, and policy email exchanges.

### Sector Intelligence (59 records)

External reporting from Reuters, Bloomberg, FAO Press, State Dept cables, EU Monitor, Vatican Press Office, and trade press — covering the Critical Minerals Ministerial, EU CRMA implementation, WFP reform debates, Vatican AI ethics, and lithium market developments.

### Policy Documents (6 full-text documents)

| # | Document | Type | Classification |
|---|----------|------|---------------|
| 1 | EO 14179 — American AI Leadership | Executive Order | Internal |
| 2 | Critical Minerals Strategy 2026 | Strategic Document | Internal |
| 3 | USUN Rome Cable: WFP Accountability Review | Diplomatic Cable | Internal |
| 4 | Rome Call for AI Ethics (Updated 2025) | Multilateral Declaration | External |
| 5 | FAO Digital Agriculture and AI Strategy | Organizational Strategy | External |
| 6 | Italian G7 AI Declaration — Naples 2024 | G7 Declaration | External |

---

## Setup Instructions

### Prerequisites

- Snowflake account with ACCOUNTADMIN access (for initial role/warehouse creation)
- Snowflake CLI (`snow`) or SnowSQL for file staging

### Step-by-Step Setup

Run the SQL scripts in order from `sql/`:

```bash
# 1. Create role, warehouse, database, schemas (BRONZE, SILVER, GOLD), and grants
# Run sql/01_setup.sql in a Snowflake worksheet as ACCOUNTADMIN

# 2. Create tables
# Run sql/02_tables.sql

# 3. Load seed data
# Run sql/03_seed_data.sql

# 4. Create Cortex Search services (takes ~1-2 minutes to build indexes)
# Run sql/04_cortex_search_services.sql

# 5. Create semantic view
# Run sql/05_semantic_view.sql

# 6. Create Cortex Agent
# Run sql/06_cortex_agent.sql

# 7. Deploy Streamlit app
# First stage the files, then run sql/07_streamlit_deploy.sql
```

For the Streamlit deployment (step 7), you need to stage the app files first:

```sql
-- From SnowSQL, in the project root directory:
USE ROLE DOS_ROME_DEMO_ROLE;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA GOLD;

CREATE STAGE IF NOT EXISTS STREAMLIT_STAGE;
PUT file://streamlit/streamlit_app.py @STREAMLIT_STAGE/app AUTO_COMPRESS=FALSE OVERWRITE=TRUE;
PUT file://streamlit/pyproject.toml @STREAMLIT_STAGE/app AUTO_COMPRESS=FALSE OVERWRITE=TRUE;
```

Alternatively, deploy with the Snowflake CLI:

```bash
cd streamlit
snow streamlit deploy --replace
```

### Accessing the Demo

- **Dashboard:** In Snowsight, navigate to Projects > Streamlit > DOS_ROME_DASHBOARD
- **Agent:** In Snowsight, navigate to AI & ML > Agents > USUN Rome AI Assistant
  - Or use the agent in Snowflake Intelligence (CoWork)

---

## Teardown

To remove all demo objects:

```sql
-- Run sql/99_teardown.sql
-- This drops: agent, streamlit app, search services, semantic view, tables,
-- database, warehouse, and role — in reverse dependency order.
```

---

## File Structure

```
sql/
  01_setup.sql                  # Role, warehouse, database, schemas (BRONZE/SILVER/GOLD), grants
  02_tables.sql                 # All 6 table DDL statements
  03_seed_data.sql              # All INSERT statements (single consolidated file)
  04_cortex_search_services.sql # Cortex Search on policy docs + sector intel
  05_semantic_view.sql          # Semantic view for the Cortex Agent
  06_cortex_agent.sql           # Cortex Agent DDL
  07_streamlit_deploy.sql       # Stage + CREATE STREAMLIT
  99_teardown.sql               # Clean teardown of everything

streamlit/
  streamlit_app.py              # Streamlit-in-Snowflake dashboard
  pyproject.toml                # Python dependencies
  snowflake.yml                 # Snowflake CLI deployment config
```

---

## Technical Notes

- **LLM Model:** `mistral-large2` — chosen for good structured JSON output and fast response times suitable for a live demo.
- **Cortex Search Embedding:** Default model (`snowflake-arctic-embed-m-v1.5`) — fastest indexing, English-only is sufficient.
- **Streamlit Runtime:** Warehouse runtime (not container) — simpler setup with no compute pool required.
- **All data is synthetic.** Names, organizations, events, and policy documents are fabricated for demonstration purposes and do not represent real diplomatic positions or intelligence.
