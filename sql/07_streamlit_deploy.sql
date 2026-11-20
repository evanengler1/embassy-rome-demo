-- =============================================================================
-- USUN Rome Demo | 07_streamlit_deploy.sql
-- Stages Streamlit files and creates the Streamlit-in-Snowflake app.
-- Run this from the project root directory.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA GOLD;

-- Create a stage for the Streamlit app files
CREATE STAGE IF NOT EXISTS STREAMLIT_STAGE;

-- Upload files to stage (run these PUT commands from SnowSQL or Snowflake CLI)
-- PUT file://streamlit/streamlit_app.py @STREAMLIT_STAGE/app AUTO_COMPRESS=FALSE OVERWRITE=TRUE;
-- PUT file://streamlit/pyproject.toml @STREAMLIT_STAGE/app AUTO_COMPRESS=FALSE OVERWRITE=TRUE;

-- Create the Streamlit app (warehouse runtime for simplicity)
CREATE OR REPLACE STREAMLIT DOS_ROME_DASHBOARD
  FROM '@STREAMLIT_STAGE/app'
  MAIN_FILE = 'streamlit_app.py'
  QUERY_WAREHOUSE = DOS_ROME_DEMO_WH;

ALTER STREAMLIT DOS_ROME_DASHBOARD ADD LIVE VERSION FROM LAST;
