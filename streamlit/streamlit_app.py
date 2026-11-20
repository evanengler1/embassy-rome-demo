# streamlit_app.py
# ─────────────────────────────────────────────────────────────────────────────
# U.S. Embassy Rome | Snowflake AI Data Cloud Demo  —  Streamlit-in-Snowflake (LIVE)
# Use Cases: CRM Enrichment → Event Prioritization → Policy Alignment
#
# This app runs INSIDE Snowflake (Streamlit-in-Snowflake).
#   • Session comes from snowflake.snowpark.context.get_active_session()
#   • All data comes from live tables in DOS_ROME_DEMO.BRONZE
#   • All AI output comes from live SNOWFLAKE.CORTEX calls
# ─────────────────────────────────────────────────────────────────────────────

import json
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.set_page_config(
    page_title="U.S. Embassy Rome — Snowflake AI Demo",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

DB_SCHEMA = "DOS_ROME_DEMO.BRONZE"
MODEL = "mistral-large2"
POLICY_SEARCH = "DOS_ROME_DEMO.SILVER.POLICY_DOCS_SEARCH"
SECTOR_SEARCH = "DOS_ROME_DEMO.SILVER.SECTOR_INTEL_SEARCH"

session = get_active_session()


# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS — glossy dark theme with glass cards and gradient accents
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Base ─────────────────────────────────────────────────────────────────── */
.stApp {
    background:
        radial-gradient(1200px 500px at 80% -10%, rgba(41,181,232,0.10), transparent 60%),
        radial-gradient(900px 400px at -10% 110%, rgba(99,102,241,0.08), transparent 60%),
        linear-gradient(180deg, #0b1220 0%, #0e1729 100%);
    background-attachment: fixed;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c1526 0%, #0a1120 100%) !important;
    border-right: 1px solid rgba(148,163,184,0.15) !important;
}
section[data-testid="stSidebar"] * { color: #cbd5e1 !important; }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 { color: #f1f5f9 !important; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }

/* ── Hero banner ──────────────────────────────────────────────────────────── */
.hero {
    position: relative; overflow: hidden;
    background: linear-gradient(120deg, #0a2a4a 0%, #0e4d75 45%, #29B5E8 160%);
    border: 1px solid rgba(41,181,232,0.35);
    border-radius: 16px; padding: 26px 32px 22px; margin-bottom: 22px;
    box-shadow: 0 8px 32px rgba(14,77,117,0.45), inset 0 1px 0 rgba(255,255,255,0.12);
}
.hero::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.07) 50%, transparent 60%);
    pointer-events: none;
}
.hero .kicker {
    font-size: 11px; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase;
    color: #7dd3fc; margin-bottom: 6px;
}
.hero h1 {
    color: #ffffff; font-size: 26px; font-weight: 800; margin: 0 0 4px 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.35);
}
.hero .sub { color: rgba(224,242,254,0.75); font-size: 13px; }
.hero .chips { margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap; }
.chip {
    display: inline-block; padding: 4px 12px; border-radius: 999px;
    font-size: 11px; font-weight: 600; letter-spacing: 0.03em;
    background: rgba(255,255,255,0.10); border: 1px solid rgba(255,255,255,0.22);
    color: #e0f2fe; backdrop-filter: blur(4px);
}
.chip-accent { background: rgba(41,181,232,0.25); border-color: rgba(41,181,232,0.55); color: #bae6fd; }

/* ── Glass cards ──────────────────────────────────────────────────────────── */
.glass {
    background: linear-gradient(180deg, rgba(30,41,59,0.75), rgba(15,23,42,0.65));
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 14px; padding: 20px 22px; margin-bottom: 14px;
    box-shadow: 0 4px 24px rgba(2,6,23,0.45), inset 0 1px 0 rgba(255,255,255,0.06);
    backdrop-filter: blur(8px);
}
.glass-title { font-size: 15px; font-weight: 700; color: #f1f5f9; margin-bottom: 2px; }
.glass-sub   { font-size: 12px; color: #94a3b8; }
.kv { margin-top: 12px; font-size: 13px; color: #cbd5e1; line-height: 1.9; }
.kv b { color: #e2e8f0; font-weight: 600; }
.muted { font-size: 11px; color: #64748b; margin-top: 10px; }

/* ── Badges & metrics ─────────────────────────────────────────────────────── */
.badge {
    display: inline-block; padding: 4px 14px; border-radius: 999px;
    font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
}
.badge-warm      { background: rgba(34,197,94,0.16);  color: #86efac; border: 1px solid rgba(34,197,94,0.45); }
.badge-neutral   { background: rgba(56,189,248,0.14); color: #7dd3fc; border: 1px solid rgba(56,189,248,0.45); }
.badge-cool      { background: rgba(167,139,250,0.14); color: #c4b5fd; border: 1px solid rgba(167,139,250,0.45); }
.badge-strategic { background: rgba(251,191,36,0.14); color: #fcd34d; border: 1px solid rgba(251,191,36,0.45); }

.metric-tile {
    background: linear-gradient(180deg, rgba(30,41,59,0.85), rgba(15,23,42,0.75));
    border: 1px solid rgba(148,163,184,0.20);
    border-radius: 14px; padding: 16px 20px; text-align: center;
    box-shadow: 0 4px 18px rgba(2,6,23,0.4), inset 0 1px 0 rgba(255,255,255,0.07);
}
.metric-num {
    font-size: 42px; font-weight: 800; line-height: 1.05;
    background: linear-gradient(135deg, #7dd3fc 0%, #29B5E8 60%);
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
    text-shadow: 0 0 28px rgba(41,181,232,0.35);
}
.metric-num-good  { background: linear-gradient(135deg, #86efac, #22c55e); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.metric-num-warn  { background: linear-gradient(135deg, #fcd34d, #f59e0b); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.metric-num-low   { background: linear-gradient(135deg, #fca5a5, #ef4444); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.metric-lbl { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #94a3b8; margin-top: 6px; }

/* ── Score bar ────────────────────────────────────────────────────────────── */
.bar-track {
    height: 8px; border-radius: 999px; margin: 10px 0 4px 0;
    background: rgba(148,163,184,0.15); overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.4);
}
.bar-fill {
    height: 100%; border-radius: 999px;
    background: linear-gradient(90deg, #0369a1, #29B5E8 70%, #7dd3fc);
    box-shadow: 0 0 12px rgba(41,181,232,0.55);
}
.bar-caption { font-size: 11px; color: #7dd3fc; font-weight: 600; }

/* ── Callouts & summaries ────────────────────────────────────────────────── */
.sect-lbl {
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.14em; color: #64a7c9; margin: 18px 0 8px 0;
}
.summary-text { font-size: 14px; color: #dbe4f0; line-height: 1.8; }
.callout {
    background: linear-gradient(120deg, rgba(41,181,232,0.12), rgba(41,181,232,0.05));
    border: 1px solid rgba(41,181,232,0.35); border-left: 4px solid #29B5E8;
    border-radius: 0 12px 12px 0; padding: 14px 18px; margin-top: 12px;
    font-size: 14px; color: #e2e8f0; line-height: 1.7;
    box-shadow: 0 2px 16px rgba(41,181,232,0.12);
}
.callout b, .callout strong { color: #7dd3fc; }
.src-note { font-size: 11px; color: #5874a0; margin-top: 12px; }

/* ── Priority cards ───────────────────────────────────────────────────────── */
.prio-card {
    background: linear-gradient(180deg, rgba(30,41,59,0.8), rgba(15,23,42,0.7));
    border: 1px solid rgba(148,163,184,0.18); border-left: 4px solid #29B5E8;
    border-radius: 0 14px 14px 0; padding: 16px 20px; margin-bottom: 12px;
    box-shadow: 0 4px 18px rgba(2,6,23,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
}
.prio-rank {
    display: inline-flex; align-items: center; justify-content: center;
    width: 34px; height: 34px; border-radius: 10px; margin-right: 12px;
    background: linear-gradient(135deg, #0e4d75, #29B5E8);
    color: #fff; font-size: 16px; font-weight: 800;
    box-shadow: 0 0 16px rgba(41,181,232,0.45);
    float: left;
}
.prio-name { font-size: 15px; font-weight: 700; color: #f1f5f9; }
.prio-org  { font-size: 12px; color: #94a3b8; margin: 2px 0 8px 0; }
.prio-rat  { font-size: 13px; color: #cbd5e1; line-height: 1.7; margin: 8px 0; clear: both; }
.prio-open {
    background: rgba(41,181,232,0.08); border-left: 3px solid #29B5E8;
    border-radius: 0 10px 10px 0; padding: 10px 14px;
    font-size: 13px; color: #7dd3fc; font-style: italic; line-height: 1.6;
}
.route-note {
    background: rgba(148,163,184,0.08); border: 1px solid rgba(148,163,184,0.2);
    border-radius: 12px; padding: 12px 16px; margin-top: 14px;
    font-size: 12px; color: #94a3b8; line-height: 1.6;
}
.route-note b { color: #cbd5e1; }

/* ── Policy alignment ─────────────────────────────────────────────────────── */
.doc-card {
    background: linear-gradient(180deg, rgba(30,41,59,0.8), rgba(15,23,42,0.7));
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 14px; padding: 18px 20px;
    box-shadow: 0 4px 18px rgba(2,6,23,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
}
.doc-kicker { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: #64a7c9; margin-bottom: 6px; }
.doc-title  { font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 4px; line-height: 1.45; }
.doc-meta   { font-size: 12px; color: #94a3b8; margin-bottom: 10px; }
.doc-prev   { font-size: 12px; color: #8ba3c0; line-height: 1.65; }

.gauge-wrap {
    text-align: center; padding: 22px 12px;
    background: linear-gradient(180deg, rgba(30,41,59,0.85), rgba(15,23,42,0.75));
    border: 1px solid rgba(148,163,184,0.2); border-radius: 14px;
    box-shadow: 0 4px 24px rgba(2,6,23,0.45), inset 0 1px 0 rgba(255,255,255,0.07);
}
.gauge-num { font-size: 52px; font-weight: 800; line-height: 1; }
.gauge-lbl { font-size: 12px; color: #cbd5e1; margin-top: 8px; line-height: 1.5; }

.agree-item, .tension-item {
    display: flex; gap: 10px; align-items: flex-start; margin-bottom: 10px;
    font-size: 13.5px; line-height: 1.65;
}
.agree-item   { color: #a5e5bf; }
.tension-item { color: #f3b0b0; }
.agree-item .mark   { color: #34d399; font-weight: 800; }
.tension-item .mark { color: #f87171; font-weight: 800; }

.approach-box {
    background: linear-gradient(120deg, rgba(41,181,232,0.10), rgba(99,102,241,0.07));
    border: 1px solid rgba(41,181,232,0.28);
    border-radius: 12px; padding: 16px 18px;
    font-size: 13.5px; color: #cfe1f2; line-height: 1.8;
}

.tp-box {
    background: linear-gradient(180deg, rgba(30,41,59,0.8), rgba(15,23,42,0.7));
    border: 1px solid rgba(148,163,184,0.18); border-left: 3px solid #7dd3fc;
    border-radius: 0 12px 12px 0; padding: 12px 16px; margin-bottom: 10px;
    font-size: 13.5px; color: #e2e8f0; font-style: italic; line-height: 1.7;
    box-shadow: 0 2px 12px rgba(2,6,23,0.35);
}

/* ── Controls ─────────────────────────────────────────────────────────────── */
div[data-baseweb="radio"] { border-radius: 10px; }
.stRadio > label, .stRadio > label * { color: #f1f5f9 !important; }

button[kind="primary"] {
    background: linear-gradient(135deg, #0369a1 0%, #29B5E8 100%) !important;
    border: 1px solid rgba(41,181,232,0.6) !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 18px rgba(41,181,232,0.35), inset 0 1px 0 rgba(255,255,255,0.25) !important;
    font-weight: 600 !important;
    transition: all 0.2s ease;
}
button[kind="primary"]:hover {
    box-shadow: 0 6px 26px rgba(41,181,232,0.55), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    transform: translateY(-1px);
}

button[data-baseweb="tab"] {
    border-radius: 10px 10px 0 0 !important;
    font-size: 14px !important; font-weight: 600 !important;
    color: #94a3b8 !important;
    background: transparent !important;
    padding: 8px 18px !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #7dd3fc !important;
    background: rgba(41,181,232,0.10) !important;
    text-shadow: 0 0 18px rgba(41,181,232,0.5);
}
.stTabs, [data-testid="stTabs"], [role="tablist"],
[data-baseweb="tab-list"], [data-baseweb="tab-border"], [data-baseweb="tab-highlight"] {
    background-color: transparent !important; background: transparent !important;
}

/* ── Dataframe polish ─────────────────────────────────────────────────────── */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(148,163,184,0.18) !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 18px rgba(2,6,23,0.35) !important;
}

/* ── Typography — global text visibility on dark backgrounds ──────────────── */
h1, h2, h3, h4, h5, h6 { color: #e8f1f8 !important; font-weight: 700 !important; }
.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span { color: #cbd5e1 !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6 { color: #e8f1f8 !important; }
.stMarkdown strong, .stMarkdown b { color: #f1f5f9 !important; }
.stMarkdown a { color: #7dd3fc !important; }

/* Widget labels (selectbox, radio, etc.) */
.stSelectbox label, .stSelectbox label *,
.stRadio > div > label, .stRadio > div > label *,
.stTextInput label, .stTextInput label *,
.stTextArea label, .stTextArea label *,
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] * { color: #f1f5f9 !important; }

/* Captions */
.stCaption, [data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] * { color: #8ba3c0 !important; }

/* Selectbox / dropdown — dark background with bright text */
div[data-baseweb="select"] > div {
    background: rgba(15,23,42,0.85) !important;
    border-color: rgba(148,163,184,0.35) !important;
}
div[data-baseweb="select"] * { color: #f1f5f9 !important; }
div[data-baseweb="select"] input { color: #f1f5f9 !important; }
div[data-baseweb="select"] svg { fill: #94a3b8 !important; }
div[data-baseweb="select"] [data-baseweb="tag"] span { color: #f1f5f9 !important; }
/* Dropdown menu — force dark on every possible container */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] ul,
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
ul[role="listbox"],
ul[role="listbox"] > li,
div[data-baseweb="popover"] *,
div[data-baseweb="select"] ~ div,
div[data-baseweb="select"] ~ div * {
    background: #0f172a !important;
    background-color: #0f172a !important;
}
[data-baseweb="popover"] li,
[data-baseweb="menu"] li,
ul[role="listbox"] li,
ul[role="listbox"] li * {
    color: #e2e8f0 !important;
    background: #0f172a !important;
}
[data-baseweb="popover"] li:hover,
[data-baseweb="popover"] li:focus,
[data-baseweb="popover"] li[aria-selected="true"],
[data-baseweb="menu"] li:hover,
[data-baseweb="menu"] li:focus,
[data-baseweb="menu"] li[aria-selected="true"],
ul[role="listbox"] li:hover,
ul[role="listbox"] li[aria-selected="true"] {
    background: rgba(41,181,232,0.20) !important;
    background-color: rgba(41,181,232,0.20) !important;
    color: #ffffff !important;
}

/* Radio buttons — bright white text */
.stRadio label, .stRadio label *,
.stRadio [role="radiogroup"] label,
.stRadio [role="radiogroup"] label * { color: #f1f5f9 !important; }
.stRadio [role="radiogroup"] label div[data-testid="stMarkdownContainer"],
.stRadio [role="radiogroup"] label div[data-testid="stMarkdownContainer"] * { color: #f1f5f9 !important; }

/* Metrics */
[data-testid="stMetricValue"] { color: #f1f5f9 !important; }
[data-testid="stMetricLabel"] label,
[data-testid="stMetricLabel"] { color: #94a3b8 !important; }
[data-testid="stMetricDelta"] { color: #7dd3fc !important; }

/* Info, warning, error, success boxes */
[data-testid="stAlert"] { background: rgba(30,41,59,0.75) !important; border-radius: 10px !important; }
[data-testid="stAlert"] p,
[data-testid="stAlert"] span,
.stAlert p, .stAlert span,
div[role="alert"] p, div[role="alert"] span { color: #cbd5e1 !important; }

/* Spinner */
.stSpinner > div, .stSpinner > div * { color: #7dd3fc !important; }

/* Expander */
.streamlit-expanderHeader, .streamlit-expanderHeader p { color: #e2e8f0 !important; }

/* Tab text (reiterated with broader selectors) */
[data-baseweb="tab-panel"] p,
[data-baseweb="tab-panel"] span,
[data-baseweb="tab-panel"] li { color: #cbd5e1; }

/* Progress bar label */
.stProgress > div > div > div { color: #7dd3fc !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS — SQL, Cortex, JSON parsing
# ─────────────────────────────────────────────────────────────────────────────
def sql_escape(text):
    """Escape a Python string for safe embedding in a Snowflake SQL string literal."""
    if text is None:
        return ""
    return str(text).replace("\\", "\\\\").replace("'", "''")


def row_val(row, *candidates):
    """Case-insensitive, tolerant read of a Snowpark Row value by candidate column names."""
    try:
        d = row.as_dict()
    except Exception:
        d = dict(row)
    upper_map = {str(k).upper(): v for k, v in d.items()}
    for cand in candidates:
        v = upper_map.get(str(cand).upper())
        if v is not None and str(v).strip() != "":
            return v
    return ""


def parse_llm_json(text):
    """Strip markdown code fences and parse JSON from an LLM response."""
    text = (text or "").strip()
    if text.startswith("```"):
        # drop the opening fence line (``` or ```json)
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    if text.startswith("json"):
        text = text[4:].strip()
    # As a last resort, isolate the outermost JSON object/array
    if not (text.startswith("{") or text.startswith("[")):
        first_obj, first_arr = text.find("{"), text.find("[")
        starts = [p for p in (first_obj, first_arr) if p != -1]
        if starts:
            start = min(starts)
            end = max(text.rfind("}"), text.rfind("]"))
            if end > start:
                text = text[start:end + 1]
    return json.loads(text)


def cortex_complete(system_prompt, user_prompt, temperature=0.1, max_tokens=4096):
    """Chat-style CORTEX.COMPLETE call with temperature control; returns the text content."""
    sys_e = sql_escape(system_prompt)
    usr_e = sql_escape(user_prompt)
    q = f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            '{MODEL}',
            [
                {{'role': 'system', 'content': '{sys_e}'}},
                {{'role': 'user', 'content': '{usr_e}'}}
            ],
            {{'temperature': {temperature}, 'max_tokens': {max_tokens}}}
        ) AS response
    """
    rows = session.sql(q).collect()
    raw = rows[0]["RESPONSE"]
    # The chat/messages form returns a JSON envelope: {"choices":[{"messages":"..."}], ...}
    try:
        obj = json.loads(raw)
        if isinstance(obj, dict) and "choices" in obj and obj["choices"]:
            return obj["choices"][0].get("messages", raw)
    except Exception:
        pass
    return raw


def cortex_search(service, query, columns, limit=3):
    """Call CORTEX.SEARCH_PREVIEW and return a compact text block of results."""
    cols_json = ", ".join(f'"{c}"' for c in columns)
    payload = f'{{"query": "{sql_escape(query)}", "columns": [{cols_json}], "limit": {limit}}}'
    q = f"""
        SELECT SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
            '{service}',
            '{sql_escape(payload)}'
        ) AS results
    """
    rows = session.sql(q).collect()
    raw = rows[0]["RESULTS"]
    try:
        obj = json.loads(raw)
        results = obj.get("results", []) if isinstance(obj, dict) else []
    except Exception:
        return ""
    lines = []
    for r in results:
        parts = [f"{c}: {r.get(c, '')}" for c in columns if r.get(c)]
        if parts:
            lines.append(" | ".join(parts))
    return "\n".join(lines)


def score_variant(score):
    """Pick a gradient class for a 0-100 score."""
    try:
        s = int(score)
    except Exception:
        s = 0
    if s >= 75:
        return "metric-num metric-num-good"
    if s >= 60:
        return "metric-num metric-num-warn"
    return "metric-num metric-num-low"


def badge_class(signal):
    return {
        "Warm": "badge-warm", "Neutral": "badge-neutral",
        "Cool": "badge-cool", "Strategic": "badge-strategic",
    }.get(str(signal).strip().title(), "badge-neutral")


# ─────────────────────────────────────────────────────────────────────────────
# DATA LOADERS  (live Snowflake queries)
# ─────────────────────────────────────────────────────────────────────────────
def load_crm_contacts():
    return session.sql(f"SELECT * FROM {DB_SCHEMA}.CRM_CONTACTS").collect()


def load_activities(org):
    q = f"""
        SELECT * FROM {DB_SCHEMA}.CRM_ACTIVITY_LOG
        WHERE ORG_NAME = '{sql_escape(org)}'
        ORDER BY ACTIVITY_DATE DESC
        LIMIT 5
    """
    return session.sql(q).collect()


def load_intel(org):
    q = f"""
        SELECT * FROM {DB_SCHEMA}.SECTOR_INTELLIGENCE
        WHERE ORG_NAME = '{sql_escape(org)}'
        ORDER BY INTEL_DATE DESC
        LIMIT 3
    """
    return session.sql(q).collect()


def load_attendees_df():
    return session.sql(f"SELECT * FROM {DB_SCHEMA}.SUMMIT_ATTENDEES").to_pandas()


def load_priorities():
    return session.sql(f"SELECT * FROM {DB_SCHEMA}.MISSION_PRIORITIES").collect()


def load_policy_docs():
    return session.sql(f"SELECT * FROM {DB_SCHEMA}.POLICY_DOCUMENTS").collect()


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
for key in ["crm_result", "priority_result", "priority_scenario",
            "alignment_result", "alignment_pair"]:
    if key not in st.session_state:
        st.session_state[key] = None


# ─────────────────────────────────────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="kicker">Snowflake AI Data Cloud — Live Demo</div>
  <h1>U.S. Embassy in Rome</h1>
  <div class="sub">Diplomatic operations intelligence powered by Cortex — stakeholder enrichment, engagement prioritization, and policy alignment.</div>
  <div class="chips">
    <span class="chip chip-accent">Cortex Complete</span>
    <span class="chip">Cortex Search</span>
    <span class="chip">Live Snowflake Data</span>
    <span class="chip">Medallion Architecture</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — Mission Context
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("##### Mission Context")
    st.markdown("""
    <div class="glass" style="padding:14px 16px;">
      <div class="sect-lbl" style="margin-top:0;">Strategic Priorities</div>
      <div class="kv" style="margin-top:6px; font-size:12.5px; line-height:1.8;">
        &bull; Critical minerals supply chain<br>
        &bull; WFP &amp; FAO accountability<br>
        &bull; AI diplomacy alignment<br>
        &bull; U.S.&ndash;Italy energy partnership
      </div>
    </div>
    <div class="glass" style="padding:14px 16px;">
      <div class="sect-lbl" style="margin-top:0;">Rome-Based International Organizations</div>
      <div class="kv" style="margin-top:6px; font-size:12.5px;">
        FAO &nbsp;&middot;&nbsp; WFP &nbsp;&middot;&nbsp; IFAD
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("All data is synthetic for demonstration purposes.")


# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "CRM Enrichment",
    "Event Prioritization",
    "Policy Alignment",
])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — CRM ENRICHMENT PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("#### Automated CRM Enrichment via Snowflake Cortex")
    st.markdown(
        "Select any CRM contact. Snowflake cross-references internal activity data, external sector intelligence, "
        "and policy context via Cortex Search — then Cortex Complete produces an enriched stakeholder profile: "
        "sector rank, relationship signal, strategic alignment score, and recommended action."
    )

    try:
        contacts = load_crm_contacts()
    except Exception as ex:
        contacts = []
        st.error(f"Failed to load CRM_CONTACTS: {ex}")

    col_left, col_right = st.columns([1, 2])

    with col_left:
        if contacts:
            company_names = [str(row_val(c, "ORG_NAME", "NAME", "ORGANIZATION", "COMPANY")) for c in contacts]
            selected = st.selectbox("Select CRM Contact", company_names, key="crm_select")
            contact = next(
                (c for c in contacts
                 if str(row_val(c, "ORG_NAME", "NAME", "ORGANIZATION", "COMPANY")) == selected),
                None,
            )

            c_type = c_country = c_hq = c_contact = c_last = ""
            if contact is not None:
                c_type = row_val(contact, "SECTOR_TYPE", "TYPE", "SECTOR")
                c_country = row_val(contact, "COUNTRY")
                c_hq = row_val(contact, "HQ", "HQ_LOCATION", "HEADQUARTERS")
                c_contact = row_val(contact, "PRIMARY_CONTACT", "CONTACT", "CONTACT_NAME")
                c_last = row_val(contact, "LAST_INTERACTION", "LAST", "LAST_CONTACT")

                st.markdown(f"""
                <div class="glass" style="margin-top:14px;">
                  <div class="glass-title">{selected}</div>
                  <div class="glass-sub">{c_type}</div>
                  <div class="kv">
                    <b>Country:</b> {c_country}<br>
                    <b>HQ:</b> {c_hq}<br>
                    <b>Contact:</b> {c_contact}<br>
                    <b>Last Interaction:</b> {c_last}
                  </div>
                  <div class="muted">Raw CRM record — unenriched</div>
                </div>
                """, unsafe_allow_html=True)

            if st.button("Enrich with Snowflake Cortex", key="enrich_btn", use_container_width=True, type="primary"):
                try:
                    with st.spinner("Querying activity log · Fetching sector intelligence · Cortex Search · Computing alignment score..."):
                        # (a) recent activities
                        activity_text = ""
                        try:
                            acts = load_activities(selected)
                            activity_text = "\n".join(
                                f"- {row_val(a, 'ACTIVITY_DATE', 'DATE')} | "
                                f"{row_val(a, 'ACTIVITY_TYPE', 'TYPE')} | "
                                f"{row_val(a, 'ACTIVITY_DETAIL', 'DETAIL', 'SUMMARY', 'NOTES')}"
                                for a in acts
                            ) or "No recent activity logged."
                        except Exception as ex:
                            activity_text = f"(activity log unavailable: {ex})"

                        # (b) sector intelligence
                        intel_text = ""
                        try:
                            intel = load_intel(selected)
                            intel_text = "\n".join(
                                f"- {row_val(i, 'INTEL_DATE', 'DATE')} | "
                                f"{row_val(i, 'INTEL_SUMMARY', 'SUMMARY', 'DETAIL')} "
                                f"(source: {row_val(i, 'SOURCE')})"
                                for i in intel
                            ) or "No sector intelligence on file."
                        except Exception as ex:
                            intel_text = f"(sector intelligence unavailable: {ex})"

                        # (c) policy context via Cortex Search
                        policy_text = ""
                        try:
                            policy_text = cortex_search(
                                POLICY_SEARCH,
                                f"{selected} {c_type} critical minerals food security policy alignment",
                                ["DOC_TITLE", "SUMMARY"],
                                limit=3,
                            ) or "No relevant policy context retrieved."
                        except Exception as ex:
                            policy_text = f"(policy search unavailable: {ex})"

                        # (d) Cortex Complete → structured enrichment
                        system_prompt = (
                            "You are a diplomatic intelligence analyst for the U.S. Embassy in Rome. "
                            "You assess private-sector and multilateral "
                            "stakeholders against U.S. strategic priorities: critical minerals supply "
                            "chain diversification away from China, WFP/FAO accountability reform, and "
                            "AI-diplomacy alignment. You are precise, sober, and action-oriented. "
                            "You output ONLY valid JSON — no prose, no markdown fences."
                        )
                        user_prompt = f"""Enrich the following stakeholder profile.

RAW CRM RECORD
Organization: {selected}
Sector/Type: {c_type}
Country: {c_country}
HQ: {c_hq}
Primary contact: {c_contact}
Last interaction: {c_last}

RECENT ACTIVITY (internal CRM_ACTIVITY_LOG)
{activity_text}

SECTOR INTELLIGENCE (SECTOR_INTELLIGENCE)
{intel_text}

RELEVANT POLICY CONTEXT (Cortex Search over policy corpus)
{policy_text}

Return a JSON object with EXACTLY these keys:
{{
  "sector_rank": "one concise sentence positioning this org within its sector and relevance to U.S. Embassy Rome priorities",
  "relationship_signal": "Warm | Neutral | Cool | Strategic",
  "alignment_score": <integer 0-100 reflecting strategic alignment with U.S. priorities>,
  "intelligence_summary": "3-4 sentence analytical summary grounded ONLY in the context above",
  "recommended_action": "one specific, concrete next step for U.S. Embassy Rome staff"
}}
Output ONLY the JSON object."""

                        response = cortex_complete(system_prompt, user_prompt, temperature=0.1)
                        enrichment = parse_llm_json(response)
                        enrichment["_org"] = selected
                        enrichment["_type"] = c_type
                        st.session_state.crm_result = enrichment
                except Exception as ex:
                    st.session_state.crm_result = None
                    st.error(f"Cortex enrichment failed: {ex}")
        else:
            st.info("No CRM contacts available.")

    with col_right:
        e = st.session_state.crm_result
        if isinstance(e, dict):
            signal = e.get("relationship_signal", "Neutral")
            score = e.get("alignment_score", 0)
            try:
                score_int = int(score)
            except Exception:
                score_int = 0
            org_name = e.get("_org", "")
            bar_pct = min(max(score_int, 0), 100)

            st.markdown(f"""
            <div class="glass">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;">
                <div>
                  <div class="glass-title" style="font-size:17px;">{org_name}</div>
                  <div style="margin-top:8px;">
                    <span class="badge {badge_class(signal)}">{signal}</span>
                    <span style="font-size:11px;color:#64748b;margin-left:6px;">Relationship Signal</span>
                  </div>
                </div>
                <div class="metric-tile" style="min-width:130px;">
                  <div class="{score_variant(score_int)}">{score_int}</div>
                  <div class="metric-lbl">Alignment Score</div>
                </div>
              </div>
              <div class="bar-track"><div class="bar-fill" style="width:{bar_pct}%;"></div></div>
              <div class="bar-caption">Strategic Alignment: {score_int}%</div>
              <div class="sect-lbl">Sector Rank</div>
              <div class="summary-text">{e.get('sector_rank', '')}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="glass">
              <div class="sect-lbl" style="margin-top:0;">Intelligence Summary</div>
              <div class="summary-text">{e.get('intelligence_summary', '')}</div>
              <div class="sect-lbl">Recommended Action</div>
              <div class="callout"><b>→</b> {e.get('recommended_action', '')}</div>
              <div class="src-note">Powered by Cortex Complete + Cortex Search &nbsp;·&nbsp; Sources: CRM_ACTIVITY_LOG · SECTOR_INTELLIGENCE · POLICY_DOCS_SEARCH</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="glass" style="text-align:center;padding:70px 24px;">
              <div style="font-size:40px;margin-bottom:14px;color:#29B5E8;text-shadow:0 0 24px rgba(41,181,232,0.5);">&#10038;</div>
              <div style="font-size:14px;color:#8ba3c0;">Select a contact and click <b style="color:#7dd3fc;">Enrich with Snowflake Cortex</b> to generate the enriched profile.</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — EVENT PRIORITIZATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("#### Ambassador Bandwidth Prioritization — Critical Minerals Summit")
    st.markdown(
        "Limited Ambassador time, a full attendee roster. Select the mission priority scenario and let "
        "Cortex match every attendee against U.S. Embassy Rome's strategic priorities — surfacing the top 8 contacts "
        "with ranked rationale and an opening line for the Ambassador."
    )

    try:
        priorities = load_priorities()
    except Exception as ex:
        priorities = []
        st.error(f"Failed to load MISSION_PRIORITIES: {ex}")

    priority_map = {}
    for p in priorities:
        name = str(row_val(p, "PRIORITY_NAME", "NAME", "SCENARIO", "PRIORITY"))
        desc = str(row_val(p, "DESCRIPTION", "DESC", "DETAIL"))
        if name:
            priority_map[name] = desc

    col_a, col_b = st.columns([1, 3])

    with col_a:
        if priority_map:
            scenario = st.radio(
                "Mission Priority Scenario",
                list(priority_map.keys()),
                key="scenario_radio",
            )
            st.markdown(
                f'<div class="glass" style="padding:12px 14px;"><div style="font-size:11.5px;color:#8ba3c0;line-height:1.6;">{priority_map.get(scenario, "")}</div></div>',
                unsafe_allow_html=True,
            )

            if st.button("Prioritize Ambassador Bandwidth", key="priority_btn", use_container_width=True, type="primary"):
                try:
                    with st.spinner("Matching attendees against mission priorities via Cortex..."):
                        # (a) full roster
                        att_df = load_attendees_df()
                        roster_lines = []
                        for _, r in att_df.iterrows():
                            d = {str(k).upper(): v for k, v in r.to_dict().items()}
                            roster_lines.append(
                                f"- {d.get('NAME', '')} | {d.get('ORGANIZATION', '')} | "
                                f"{d.get('COUNTRY', '')} | {d.get('TITLE', '')} | {d.get('SECTOR', '')}"
                            )
                        roster_text = "\n".join(roster_lines)

                        # (b) selected priority record
                        scenario_desc = priority_map.get(scenario, "")

                        # (c) relevant context via Cortex Search
                        context_text = ""
                        try:
                            context_text = cortex_search(
                                POLICY_SEARCH,
                                f"{scenario} {scenario_desc}",
                                ["DOC_TITLE", "SUMMARY"],
                                limit=3,
                            ) or ""
                        except Exception:
                            context_text = ""

                        # (d) Cortex Complete → ranked top-8 + deprioritized note
                        system_prompt = (
                            "You are a strategic scheduling analyst for the U.S. Embassy in Rome. "
                            "You match summit attendees against a stated mission priority "
                            "and rank the highest-value engagements for the Ambassador. You are decisive and "
                            "diplomatic. You output ONLY valid JSON — no prose, no markdown fences."
                        )
                        user_prompt = f"""Prioritize the Ambassador's limited time at the Critical Minerals Summit (Rome 2026).

MISSION PRIORITY SCENARIO
Name: {scenario}
Description: {scenario_desc}

RELEVANT POLICY CONTEXT (Cortex Search)
{context_text or "(none)"}

FULL ATTENDEE ROSTER
{roster_text}

Rank the TOP 8 attendees for this scenario. Return a JSON object with EXACTLY these keys:
{{
  "ranked": [
    {{
      "rank": 1,
      "name": "attendee name",
      "org": "organization (country)",
      "score": <integer 0-100 fit against the scenario>,
      "rationale": "1-2 sentences on why this attendee is high priority for THIS scenario",
      "opening_line": "a natural, diplomatic opening line the Ambassador could use"
    }}
  ],
  "deprioritized_note": "one sentence on how the remaining attendees are routed, plus any attendee that requires special clearance"
}}
The "ranked" array MUST contain exactly 8 objects ordered by rank 1-8. Output ONLY the JSON object."""

                        response = cortex_complete(system_prompt, user_prompt, temperature=0.1)
                        result = parse_llm_json(response)
                        st.session_state.priority_result = result
                        st.session_state.priority_scenario = scenario
                except Exception as ex:
                    st.session_state.priority_result = None
                    st.error(f"Cortex prioritization failed: {ex}")

            st.markdown(
                '<span class="chip chip-accent" style="margin-top:6px;">Cortex Complete + Live Data</span>',
                unsafe_allow_html=True,
            )
        else:
            st.info("No mission priorities available.")

    with col_b:
        st.markdown('<div class="sect-lbl">Full Attendee Roster — Critical Minerals Summit · Rome 2026</div>', unsafe_allow_html=True)
        try:
            att_df_display = load_attendees_df()
            st.dataframe(att_df_display, height=240, use_container_width=True)
        except Exception as ex:
            st.error(f"Failed to load SUMMIT_ATTENDEES: {ex}")

    result = st.session_state.priority_result
    if isinstance(result, dict) and result.get("ranked"):
        active_scenario = st.session_state.priority_scenario or ""
        st.markdown(f"""
        <div style="margin-top:18px;">
          <div class="sect-lbl" style="margin-bottom:2px;">Ambassador Priority List</div>
          <div class="glass-title" style="font-size:16px;">{active_scenario}</div>
        </div>
        """, unsafe_allow_html=True)

        top8 = result.get("ranked", [])[:8]
        p_col1, p_col2 = st.columns(2)

        for i, p in enumerate(top8):
            col = p_col1 if i % 2 == 0 else p_col2
            try:
                p_score = int(p.get("score", 0))
            except Exception:
                p_score = 0
            bar_pct = min(max(p_score, 0), 100)
            with col:
                st.markdown(f"""
                <div class="prio-card">
                  <div class="prio-rank">{p.get('rank', i + 1)}</div>
                  <div class="prio-name">{p.get('name', '')}</div>
                  <div class="prio-org">{p.get('org', '')}</div>
                  <div class="bar-track" style="margin-top:4px;"><div class="bar-fill" style="width:{bar_pct}%;"></div></div>
                  <div class="bar-caption" style="margin-bottom:6px;">Priority Score: {p_score}</div>
                  <div class="prio-rat">{p.get('rationale', '')}</div>
                  <div class="prio-open">&#8220;{p.get('opening_line', '')}&#8221;</div>
                </div>
                """, unsafe_allow_html=True)

        depri = result.get("deprioritized_note", "")
        if depri:
            st.markdown(
                f'<div class="route-note"><b>Staff Routing:</b> {depri}</div>',
                unsafe_allow_html=True,
            )


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — POLICY ALIGNMENT ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("#### Cross-Document Policy Alignment Analysis")
    st.markdown(
        "Select an internal administration document alongside an external policy document. "
        "Cortex Complete cross-references both full texts, scores alignment, identifies points of agreement "
        "and tension, and generates a recommended diplomatic approach with Ambassador talking points."
    )

    try:
        docs = load_policy_docs()
    except Exception as ex:
        docs = []
        st.error(f"Failed to load POLICY_DOCUMENTS: {ex}")

    # Split by classification: internal/administration vs external/partner
    internal_docs, external_docs = {}, {}
    for d in docs:
        title = str(row_val(d, "DOC_TITLE", "TITLE", "NAME"))
        classification = str(row_val(d, "CLASSIFICATION", "CLASS", "CATEGORY")).upper()
        entry = {
            "title": title,
            "type": row_val(d, "DOC_TYPE", "TYPE"),
            "date": row_val(d, "DOC_DATE", "DATE"),
            "issuer": row_val(d, "ISSUER", "SOURCE"),
            "summary": row_val(d, "SUMMARY", "PREVIEW", "ABSTRACT"),
            "full_text": row_val(d, "FULL_TEXT", "TEXT", "BODY", "CONTENT"),
        }
        if "INTERN" in classification or "ADMIN" in classification:
            internal_docs[title] = entry
        elif "EXTERN" in classification or "PARTNER" in classification:
            external_docs[title] = entry
        else:
            # Unclassified: make available on both sides so the demo still works
            internal_docs.setdefault(title, entry)
            external_docs.setdefault(title, entry)

    c1, c_mid, c2 = st.columns([5, 1, 5])

    internal_sel = external_sel = None
    idoc = edoc = None

    with c1:
        if internal_docs:
            internal_sel = st.selectbox("Internal Document", list(internal_docs.keys()), key="int_sel", label_visibility="collapsed")
            idoc = internal_docs[internal_sel]
            st.markdown(f"""
            <div class="doc-card" style="margin-top:6px;">
              <div class="doc-kicker">Internal / Administration</div>
              <div class="doc-title">{internal_sel}</div>
              <div class="doc-meta">{idoc['type']} &nbsp;&middot;&nbsp; {idoc['date']} &nbsp;&middot;&nbsp; Issuer: {idoc['issuer']}</div>
              <div class="doc-prev">{idoc['summary']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No internal documents available.")

    with c_mid:
        st.markdown(
            '<div style="text-align:center;font-size:20px;font-weight:800;color:#29B5E8;padding-top:26px;'
            'text-shadow:0 0 18px rgba(41,181,232,0.5);">vs</div>',
            unsafe_allow_html=True,
        )

    with c2:
        if external_docs:
            external_sel = st.selectbox("External Document", list(external_docs.keys()), key="ext_sel", label_visibility="collapsed")
            edoc = external_docs[external_sel]
            st.markdown(f"""
            <div class="doc-card" style="margin-top:6px;">
              <div class="doc-kicker">External / Partner</div>
              <div class="doc-title">{external_sel}</div>
              <div class="doc-meta">{edoc['type']} &nbsp;&middot;&nbsp; {edoc['date']} &nbsp;&middot;&nbsp; Issuer: {edoc['issuer']}</div>
              <div class="doc-prev">{edoc['summary']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No external documents available.")

    st.markdown("<div style='margin-top:18px;'></div>", unsafe_allow_html=True)
    btn_col, _ = st.columns([2, 5])
    with btn_col:
        analyze_clicked = st.button(
            "Analyze Alignment",
            key="align_btn",
            use_container_width=True,
            type="primary",
            disabled=not (idoc and edoc),
        )

    if analyze_clicked and idoc and edoc:
        try:
            with st.spinner("Running cross-document analysis via Cortex Complete · Scoring alignment · Generating diplomatic guidance..."):
                internal_text = idoc.get("full_text") or idoc.get("summary") or ""
                external_text = edoc.get("full_text") or edoc.get("summary") or ""

                system_prompt = (
                    "You are a senior policy alignment analyst for the U.S. Embassy in Rome. "
                    "You compare a U.S./administration policy document against an "
                    "external or partner policy document, quantify alignment, and produce diplomatic "
                    "guidance the Ambassador can act on. You are candid about genuine tensions rather "
                    "than papering over them. You output ONLY valid JSON — no prose, no markdown fences."
                )
                user_prompt = f"""Compare these two policy documents and assess their alignment.

INTERNAL / ADMINISTRATION DOCUMENT
Title: {internal_sel}
Type: {idoc['type']} · {idoc['date']} · Issuer: {idoc['issuer']}
Full text:
{internal_text}

EXTERNAL / PARTNER DOCUMENT
Title: {external_sel}
Type: {edoc['type']} · {edoc['date']} · Issuer: {edoc['issuer']}
Full text:
{external_text}

Return a JSON object with EXACTLY these keys:
{{
  "alignment_score": <integer 0-100>,
  "label": "a short verdict, e.g. 'Strong Alignment — Natural Partnership Opportunity'",
  "agreements": ["3-4 concrete points of genuine agreement"],
  "tensions": ["2-3 concrete points of genuine tension or divergence"],
  "diplomatic_approach": "one paragraph of recommended diplomatic strategy for U.S. Embassy Rome",
  "talking_points": ["3 quotable talking points the Ambassador could deliver"]
}}
Base every claim ONLY on the document texts provided. Output ONLY the JSON object."""

                response = cortex_complete(system_prompt, user_prompt, temperature=0.1)
                analysis = parse_llm_json(response)
                analysis["_pair"] = (internal_sel, external_sel)
                st.session_state.alignment_result = analysis
        except Exception as ex:
            st.session_state.alignment_result = None
            st.error(f"Cortex alignment analysis failed: {ex}")

    r = st.session_state.alignment_result
    if isinstance(r, dict) and "alignment_score" in r:
        try:
            a_score = int(r.get("alignment_score", 0))
        except Exception:
            a_score = 0
        bar_pct = min(max(a_score, 0), 100)

        score_col, details_col = st.columns([1, 3])

        with score_col:
            st.markdown(f"""
            <div class="gauge-wrap">
              <div class="gauge-num {score_variant(a_score)}" style="font-size:56px;">{a_score}%</div>
              <div class="bar-track" style="margin-top:14px;"><div class="bar-fill" style="width:{bar_pct}%;"></div></div>
              <div class="gauge-lbl">{r.get('label', '')}</div>
              <div class="src-note" style="margin-top:14px;">Cortex Complete</div>
            </div>
            """, unsafe_allow_html=True)

        with details_col:
            st.markdown('<div class="sect-lbl">Points of Agreement</div>', unsafe_allow_html=True)
            agreements = r.get("agreements", [])
            if agreements:
                st.markdown(
                    "\n".join(f'<div class="agree-item"><span class="mark">✓</span><span>{a}</span></div>' for a in agreements),
                    unsafe_allow_html=True,
                )
            else:
                st.caption("None identified.")

            st.markdown('<div class="sect-lbl">Points of Tension</div>', unsafe_allow_html=True)
            tensions = r.get("tensions", [])
            if tensions:
                st.markdown(
                    "\n".join(f'<div class="tension-item"><span class="mark">⚠</span><span>{t}</span></div>' for t in tensions),
                    unsafe_allow_html=True,
                )
            else:
                st.caption("None identified.")

            st.markdown('<div class="sect-lbl">Recommended Diplomatic Approach</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="approach-box">{r.get("diplomatic_approach", "")}</div>', unsafe_allow_html=True)

            st.markdown('<div class="sect-lbl">Suggested Ambassador Talking Points</div>', unsafe_allow_html=True)
            talking_points = r.get("talking_points", [])
            if talking_points:
                for tp in talking_points:
                    st.markdown(f'<div class="tp-box">&#8220;{tp}&#8221;</div>', unsafe_allow_html=True)
            else:
                st.caption("None generated.")
