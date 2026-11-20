-- =============================================================================
-- USUN Rome Demo | 06_cortex_agent.sql
-- Creates the Cortex Agent for conversational access to demo data.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA GOLD;

CREATE AGENT DOS_ROME_DEMO.GOLD.DOS_ROME_AGENT
  COMMENT = 'USUN Rome diplomatic operations assistant'
  PROFILE = '{"display_name": "USUN Rome AI Assistant", "color": "blue"}'
  FROM SPECIFICATION
  $$
  models:
    orchestration: auto

  orchestration:
    capabilities:
      analytical_search: true
    tool_not_accessible: accept
    budget:
      seconds: 60
      tokens: 32000

  instructions:
    response: >
      You are an AI assistant for the U.S. Mission to the UN Agencies in Rome (USUN Rome).
      You help diplomatic staff with stakeholder intelligence, event preparation, and policy analysis.
      Respond in a professional, concise diplomatic tone. When providing stakeholder assessments,
      include the relationship status and relevant recent activity. When discussing policy alignment,
      identify both points of agreement and tension.
    orchestration: >
      For questions about CRM contacts, interaction history, relationship status, summit attendees,
      or any structured data queries, use the CRMAnalyst tool with the semantic view.
      For questions about policy documents, diplomatic guidance, alignment analysis, executive orders,
      or multilateral declarations, use the PolicySearch tool.
      For questions about sector intelligence, organizational news, market developments,
      or external reporting, use the IntelSearch tool.
      When a question spans multiple domains, use multiple tools and synthesize the results.
    sample_questions:
      - question: "What do we know about Enel Green Power?"
      - question: "Who should the Ambassador prioritize at the summit for critical minerals?"
      - question: "How does our AI executive order align with the Vatican's Rome Call?"
      - question: "Draft talking points for the Ambassador's meeting with the FAO Deputy Director-General."
      - question: "Which CRM contacts have a relationship gap we should address?"
      - question: "What is the latest intelligence on WFP reform progress?"

  tools:
    - tool_spec:
        type: cortex_analyst_text_to_sql
        name: CRMAnalyst
        description: "Query structured CRM contact data, diplomatic interaction history, relationship status, and summit attendee information for USUN Rome stakeholder organizations."
    - tool_spec:
        type: cortex_search
        name: PolicySearch
        description: "Search internal and external policy documents including executive orders, strategic documents, diplomatic cables, multilateral declarations, and organizational strategies relevant to USUN Rome priorities."
    - tool_spec:
        type: cortex_search
        name: IntelSearch
        description: "Search sector intelligence reports covering news, regulatory developments, partnerships, ministerial activities, and analytical assessments for USUN Rome stakeholder organizations."

  tool_resources:
    CRMAnalyst:
      semantic_view: "DOS_ROME_DEMO.GOLD.DOS_ROME_SV"
    PolicySearch:
      search_service: "DOS_ROME_DEMO.SILVER.POLICY_DOCS_SEARCH"
      max_results: "5"
      title_column: "DOC_TITLE"
    IntelSearch:
      search_service: "DOS_ROME_DEMO.SILVER.SECTOR_INTEL_SEARCH"
      max_results: "5"
      title_column: "HEADLINE"
  $$;
