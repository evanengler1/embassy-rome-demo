-- =============================================================================
-- USUN Rome Demo | 04_cortex_search_services.sql
-- Creates Cortex Search services for policy documents and sector intelligence.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA SILVER;

-- Policy Documents Search: semantic search over full policy document text
CREATE OR REPLACE CORTEX SEARCH SERVICE POLICY_DOCS_SEARCH
  ON full_text
  ATTRIBUTES doc_title, doc_type, classification, issuer
  WAREHOUSE = DOS_ROME_DEMO_WH
  TARGET_LAG = '1 day'
AS (
  SELECT
    doc_id,
    doc_title,
    doc_type,
    issuer,
    issue_date,
    classification,
    full_text,
    summary
  FROM DOS_ROME_DEMO.BRONZE.POLICY_DOCUMENTS
);

-- Sector Intelligence Search: semantic search over intel summaries
CREATE OR REPLACE CORTEX SEARCH SERVICE SECTOR_INTEL_SEARCH
  ON summary
  ATTRIBUTES org_name, intel_type, source
  WAREHOUSE = DOS_ROME_DEMO_WH
  TARGET_LAG = '1 day'
AS (
  SELECT
    intel_id,
    org_name,
    intel_type,
    intel_date,
    headline,
    summary,
    source,
    relevance_score
  FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
);
