-- =============================================================================
-- USUN Rome Demo | 02_tables.sql
-- Creates all 6 tables for the demo data foundation.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA BRONZE;

-- CRM Contacts: diplomatic stakeholder organizations
CREATE OR REPLACE TABLE CRM_CONTACTS (
    org_name            VARCHAR     NOT NULL,
    sector              VARCHAR,
    country             VARCHAR,
    hq_city             VARCHAR,
    primary_contact_name   VARCHAR,
    primary_contact_title  VARCHAR,
    last_interaction_date  DATE,
    relationship_status VARCHAR,   -- Warm / Neutral / Cool / Strategic
    org_description     VARCHAR,
    PRIMARY KEY (org_name)
);

-- CRM Activity Log: interaction history with stakeholders
CREATE OR REPLACE TABLE CRM_ACTIVITY_LOG (
    activity_id         INT         NOT NULL,
    org_name            VARCHAR     NOT NULL,
    activity_type       VARCHAR,   -- Meeting / Cable / Call / Event / Email
    activity_date       DATE,
    summary             VARCHAR,
    participants        VARCHAR,
    classification      VARCHAR,   -- Routine / Significant / High-Priority
    PRIMARY KEY (activity_id)
);

-- Sector Intelligence: external intel records per organization
CREATE OR REPLACE TABLE SECTOR_INTELLIGENCE (
    intel_id            INT         NOT NULL,
    org_name            VARCHAR,
    intel_type          VARCHAR,   -- News / Regulatory / Partnership / Ministerial / Analysis
    intel_date          DATE,
    headline            VARCHAR,
    summary             VARCHAR,
    source              VARCHAR,
    relevance_score     INT,       -- 1-100
    PRIMARY KEY (intel_id)
);

-- Summit Attendees: Critical Minerals Summit roster
CREATE OR REPLACE TABLE SUMMIT_ATTENDEES (
    attendee_name       VARCHAR     NOT NULL,
    organization        VARCHAR,
    country             VARCHAR,
    title               VARCHAR,
    sector              VARCHAR,
    PRIMARY KEY (attendee_name)
);

-- Mission Priorities: USUN Rome strategic priorities with weights
CREATE OR REPLACE TABLE MISSION_PRIORITIES (
    priority_id         INT         NOT NULL,
    priority_name       VARCHAR,
    description         VARCHAR,
    weight              FLOAT,     -- 0.0 to 1.0
    status              VARCHAR,   -- Active / Monitoring
    PRIMARY KEY (priority_id)
);

-- Policy Documents: internal and external documents for Cortex Search
CREATE OR REPLACE TABLE POLICY_DOCUMENTS (
    doc_id              INT         NOT NULL,
    doc_title           VARCHAR,
    doc_type            VARCHAR,   -- Executive Order / Strategic Document / Diplomatic Cable / Declaration / Strategy
    issuer              VARCHAR,
    issue_date          DATE,
    classification      VARCHAR,   -- Internal / External
    full_text           VARCHAR,
    summary             VARCHAR,
    PRIMARY KEY (doc_id)
);
