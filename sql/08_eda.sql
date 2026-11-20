-- =============================================================================
-- DOS Rome Demo | 08_eda.sql
-- Exploratory Data Analysis — a guided tour of the demo dataset.
-- Run these queries after setup to familiarize yourself with the data.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;


-- =============================================================================
-- SECTION 1 | CRM CONTACTS OVERVIEW
-- The stakeholder book: who USUN Rome tracks and how warm each relationship is.
-- =============================================================================

-- 1.1 Total contacts and breakdown by relationship signal (Warm/Neutral/Cool/Strategic).
SELECT
    relationship_status,
    COUNT(*)                                        AS contacts,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_of_book
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS
GROUP BY relationship_status
ORDER BY contacts DESC;

-- 1.2 Which countries host the most stakeholders?
SELECT
    country,
    COUNT(*) AS contacts,
    LISTAGG(org_name, ', ') WITHIN GROUP (ORDER BY org_name) AS organizations
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS
GROUP BY country
ORDER BY contacts DESC;

-- 1.3 What domains does the mission cover? (contacts by sector)
SELECT
    sector,
    COUNT(*) AS contacts
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS
GROUP BY sector
ORDER BY contacts DESC;

-- 1.4 A sample of contacts with their descriptions.
SELECT
    org_name,
    sector,
    country,
    relationship_status,
    org_description
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS
ORDER BY org_name
LIMIT 5;


-- =============================================================================
-- SECTION 2 | INTERACTION HISTORY
-- 108 logged interactions: meetings, cables, calls, events, and emails.
-- =============================================================================

-- 2.1 Total activities by type.
SELECT
    activity_type,
    COUNT(*) AS activities
FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
GROUP BY activity_type
ORDER BY activities DESC;

-- 2.2 Activities by classification (Routine / Significant / High-Priority).
SELECT
    classification,
    COUNT(*)                                          AS activities,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct
FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
GROUP BY classification
ORDER BY activities DESC;

-- 2.3 Most active organizations — top 10 by interaction count.
SELECT
    org_name,
    COUNT(*)                                           AS interactions,
    SUM(IFF(classification = 'High-Priority', 1, 0))   AS high_priority,
    MIN(activity_date)                                 AS first_touch,
    MAX(activity_date)                                 AS last_touch
FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
GROUP BY org_name
ORDER BY interactions DESC
LIMIT 10;

-- 2.4 High-priority engagement timeline — where the mission spent its senior attention.
SELECT
    activity_date,
    org_name,
    activity_type,
    participants,
    summary
FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
WHERE classification = 'High-Priority'
ORDER BY activity_date DESC;

-- 2.5 Most recent activity per organization (window function: latest touch per org).
SELECT
    org_name,
    activity_date AS last_activity_date,
    activity_type,
    summary
FROM (
    SELECT
        org_name,
        activity_date,
        activity_type,
        summary,
        ROW_NUMBER() OVER (PARTITION BY org_name ORDER BY activity_date DESC) AS rn
    FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
)
WHERE rn = 1
ORDER BY last_activity_date DESC;


-- =============================================================================
-- SECTION 3 | SECTOR INTELLIGENCE
-- 59 external intel records scored 1-100 for relevance to the mission.
-- =============================================================================

-- 3.1 Intel records by type (News / Regulatory / Partnership / Ministerial / Analysis).
SELECT
    intel_type,
    COUNT(*) AS records
FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
GROUP BY intel_type
ORDER BY records DESC;

-- 3.2 Average relevance score by organization — who carries the highest-signal intel?
SELECT
    org_name,
    COUNT(*)                    AS intel_records,
    ROUND(AVG(relevance_score)) AS avg_relevance,
    MAX(relevance_score)        AS top_relevance
FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
GROUP BY org_name
HAVING COUNT(*) >= 2
ORDER BY avg_relevance DESC;

-- 3.3 Top intel headlines by relevance score.
SELECT
    relevance_score,
    org_name,
    intel_type,
    intel_date,
    headline,
    source
FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
ORDER BY relevance_score DESC
LIMIT 10;

-- 3.4 Intel timeline — how coverage builds quarter over quarter.
SELECT
    DATE_TRUNC('quarter', intel_date)  AS quarter,
    COUNT(*)                           AS records,
    ROUND(AVG(relevance_score))        AS avg_relevance
FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
GROUP BY quarter
ORDER BY quarter;


