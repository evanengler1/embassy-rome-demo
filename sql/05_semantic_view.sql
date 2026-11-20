-- =============================================================================
-- USUN Rome Demo | 05_semantic_view.sql
-- Creates a semantic view over CRM and summit data for the Cortex Agent.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA GOLD;

CREATE OR REPLACE SEMANTIC VIEW DOS_ROME_SV

  TABLES (
    contacts AS DOS_ROME_DEMO.BRONZE.CRM_CONTACTS
      PRIMARY KEY (ORG_NAME)
      COMMENT = 'Diplomatic stakeholder organizations tracked by USUN Rome',
    activity_log AS DOS_ROME_DEMO.BRONZE.CRM_ACTIVITY_LOG
      PRIMARY KEY (ACTIVITY_ID)
      COMMENT = 'Interaction history with stakeholder organizations',
    attendees AS DOS_ROME_DEMO.BRONZE.SUMMIT_ATTENDEES
      PRIMARY KEY (ATTENDEE_NAME)
      COMMENT = 'Critical Minerals Summit attendee roster'
  )

  RELATIONSHIPS (
    activity_to_contacts AS
      activity_log (ORG_NAME) REFERENCES contacts (ORG_NAME)
  )

  FACTS (
    activity_log.activity_org AS ORG_NAME
      COMMENT = 'Organization name from the activity log'
  )

  DIMENSIONS (
    contacts.org_name_dim AS ORG_NAME
      COMMENT = 'Organization name. Examples: Enel Green Power, ENI S.p.A., WFP.',
    contacts.sector_dim AS SECTOR
      COMMENT = 'Industry sector. Examples: Energy / Critical Minerals, Food Security / Humanitarian.',
    contacts.country_dim AS COUNTRY
      COMMENT = 'Country where the organization is based.',
    contacts.hq_city_dim AS HQ_CITY
      COMMENT = 'Headquarters city.',
    contacts.contact_name_dim AS PRIMARY_CONTACT_NAME
      COMMENT = 'Name of the primary contact person.',
    contacts.contact_title_dim AS PRIMARY_CONTACT_TITLE
      COMMENT = 'Title of the primary contact.',
    contacts.last_interaction_dim AS LAST_INTERACTION_DATE
      COMMENT = 'Date of the most recent interaction.',
    contacts.relationship_status_dim AS RELATIONSHIP_STATUS
      COMMENT = 'Relationship signal. Values: Warm, Neutral, Cool, Strategic.'
      SAMPLE_VALUES ('Warm', 'Neutral', 'Cool', 'Strategic')
      IS_ENUM,
    contacts.description_dim AS ORG_DESCRIPTION
      COMMENT = 'Brief description of the organization.',
    activity_log.activity_type_dim AS ACTIVITY_TYPE
      COMMENT = 'Interaction type. Values: Meeting, Cable, Call, Event, Email.'
      SAMPLE_VALUES ('Meeting', 'Cable', 'Call', 'Event', 'Email')
      IS_ENUM,
    activity_log.activity_date_dim AS ACTIVITY_DATE
      COMMENT = 'Date of the activity.',
    activity_log.activity_summary_dim AS SUMMARY
      COMMENT = 'Brief description of the activity.',
    activity_log.classification_dim AS CLASSIFICATION
      COMMENT = 'Importance. Values: Routine, Significant, High-Priority.'
      SAMPLE_VALUES ('Routine', 'Significant', 'High-Priority')
      IS_ENUM,
    attendees.attendee_name_dim AS ATTENDEE_NAME
      COMMENT = 'Full name of the summit attendee.',
    attendees.organization_dim AS ORGANIZATION
      COMMENT = 'Organization the attendee represents.',
    attendees.attendee_country_dim AS COUNTRY
      COMMENT = 'Country of the attendee.',
    attendees.attendee_title_dim AS TITLE
      COMMENT = 'Professional title.',
    attendees.attendee_sector_dim AS SECTOR
      COMMENT = 'Sector of the attendee.'
  )

  METRICS (
    activity_log.interaction_count AS COUNT(ACTIVITY_ID)
      COMMENT = 'Total number of interactions with an organization.',
    activity_log.high_priority_count AS SUM(IFF(CLASSIFICATION = 'High-Priority', 1, 0))
      COMMENT = 'Number of high-priority interactions.'
  )

  COMMENT = 'Semantic view for USUN Rome diplomatic CRM data';