-- =============================================================================
-- SECTION 4 | SUMMIT ATTENDEES
-- The 28-person Critical Minerals Summit roster.
-- =============================================================================

-- 4.1 Attendees by sector.
SELECT
    sector,
    COUNT(*) AS attendees
FROM DOS_ROME_DEMO.BRONZE.SUMMIT_ATTENDEES
GROUP BY sector
ORDER BY attendees DESC;

-- 4.2 Attendees by country.
SELECT
    country,
    COUNT(*) AS attendees
FROM DOS_ROME_DEMO.BRONZE.SUMMIT_ATTENDEES
GROUP BY country
ORDER BY attendees DESC;

-- 4.3 Cross-reference: which summit attendees represent orgs already in the CRM?
--     These are known stakeholders the Ambassador can prioritize on sight.
SELECT
    a.attendee_name,
    a.title,
    a.organization,
    a.country,
    c.relationship_status,
    c.sector AS crm_sector
FROM DOS_ROME_DEMO.BRONZE.SUMMIT_ATTENDEES a
INNER JOIN DOS_ROME_DEMO.BRONZE.CRM_CONTACTS c
    ON a.organization = c.org_name
ORDER BY c.relationship_status, a.organization;


-- =============================================================================
-- SECTION 5 | MISSION PRIORITIES
-- The 4 weighted strategic priorities that drive scoring across the demo.
-- =============================================================================

-- 5.1 All priorities with their weights, heaviest first.
SELECT
    priority_id,
    priority_name,
    weight,
    status,
    description
FROM DOS_ROME_DEMO.BRONZE.MISSION_PRIORITIES
ORDER BY weight DESC;

-- 5.2 Which CRM contacts align with which priority?
--     Heuristic: match the leading token of each contact's sector against the
--     priority description text via ILIKE. This is a rough keyword join meant to
--     illustrate alignment, not an authoritative mapping.
SELECT
    p.priority_name,
    p.weight,
    c.org_name,
    c.sector,
    c.relationship_status
FROM DOS_ROME_DEMO.BRONZE.MISSION_PRIORITIES p
JOIN DOS_ROME_DEMO.BRONZE.CRM_CONTACTS c
    ON p.description ILIKE '%' || SPLIT_PART(c.sector, ' / ', 1) || '%'
ORDER BY p.weight DESC, c.org_name;


-- =============================================================================
-- SECTION 6 | POLICY DOCUMENTS
-- 6 full-text documents — internal U.S. positions and external partner texts.
-- =============================================================================

-- 6.1 Document inventory with size metrics (character length and est. word count).
SELECT
    doc_id,
    doc_title,
    doc_type,
    issuer,
    classification,
    issue_date,
    LENGTH(full_text)                     AS chars,
    ARRAY_SIZE(SPLIT(full_text, ' '))     AS est_words
FROM DOS_ROME_DEMO.BRONZE.POLICY_DOCUMENTS
ORDER BY issue_date;

-- 6.2 Internal vs external comparison — count and average document length.
SELECT
    classification,
    COUNT(*)                     AS documents,
    ROUND(AVG(LENGTH(full_text))) AS avg_chars
FROM DOS_ROME_DEMO.BRONZE.POLICY_DOCUMENTS
GROUP BY classification
ORDER BY classification;

-- 6.3 Preview of each document's summary.
SELECT
    doc_title,
    classification,
    summary
FROM DOS_ROME_DEMO.BRONZE.POLICY_DOCUMENTS
ORDER BY doc_id;


-- =============================================================================
-- SECTION 7 | CROSS-TABLE ANALYTICS
-- Where the value shows: structured data joined into stakeholder intelligence.
-- =============================================================================

-- 7.1 Full stakeholder profile — one row per contact, enriched with activity and
--     intel aggregates. This is the 360-degree view the enrichment pipeline builds on.
SELECT
    c.org_name,
    c.sector,
    c.relationship_status,
    COALESCE(act.interactions, 0)      AS interactions,
    act.last_activity_date,
    COALESCE(intel.intel_records, 0)   AS intel_records,
    intel.avg_relevance
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS c
LEFT JOIN (
    SELECT org_name,
           COUNT(*)           AS interactions,
           MAX(activity_date) AS last_activity_date
    FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
    GROUP BY org_name
) act  ON c.org_name = act.org_name
LEFT JOIN (
    SELECT org_name,
           COUNT(*)                    AS intel_records,
           ROUND(AVG(relevance_score)) AS avg_relevance
    FROM DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE
    GROUP BY org_name
) intel ON c.org_name = intel.org_name
ORDER BY interactions DESC, intel_records DESC;

-- 7.2 Relationship gap analysis — Cool/Neutral contacts carrying high-signal intel.
--     These are underengaged stakeholders where external activity outpaces our own.
SELECT
    c.org_name,
    c.relationship_status,
    c.sector,
    COUNT(i.intel_id)           AS intel_records,
    ROUND(AVG(i.relevance_score)) AS avg_relevance,
    MAX(i.relevance_score)      AS top_relevance
FROM DOS_ROME_DEMO.BRONZE.CRM_CONTACTS c
JOIN DOS_ROME_DEMO.BRONZE.SECTOR_INTELLIGENCE i
    ON c.org_name = i.org_name
WHERE c.relationship_status IN ('Cool', 'Neutral')
GROUP BY c.org_name, c.relationship_status, c.sector
HAVING AVG(i.relevance_score) >= 70
ORDER BY avg_relevance DESC;

-- 7.3 Engagement intensity — share of interactions that were high-priority per org.
SELECT
    org_name,
    COUNT(*)                                              AS total_interactions,
    SUM(IFF(classification = 'High-Priority', 1, 0))      AS high_priority,
    ROUND(100.0 * SUM(IFF(classification = 'High-Priority', 1, 0)) / COUNT(*), 1)
                                                          AS high_priority_pct
FROM DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
GROUP BY org_name
HAVING COUNT(*) >= 3
ORDER BY high_priority_pct DESC, total_interactions DESC;


-- =============================================================================
-- SECTION 8 | CORTEX SEARCH PREVIEW
-- Semantic retrieval over the SILVER search services (no LLM call required).
-- =============================================================================

-- 8.1 Policy document search: "AI governance ethics".
SELECT
    r.value:doc_title::STRING      AS doc_title,
    r.value:doc_type::STRING       AS doc_type,
    r.value:classification::STRING AS classification,
    r.value:summary::STRING        AS summary
FROM TABLE(FLATTEN(
    input => PARSE_JSON(
        SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
            'DOS_ROME_DEMO.SILVER.POLICY_DOCS_SEARCH',
            '{
               "query": "AI governance ethics",
               "columns": ["doc_title", "doc_type", "classification", "summary"],
               "limit": 5
             }'
        )
    ):results
)) r;

-- 8.2 Sector intelligence search: "lithium supply chain".
SELECT
    r.value:org_name::STRING   AS org_name,
    r.value:intel_type::STRING AS intel_type,
    r.value:headline::STRING   AS headline,
    r.value:summary::STRING    AS summary
FROM TABLE(FLATTEN(
    input => PARSE_JSON(
        SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
            'DOS_ROME_DEMO.SILVER.SECTOR_INTEL_SEARCH',
            '{
               "query": "lithium supply chain",
               "columns": ["org_name", "intel_type", "headline", "summary"],
               "limit": 5
             }'
        )
    ):results
)) r;

-- 8.3 Sector intelligence search with an attribute filter: "reform", org_name = 'WFP'.
SELECT
    r.value:org_name::STRING   AS org_name,
    r.value:intel_type::STRING AS intel_type,
    r.value:headline::STRING   AS headline,
    r.value:summary::STRING    AS summary
FROM TABLE(FLATTEN(
    input => PARSE_JSON(
        SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
            'DOS_ROME_DEMO.SILVER.SECTOR_INTEL_SEARCH',
            '{
               "query": "reform",
               "columns": ["org_name", "intel_type", "headline", "summary"],
               "filter": {"@eq": {"org_name": "WFP"}},
               "limit": 5
             }'
        )
    ):results
)) r;


-- =============================================================================
-- SECTION 9 | SEMANTIC VIEW QUERY
-- The same CRM data the Cortex Agent reasons over, queried directly.
-- =============================================================================

-- 9.1 Interaction counts by organization, straight from the semantic view.
SELECT *
FROM SEMANTIC_VIEW(
    DOS_ROME_DEMO.GOLD.DOS_ROME_SV
    DIMENSIONS contacts.org_name_dim
    METRICS    activity_log.interaction_count
)
ORDER BY interaction_count DESC;

-- =============================================================================
-- End of guided tour.
-- =============================================================================
