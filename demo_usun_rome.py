# demo_usun_rome.py
# ─────────────────────────────────────────────────────────────────────────────
# USUN Rome | Snowflake AI Data Cloud Demo
# Demo: USUN Rome
# Use Cases: CRM Enrichment → Event Prioritization → Policy Alignment
#
# Run locally:  streamlit run demo_usun_rome.py
# Deploy SiS:   update snowflake.yml then: snow streamlit deploy
# ─────────────────────────────────────────────────────────────────────────────

import streamlit as st
import time
import pandas as pd

st.set_page_config(
    page_title="USUN Rome — Snowflake AI Demo",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Page background */
.stApp { background-color: #0f172a; }
section[data-testid="stSidebar"] { background-color: #0a1628 !important; }

/* Demo header */
.demo-header {
    background: linear-gradient(135deg, #0a1628 0%, #0f2040 100%);
    border-bottom: 3px solid #29B5E8;
    padding: 20px 28px 16px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.demo-header h1 { color: #fff !important; font-size: 21px !important; font-weight: 700 !important; margin: 0 0 4px 0 !important; }
.demo-header .sub { color: #94a3b8; font-size: 13px; }
.demo-header .badges { margin-top: 12px; display: flex; gap: 8px; flex-wrap: wrap; }
.hbadge {
    display: inline-block; padding: 3px 11px; border-radius: 12px;
    font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;
}
.hbadge-blue   { background: #1a3a5c; color: #60a5fa; border: 1px solid #2563eb; }
.hbadge-amber  { background: #451a03; color: #fcd34d; border: 1px solid #d97706; }
.hbadge-purple { background: #2a1f45; color: #c4b5fd; border: 1px solid #7c3aed; }
.hbadge-green  { background: #14532d; color: #86efac; border: 1px solid #16a34a; }

/* Info cards */
.sf-card {
    background: #1e293b; border: 1px solid #334155; border-radius: 10px;
    padding: 16px 20px; margin-bottom: 12px;
}
.sf-card-title { font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 4px; }
.sf-card-sub   { font-size: 12px; color: #94a3b8; }

/* Relationship signal badges */
.sig { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }
.sig-warm     { background: #14532d; color: #86efac; border: 1px solid #16a34a; }
.sig-neutral  { background: #1e3a5f; color: #7dd3fc; border: 1px solid #0369a1; }
.sig-cool     { background: #1e1b2e; color: #a78bfa; border: 1px solid #7c3aed; }
.sig-strategic{ background: #451a03; color: #fcd34d; border: 1px solid #d97706; }

/* Cortex feature badge */
.cortex-badge {
    display: inline-flex; align-items: center; gap: 5px;
    background: #0c2a3f; border: 1px solid #0369a1; color: #7dd3fc;
    padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600;
}

/* Enrichment card */
.enrich-card {
    background: #1e293b; border: 1px solid #334155; border-left: 4px solid #29B5E8;
    border-radius: 0 10px 10px 0; padding: 18px 20px; margin-top: 8px;
}
.enrich-rank  { font-size: 12px; color: #7dd3fc; margin-bottom: 10px; }
.enrich-summary { font-size: 13px; color: #cbd5e1; line-height: 1.7; margin: 10px 0; }
.enrich-action {
    background: #0f172a; border-left: 3px solid #29B5E8;
    padding: 10px 14px; font-size: 13px; color: #e2e8f0;
    border-radius: 0 6px 6px 0; margin-top: 12px;
}
.enrich-action strong { color: #29B5E8; }
.data-sources { font-size: 11px; color: #475569; margin-top: 8px; }

/* Priority cards */
.priority-card {
    background: #1e293b; border: 1px solid #334155; border-left: 4px solid #29B5E8;
    border-radius: 0 10px 10px 0; padding: 14px 16px; margin-bottom: 10px;
}
.p-rank  { font-size: 26px; font-weight: 800; color: #29B5E8; float: left; margin-right: 12px; line-height: 1; }
.p-name  { font-size: 14px; font-weight: 700; color: #f1f5f9; }
.p-org   { font-size: 12px; color: #94a3b8; margin-bottom: 6px; }
.p-rat   { font-size: 12px; color: #cbd5e1; margin: 8px 0; clear: both; }
.p-open  {
    background: #0f172a; border-left: 3px solid #29B5E8;
    padding: 8px 12px; font-size: 12px; color: #7dd3fc; font-style: italic;
    border-radius: 0 6px 6px 0;
}
.deprior {
    background: #1e293b; border: 1px solid #334155; border-radius: 8px;
    padding: 12px 16px; margin-top: 12px; font-size: 12px; color: #94a3b8;
}

/* Policy alignment */
.doc-card {
    background: #1e293b; border: 1px solid #334155; border-radius: 10px;
    padding: 14px 16px; height: 140px; overflow: hidden;
}
.doc-type  { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: #64748b; margin-bottom: 4px; }
.doc-title { font-size: 13px; font-weight: 700; color: #f1f5f9; margin-bottom: 4px; }
.doc-issuer { font-size: 11px; color: #94a3b8; margin-bottom: 8px; }
.doc-preview { font-size: 11px; color: #64748b; line-height: 1.5; overflow: hidden; }

.align-score-box {
    text-align: center; padding: 20px; background: #1e293b;
    border: 1px solid #334155; border-radius: 10px; margin-bottom: 16px;
}
.align-score-num { font-size: 52px; font-weight: 800; line-height: 1; }
.align-score-lbl { font-size: 12px; color: #94a3b8; margin-top: 4px; }

.section-lbl {
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.08em; color: #64748b; margin: 16px 0 8px 0;
}
.agree-item { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 8px; font-size: 13px; color: #86efac; line-height: 1.5; }
.tension-item { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 8px; font-size: 13px; color: #fca5a5; line-height: 1.5; }
.approach-box {
    background: #0f2040; border: 1px solid #1e3a5f; border-radius: 8px;
    padding: 14px 16px; font-size: 13px; color: #bfdbfe; line-height: 1.7;
}
.tp-box {
    background: #1e293b; border: 1px solid #334155; border-left: 3px solid #7dd3fc;
    border-radius: 0 8px 8px 0; padding: 10px 14px; margin-bottom: 8px;
    font-size: 13px; color: #e2e8f0; font-style: italic; line-height: 1.6;
}

/* Sidebar */
.sb-header { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #475569; margin-bottom: 8px; }
.sb-item { font-size: 12px; color: #cbd5e1; margin-bottom: 6px; padding: 6px 10px; background: #1e293b; border-radius: 6px; border-left: 3px solid #29B5E8; }
.sb-item-dim { font-size: 12px; color: #475569; margin-bottom: 6px; padding: 6px 10px; background: #1e293b; border-radius: 6px; border-left: 3px solid #334155; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════
#  DATA LAYER — Synthetic demo content scripted for USUN Rome context
# ════════════════════════════════════════════════════════════════════════════
# ─────────────────────────────────────────────────────────────────────────────

CRM_CONTACTS = [
    {"name": "Enel Green Power",               "type": "Energy / Critical Minerals",        "country": "Italy",       "hq": "Rome",        "last": "Aug 2026", "contact": "Maria Rossi, VP Government Affairs"},
    {"name": "ENI S.p.A.",                      "type": "Oil & Gas / Critical Minerals",     "country": "Italy",       "hq": "Rome",        "last": "Jun 2026", "contact": "Roberto Ferretti, EU Affairs Director"},
    {"name": "APSA (Vatican Investments)",       "type": "Finance / Ethics",                  "country": "Vatican City","hq": "Vatican",     "last": "Jul 2026", "contact": "Msgr. Pietro Conti, Secretary"},
    {"name": "Vulcan Energy Resources",          "type": "Lithium Processing",                "country": "Germany",     "hq": "Frankfurt",   "last": "Aug 2026", "contact": "Dr. Marco Van der Berg, CTO"},
    {"name": "Albemarle Corporation",            "type": "Lithium / Bromine",                 "country": "USA",         "hq": "Charlotte, NC","last": "Jul 2026", "contact": "Thomas Whitmore, VP Gov. Affairs"},
    {"name": "Yara International",               "type": "Fertilizers / Food Security",       "country": "Norway",      "hq": "Oslo",        "last": "May 2026", "contact": "Helena Svensson, Int'l Relations"},
    {"name": "Cargill International (Rome)",     "type": "Agriculture / Food Security",       "country": "USA",         "hq": "Rome (EMEA)", "last": "Aug 2026", "contact": "James O'Connor, Regional Director"},
    {"name": "OCP Group",                        "type": "Critical Minerals / Phosphates",    "country": "Morocco",     "hq": "Casablanca",  "last": "Mar 2026", "contact": "Hamid Benali, VP International"},
    {"name": "Barrick Gold (Italy)",             "type": "Mining",                            "country": "Canada",      "hq": "Toronto",     "last": "Jan 2026", "contact": "Lucia Fernandez, EU Affairs"},
    {"name": "Breakthrough Energy Europe",       "type": "Clean Energy / Minerals",           "country": "Belgium",     "hq": "Brussels",    "last": "Jun 2026", "contact": "Sophie Laurent, Managing Director"},
    {"name": "FAO Private Sector Advisory Group","type": "Food Security / Multi-stakeholder", "country": "Italy",       "hq": "Rome (FAO)",  "last": "Aug 2026", "contact": "Prof. Anna Kessler, Chair"},
    {"name": "World Resources Institute Rome",   "type": "Environmental Policy",              "country": "USA / Italy", "hq": "Rome",        "last": "Jul 2026", "contact": "Dr. Maria Gonzalez, Director"},
]

CRM_ENRICHMENT = {
    "Enel Green Power": {
        "rank": "#1 renewable energy company in Italy · Top 3 European operator with active critical minerals integration strategy",
        "signal": "Warm", "score": 87,
        "summary": "Enel signed the Critical Minerals Ministerial declaration (Feb 2026) and publicly endorsed U.S.-led supply chain transparency initiatives. CEO engagement with U.S. officials at COP30 signals strong bilateral interest. Enel X subsidiary has active downstream lithium and cobalt supply chain investments across Chile and Argentina.",
        "action": "Schedule Principal-level engagement before the September summit. Enel's Ministerial commitment makes them a natural anchor for a U.S.-Italy minerals partnership narrative — coordinate with DOE attaché on supply chain agreement framing.",
        "feature": "Cortex Complete + Cortex Search",
        "sources": "CRM activity log · Ministerial participant list · DOE loan database · LinkedIn graph",
    },
    "ENI S.p.A.": {
        "rank": "Italy's largest energy company · Emerging critical minerals position through Chile lithium and Morocco phosphate JVs",
        "signal": "Neutral", "score": 62,
        "summary": "ENI has active lithium exploration licenses in Chile and a 2025 joint venture with OCP Morocco for phosphate processing. ENI's CEO attended the Critical Minerals Ministerial as part of Italy's official delegation but has not publicly committed to U.S. supply chain frameworks. Observing closely.",
        "action": "Introduce ENI to the critical minerals supply chain framework through the Ministerial follow-on working group. Their Morocco JV is a natural entry point for U.S. supply chain resilience goals — flag to Econ Officer.",
        "feature": "Cortex Complete + Snowflake Data Sharing",
        "sources": "CRM activity log · SEC filings · Trade press monitoring · Ministerial participant list",
    },
    "APSA (Vatican Investments)": {
        "rank": "Manages €5B+ Vatican patrimony · Growing influence on ethical AI and sustainable investment governance globally",
        "signal": "Strategic", "score": 74,
        "summary": "APSA divested from several AI companies in Q3 2024 citing misalignment with Catholic Social Teaching. The Vatican's Dicastery for Culture and Education is co-authoring a multilateral AI governance framework now cited in EU AI Act commentary. Cardinal Fitzgerald maintains close contact with the U.S. Embassy to the Holy See.",
        "action": "HIGH PRIORITY: The Vatican's AI ethics position directly intersects with the administration's AI EO narrative. Brief the Ambassador before any Vatican-side engagement — alignment is substantive but framing matters critically.",
        "feature": "Cortex Complete + Document AI",
        "sources": "CRM activity log · Vatican press office · Holy See Embassy cables · Rome Call signatories list",
    },
    "Vulcan Energy Resources": {
        "rank": "Europe's leading zero-carbon lithium developer · Flagship of EU Critical Raw Materials Act implementation pipeline",
        "signal": "Warm", "score": 83,
        "summary": "Vulcan produces lithium via geothermal brine extraction in Germany — a process aligned with U.S. environmental criteria for supply chain certification. The company briefed State Dept Econ Bureau on European lithium capacity in Q1 2026. USUN Rome introduction established March 2026 through German Embassy.",
        "action": "Connect Vulcan to the U.S. Battery Materials Network. Their zero-carbon process technology is a strong asset for U.S.-EU critical minerals partnership narrative — particularly with Italian and German government audiences.",
        "feature": "Cortex Complete + Cortex Search",
        "sources": "CRM activity log · DOE supply chain criteria database · Company investor relations · EU CRMA registry",
    },
    "Albemarle Corporation": {
        "rank": "#1 global lithium producer · U.S. critical minerals champion with $1.26B DOE conditional commitment (Feb 2026)",
        "signal": "Warm", "score": 91,
        "summary": "Albemarle received a $1.26B conditional DOE commitment announced at the Critical Minerals Ministerial in February 2026 — a direct U.S. government success story. European operations based in the Netherlands with active engagement across Italian industrial partners. Government affairs team has been a consistent interlocutor with State Dept.",
        "action": "Leverage as the flagship U.S. critical minerals success story in Ambassador engagements. Albemarle's DOE deal is a concrete, quotable win — coordinate talking points with DOE attaché before any Italian ministerial engagement.",
        "feature": "Cortex Complete + Snowflake Data Sharing",
        "sources": "CRM activity log · DOE loan announcement · Company investor relations · Ministerial outcomes report",
    },
    "Yara International": {
        "rank": "World's largest fertilizer company · Critical WFP and FAO partner in food security programming across 150+ countries",
        "signal": "Warm", "score": 79,
        "summary": "Yara operates through a partnership with WFP under the School Meals Coalition and is a key FAO private sector partner on food security. The company has expressed concern about U.S. foreign assistance reviews impacting WFP programs but is open to constructive dialogue. Rome office maintains regular contact with WFP liaison.",
        "action": "Engage Yara on FAO accountability reform through a shared efficiency-for-impact framing. Their private sector perspective on WFP programming effectiveness is valuable — position USUN Rome as an ally for evidence-based reform, not a budget axe.",
        "feature": "Cortex Complete + Cortex Search",
        "sources": "CRM activity log · WFP partnership database · FAO private sector registry · Media monitoring",
    },
    "Cargill International (Rome)": {
        "rank": "World's largest agricultural commodity trader · Major WFP and FAO procurement contract partner",
        "signal": "Strategic", "score": 81,
        "summary": "Cargill's Rome office coordinates their engagement with FAO and WFP procurement — they have direct, operational insight into program efficiency. As a U.S.-headquartered company, they are naturally aligned with America First trade and food security priorities. Positive response to U.S. accountability agenda in recent bilateral.",
        "action": "Cargill is a natural ally for USUN Rome's WFP accountability push. Their procurement relationship provides direct insight into WFP operational efficiency — request a confidential briefing before the Executive Board review.",
        "feature": "Cortex Complete + Document AI",
        "sources": "CRM activity log · WFP procurement disclosures · FAO private sector registry · USAID contractor database",
    },
    "OCP Group": {
        "rank": "World's largest phosphate exporter (70% of global reserves) · Critical input for fertilizer and food security supply chains",
        "signal": "Neutral", "score": 68,
        "summary": "OCP controls 70% of global phosphate reserves — a critical input for fertilizers that directly affects food security globally. Morocco was represented at the Feb 2026 Critical Minerals Ministerial as a key U.S. partner. OCP's JV with ENI on phosphate processing creates a natural bridge to Italian energy sector engagement.",
        "action": "RELATIONSHIP GAP: No direct USUN Rome engagement established. OCP is strategically important for both critical minerals and food security mandates. Introduce through Moroccan Embassy contact — flag to both Minerals and Food Security desks.",
        "feature": "Cortex Complete + Cortex Search",
        "sources": "CRM activity log · Trade databases · Ministerial participant list · FAO phosphate supply data",
    },
    "Barrick Gold (Italy)": {
        "rank": "Top 5 global gold miner · Emerging position in copper and cobalt as EV demand drives minerals diversification",
        "signal": "Cool", "score": 51,
        "summary": "Barrick has limited Italian operations but maintains a Rome office for EU regulatory engagement. Their copper and cobalt strategy is tangentially relevant to the critical minerals agenda. Relationship exists primarily through Canadian Embassy channels — no direct USUN Rome engagement in the past 12 months.",
        "action": "LOW PRIORITY for near-term Ambassador time. Monitor for copper/cobalt supply chain opportunities. Route engagement through the bilateral Canada-U.S. minerals framework — flag to Canadian Embassy counterpart.",
        "feature": "Cortex Complete",
        "sources": "CRM activity log · Annual report · Canadian Embassy contact notes",
    },
    "Breakthrough Energy Europe": {
        "rank": "Bill Gates-backed clean energy investment fund · European hub for critical minerals processing innovation financing",
        "signal": "Warm", "score": 77,
        "summary": "Breakthrough Energy Europe funds critical minerals processing innovation across EU member states — strong alignment with U.S. clean energy supply chain goals. Policy team participated in Critical Minerals Ministerial side events (Feb 2026). Introduction came directly from State Dept Washington, establishing a warm channel.",
        "action": "Invite to bilateral U.S.-EU clean energy working group. Breakthrough Energy's grant-making can accelerate adoption of U.S.-aligned minerals processing standards in Europe — particularly in Italy and Germany.",
        "feature": "Cortex Complete + Snowflake Data Sharing",
        "sources": "CRM activity log · Portfolio database · State Dept introduction memo · Ministerial side-event participants",
    },
    "FAO Private Sector Advisory Group": {
        "rank": "Formal advisory body to FAO Director-General · Gateway to all FAO private sector engagement and governance influence",
        "signal": "Strategic", "score": 72,
        "summary": "The PSAG provides formal private sector input to FAO governance — a lever for influencing FAO reform from within. Several PSAG member companies are U.S.-aligned. USUN Rome has two PSAG contacts through FAO Governing Bodies engagement. Current PSAG chair is European-aligned — mixed signals on reform posture.",
        "action": "Work through friendly PSAG members to introduce America First food security accountability principles into FAO's private sector consultation framework. Identify PSAG members who can be activated for the Executive Board reform discussion.",
        "feature": "Cortex Complete + Cortex Search",
        "sources": "CRM activity log · FAO PSAG membership list · Governing Bodies meeting minutes · Media monitoring",
    },
    "World Resources Institute Rome": {
        "rank": "Leading global environmental think tank · FAO and IFAD policy partner on food systems and sustainable agriculture",
        "signal": "Warm", "score": 75,
        "summary": "WRI's Rome office maintains strong relationships with FAO and IFAD technical teams. As a U.S.-headquartered organization, WRI is naturally aligned with U.S. policy interests while maintaining multilateral credibility. Their Food and Land Use Coalition work is cited in FAO reform discussions.",
        "action": "Leverage WRI as a multilateral-facing channel for U.S. food systems positions. Their FAO relationships provide useful intelligence on reform sentiment among developing-country members — schedule quarterly intel exchange.",
        "feature": "Cortex Complete + Document AI",
        "sources": "CRM activity log · WRI publication database · FAO citation analysis · IFAD partner registry",
    },
}

# ── Tab 2: Summit Attendees ────────────────────────────────────────────────

SUMMIT_ATTENDEES = [
    {"Name": "Alessandro Corsi",        "Organization": "Enel Green Power",                  "Country": "Italy",       "Title": "CEO",                             "Sector": "Critical Minerals / Energy"},
    {"Name": "Dr. Sarah Chen",           "Organization": "U.S. Dept of Energy",               "Country": "USA",         "Title": "Dep. Asst. Secretary, Minerals",  "Sector": "Critical Minerals"},
    {"Name": "Dr. Marco Van der Berg",   "Organization": "Vulcan Energy Resources",            "Country": "Germany",     "Title": "Chief Technology Officer",        "Sector": "Lithium Processing"},
    {"Name": "Thomas Whitmore",          "Organization": "Albemarle Corporation",              "Country": "USA",         "Title": "VP Government Affairs",           "Sector": "Lithium Supply Chain"},
    {"Name": "Kenji Tanaka",             "Organization": "Japan Critical Minerals Agency",     "Country": "Japan",       "Title": "Director General",                "Sector": "Critical Minerals"},
    {"Name": "Fatima Al-Rashid",         "Organization": "WFP Rome Liaison",                   "Country": "UN / Italy",  "Title": "Executive Director, Rome Office", "Sector": "Food Security"},
    {"Name": "Dr. Emmanuel Osei",        "Organization": "FAO",                                "Country": "UN / Italy",  "Title": "Deputy Director-General",         "Sector": "Food Security / Agriculture"},
    {"Name": "Helena Svensson",          "Organization": "Yara International",                 "Country": "Norway",      "Title": "Director, International Relations","Sector": "Fertilizers / Food Security"},
    {"Name": "Miguel Fernandez",         "Organization": "Brazilian Ministry of Agriculture",  "Country": "Brazil",      "Title": "Special Agricultural Attaché",    "Sector": "Agriculture / Food Security"},
    {"Name": "Dr. Amara Diallo",         "Organization": "IFAD",                               "Country": "UN / Italy",  "Title": "Director, West Africa Program",   "Sector": "Food Security / Development"},
    {"Name": "Dr. Isabella Moretti",     "Organization": "Italian Ministry of MASE",           "Country": "Italy",       "Title": "Director, Critical Materials",    "Sector": "Critical Minerals"},
    {"Name": "Pierre Dubois",            "Organization": "European Commission",                "Country": "EU / Belgium","Title": "Commissioner, Critical Raw Materials","Sector": "Critical Minerals"},
    {"Name": "Anna Kowalski",            "Organization": "Polish Ministry of Mining",          "Country": "Poland",      "Title": "Deputy Minister",                 "Sector": "Critical Minerals"},
    {"Name": "Björn Eriksson",           "Organization": "Swedish Ministry of Trade",          "Country": "Sweden",      "Title": "Critical Minerals Attaché",       "Sector": "Critical Minerals"},
    {"Name": "Hamid Benali",             "Organization": "OCP Group",                          "Country": "Morocco",     "Title": "VP International Affairs",        "Sector": "Critical Minerals / Phosphates"},
    {"Name": "Lucia Fernandez",          "Organization": "Barrick Gold",                       "Country": "Canada",      "Title": "Director, EU Government Affairs", "Sector": "Mining"},
    {"Name": "Dr. James Achebe",         "Organization": "African Minerals Dev. Centre",       "Country": "DRC",         "Title": "Executive Chairman",              "Sector": "Critical Minerals / Africa"},
    {"Name": "Pham Thi Lan",             "Organization": "Vietnamese Ministry of Resources",   "Country": "Vietnam",     "Title": "Deputy Minister",                 "Sector": "Critical Minerals"},
    {"Name": "Carlos Matos",             "Organization": "Lithium Americas (Chile JV)",        "Country": "Chile",       "Title": "CEO, Americas Operations",        "Sector": "Lithium"},
    {"Name": "Sophie Laurent",           "Organization": "Breakthrough Energy Europe",         "Country": "Belgium",     "Title": "Managing Director",               "Sector": "Clean Energy / Minerals"},
    {"Name": "David Kim",                "Organization": "IFC Critical Minerals Fund",         "Country": "South Korea", "Title": "Partner",                         "Sector": "Finance / Development"},
    {"Name": "Margaret O'Brien",         "Organization": "European Investment Bank",           "Country": "EU / Ireland","Title": "Director, Climate Investment",    "Sector": "Finance / Energy"},
    {"Name": "Prof. Roberto Ricci",      "Organization": "Mediterranean Energy Policy Institute","Country": "Italy",     "Title": "Director General",                "Sector": "Policy / Research"},
    {"Name": "Dr. Layla Hassan",         "Organization": "CSIS Critical Minerals Program",     "Country": "USA",         "Title": "Senior Fellow",                   "Sector": "Policy / Research"},
    {"Name": "Ambassador Chen Wei",      "Organization": "Chinese Mission, UN Rome",           "Country": "China",       "Title": "Chargé d'Affaires",               "Sector": "Diplomacy"},
    {"Name": "H.E. Beatriz Santos",      "Organization": "Portuguese Government",              "Country": "Portugal",    "Title": "Special Envoy, Critical Minerals", "Sector": "Critical Minerals / Diplomacy"},
    {"Name": "Dr. Stavros Papadopoulos","Organization": "Greek Ministry of Energy",           "Country": "Greece",      "Title": "Deputy Minister",                 "Sector": "Energy / Minerals"},
    {"Name": "Rt. Hon. James Hartley",   "Organization": "UK Dept for Energy Security",        "Country": "UK",          "Title": "Deputy Minister, Mining & Minerals","Sector": "Critical Minerals"},
]

PRIORITY_OUTPUTS = {
    "Lithium Supply Chain Security — Reduce China Dependency": {
        "description": "Matching attendees against U.S. efforts to diversify critical minerals supply chains away from China — prioritizing lithium, cobalt, graphite, and rare earth supply partners.",
        "top8": [
            {"rank": 1, "name": "Alessandro Corsi",      "org": "Enel Green Power (Italy)",       "score": 96,
             "rationale": "Enel signed the Ministerial declaration and has active lithium investments in Chile and Argentina. A bilateral with Enel could anchor U.S.-Italy supply chain cooperation at the highest level.",
             "opening": "Alessandro, Secretary Rubio spoke highly of Enel's Ministerial commitment. We're looking to deepen that partnership — specifically around U.S. battery manufacturer supply agreements and the DFC financing framework."},
            {"rank": 2, "name": "Pierre Dubois",          "org": "European Commission (EU)",        "score": 93,
             "rationale": "The EU Critical Raw Materials Act Commissioner is the key policy architect for European supply chain standards. Alignment between U.S. and EU frameworks is foundational for allied-nation supply chain resilience.",
             "opening": "Commissioner Dubois, the U.S.-EU Critical Minerals Alliance announced at the Ministerial creates a real opportunity to harmonize supply chain criteria — I'd welcome a discussion on convergence around the CRMA certification framework."},
            {"rank": 3, "name": "Dr. Marco Van der Berg",  "org": "Vulcan Energy Resources (Germany)","score": 91,
             "rationale": "Vulcan's zero-carbon lithium process meets U.S. environmental supply chain criteria. Introduction to DOE battery materials program would be immediately high-value.",
             "opening": "Dr. Van der Berg, your geothermal lithium process is exactly the kind of allied-nation supply we're trying to scale. We'd like to connect you with our DOE team on the Battery Materials Network."},
            {"rank": 4, "name": "Kenji Tanaka",            "org": "Japan Critical Minerals Agency",  "score": 89,
             "rationale": "Japan is a Quad partner and top U.S. ally on supply chain resilience. The U.S.-Japan Critical Minerals Agreement needs operational follow-through — Japan JOGMEC is actively investing in allied sources.",
             "opening": "Director Tanaka, the U.S.-Japan minerals agreement gives us a strong framework. I'd like to discuss how our Rome-based engagement can support the Quad minerals working group agenda."},
            {"rank": 5, "name": "Rt. Hon. James Hartley",  "org": "UK Dept for Energy Security",    "score": 86,
             "rationale": "UK is a core Five Eyes partner with active critical minerals MOU discussions underway. UK-U.S. bilateral minerals dialogue is a natural complement to the broader Ministerial coalition.",
             "opening": "Minister Hartley, the U.S.-UK minerals MOU discussions are moving quickly — the Ambassador is keen to ensure our Rome framework is aligned with the bilateral track."},
            {"rank": 6, "name": "Carlos Matos",            "org": "Lithium Americas (Chile JV)",     "score": 82,
             "rationale": "Chile is the world's largest lithium producer. Lithium Americas' JV represents a direct U.S. supply chain asset that can be highlighted as a Ministerial success story.",
             "opening": "Carlos, Lithium Americas' Chile JV is exactly the allied-nation supply story we want to amplify. We'd like to discuss how DFC financing can accelerate your production timeline."},
            {"rank": 7, "name": "Dr. James Achebe",        "org": "African Minerals Dev. Centre (DRC)","score": 79,
             "rationale": "DRC holds 70% of global cobalt reserves. Strategic engagement with African minerals leadership is essential for diversification away from Chinese-controlled processing.",
             "opening": "Dr. Achebe, the Centre's work is central to everything we're trying to achieve. The U.S. DFC has significant appetite to finance allied-nation cobalt processing capacity."},
            {"rank": 8, "name": "H.E. Beatriz Santos",     "org": "Portuguese Government",          "score": 76,
             "rationale": "Portugal has significant Atlantic lithium deposits and is an active Ministerial participant. Portuguese special envoy status signals high-level political commitment.",
             "opening": "Ambassador Santos, Portugal's lithium reserves are one of the most underappreciated assets in the European supply chain story — we'd welcome a discussion on how U.S. DFC can support Portuguese minerals development."},
        ],
        "deprior": "Remaining 20 attendees routed to senior staff for follow-up bilaterals.  ⚠️  Ambassador Chen Wei (China) — engagement requires Ambassador-level clearance; coordinate with DCM before any interaction.",
    },
    "Food Security & FAO/WFP Accountability": {
        "description": "Matching attendees against USUN Rome's America First food security accountability mandate — FAO reform, WFP efficiency review, and U.S. taxpayer return on investment.",
        "top8": [
            {"rank": 1, "name": "Dr. Emmanuel Osei",    "org": "FAO (UN / Italy)",             "score": 97,
             "rationale": "FAO Deputy Director-General is the principal interlocutor for FAO reform. America First accountability agenda requires sustained DDG-level engagement to achieve structural governance change.",
             "opening": "Dr. Osei, the United States is FAO's largest contributor and we believe deeply in the organization's mission. We want to discuss how we can work together to ensure every dollar achieves maximum impact for the farmers and communities FAO serves."},
            {"rank": 2, "name": "Fatima Al-Rashid",     "org": "WFP Rome Liaison (UN)",        "score": 94,
             "rationale": "WFP accountability review is central to USUN Rome's mandate. The U.S. is WFP's largest bilateral donor — a direct relationship with WFP Rome leadership is essential for the efficiency review.",
             "opening": "Fatima, we remain WFP's largest donor and strongest advocate. Our accountability review is about making sure that investment achieves the impact it should — we'd welcome WFP's perspective on where administrative efficiencies are achievable."},
            {"rank": 3, "name": "Helena Svensson",       "org": "Yara International (Norway)", "score": 87,
             "rationale": "Yara's WFP School Meals Coalition partnership demonstrates effective private sector delivery. Their perspective on WFP operational efficiency is valuable input for the U.S. accountability framework.",
             "opening": "Helena, Yara's School Meals Coalition work is a model of what private sector-WFP partnership can achieve. We're interested in how Yara measures program impact — it's directly relevant to the efficiency framework we're developing."},
            {"rank": 4, "name": "Dr. Amara Diallo",      "org": "IFAD (UN / Italy)",           "score": 83,
             "rationale": "IFAD West Africa program is subject to the same U.S. accountability review as WFP. Direct IFAD engagement is essential for the comprehensive Rome-based agency assessment.",
             "opening": "Dr. Diallo, the U.S. values IFAD's rural development mission. We're conducting a comprehensive review of our Rome-based agency investments — your insights on the West Africa program impact would be invaluable."},
            {"rank": 5, "name": "Miguel Fernandez",      "org": "Brazilian Ministry of Agriculture","score": 77,
             "rationale": "Brazil is a key FAO member state and global agricultural powerhouse. Brazilian alignment with the U.S. food security reform agenda strengthens the coalition for FAO governance change.",
             "opening": "Mr. Fernandez, Brazil and the United States share a fundamental interest in ensuring FAO delivers results for global agriculture. We'd welcome Brazil's perspective on FAO reform priorities."},
            {"rank": 6, "name": "Dr. James Achebe",      "org": "African Minerals Dev. Centre (DRC)","score": 74,
             "rationale": "African agricultural development is at the heart of WFP and FAO mandates — a strategic perspective from the continent's development leadership amplifies the accountability agenda.",
             "opening": "Dr. Achebe, the Centre's perspective on how WFP and FAO programming lands in the DRC would be extremely valuable to our review — particularly around IFAD's rural development impact."},
            {"rank": 7, "name": "Prof. Roberto Ricci",   "org": "Mediterranean Energy Policy Institute (Italy)","score": 71,
             "rationale": "MEPI publishes influential food-energy nexus research cited by FAO technical committees — a credible third-party voice that can reinforce the U.S. accountability agenda with European audiences.",
             "opening": "Professor Ricci, MEPI's food-energy nexus research is some of the most cited work in FAO technical committees. We'd value your assessment of where FAO's programming is most and least effective."},
            {"rank": 8, "name": "Sophie Laurent",        "org": "Breakthrough Energy Europe (Belgium)","score": 68,
             "rationale": "Breakthrough Energy's food systems grants demonstrate private capital leveraging public investment — a key metric in the accountability framework that USUN Rome needs to amplify.",
             "opening": "Sophie, Breakthrough Energy's food systems portfolio is a compelling model of private capital amplifying public investment. We'd like to explore how that model can inform WFP's private sector engagement strategy."},
        ],
        "deprior": "Remaining 20 attendees routed to senior staff for follow-up bilaterals.  ⚠️  Ambassador Chen Wei (China) — China is a significant FAO funder; Ambassador-level engagement requires coordinated messaging; consult with DCM before any interaction.",
    },
}

# ── Tab 3: Policy Documents ───────────────────────────────────────────────

INTERNAL_DOCS = {
    "EO 14179 — American AI Leadership (Jan 2025)": {
        "key": "eo14179", "type": "Executive Order", "date": "January 23, 2025", "issuer": "The White House",
        "preview": "Revokes the Biden-era AI safety order. Directs agencies to prioritize AI innovation and U.S. competitive leadership. Establishes an AI Action Plan within 180 days. Emphasizes American AI leadership to outcompete adversaries — particularly China. Directs removal of regulatory barriers.",
    },
    "Critical Minerals Strategy 2026 — Secretary Rubio": {
        "key": "minerals2026", "type": "Strategic Document", "date": "January 2026", "issuer": "U.S. Dept of State",
        "preview": "Establishes U.S. leadership in critical minerals supply chain diversification. Authorizes $4B in DFC financing for allied-nation minerals projects. Requires 50% reduction in Chinese-sourced critical minerals for U.S. defense supply chains by 2030. Priority materials: lithium, cobalt, nickel, graphite, rare earths.",
    },
    "USUN Rome Cable: WFP Accountability Review (Jan 2026)": {
        "key": "wfp_cable", "type": "Diplomatic Cable", "date": "January 14, 2026", "issuer": "USUN Rome / Ambassador Blanchard",
        "preview": "Reports on Ambassador Blanchard's engagement with WFP leadership on operational efficiency. Notes U.S. concern about WFP's 23% administrative overhead (target: <18%). Identifies duplication between WFP school meals and FAO nutrition initiatives. Recommends withholding 15% of assessed contribution pending reform plan.",
    },
}

EXTERNAL_DOCS = {
    "Vatican Rome Call for AI Ethics (updated 2025)": {
        "key": "vatican_rome_call", "type": "Multilateral Declaration", "date": "November 2025", "issuer": "Pontifical Academy for Life",
        "preview": "Updated iteration of the 2020 Rome Call, co-signed by IBM, Microsoft, and 25 Catholic universities. Affirms six AI principles: transparency, inclusion, responsibility, impartiality, reliability, security. Emphasizes AI must serve human dignity and the common good. Calls for binding international AI governance. Specific concern: AI in weapons and mass surveillance.",
    },
    "FAO Digital Agriculture & AI Strategy (2024)": {
        "key": "fao_digital", "type": "Organizational Strategy", "date": "October 2024", "issuer": "Food and Agriculture Organization (FAO)",
        "preview": "FAO's framework for AI adoption in food and agriculture systems. Prioritizes small-scale farmer access, food security prediction modeling, and supply chain traceability. Calls for open-source AI development in agricultural domains. Cautions against proprietary monopolization of food system data. Endorses UN AI governance principles.",
    },
    "Italian G7 AI Declaration — Naples 2024": {
        "key": "g7_naples", "type": "G7 Declaration", "date": "July 2024", "issuer": "G7 Leaders (Italian Presidency)",
        "preview": "G7 leaders affirmed commitment to responsible AI development and international governance cooperation. Endorsed OECD AI Principles. Called for risk-based regulation preserving innovation space. Noted importance of human oversight in high-risk applications. Supported a joint G7 AI incident reporting framework.",
    },
}

ALIGNMENT_OUTPUTS = {
    "EO 14179 — American AI Leadership (Jan 2025)::Vatican Rome Call for AI Ethics (updated 2025)": {
        "score": 58, "color": "#f59e0b", "label": "Moderate Alignment — Framing Matters",
        "agreements": [
            "Both affirm security and reliability as core AI requirements — shared vocabulary for diplomatic engagement",
            "Both support sustained human oversight in high-stakes AI applications",
            "Shared concern about adversarial AI: U.S. frames as China/geopolitical competition; Vatican frames as arms proliferation risk",
        ],
        "tensions": [
            "EO 14179 removes safety guardrails to accelerate innovation; Vatican Rome Call explicitly calls for stronger binding governance frameworks — directly opposed regulatory philosophies",
            "U.S. frames AI leadership as competitive advantage vs. China; Vatican advocates for universalist 'common good' framing — the competitive framing creates rhetorical friction in Catholic diplomatic settings",
            "Vatican calls for international treaty-based AI governance; EO 14179 is explicitly unilateral — challenging to reconcile in multilateral forums where Vatican has outsized influence",
        ],
        "approach": "Engage Vatican through the shared language of human dignity and security — not competitive framing. The administration's commitment to 'safe and reliable AI' provides a credible bridge. Avoid discussing the revocation of Biden-era safety frameworks; pivot to what the U.S. is building forward. The Vatican's multilateral influence makes alignment on framing strategically essential.",
        "talking_points": [
            "\"The U.S. and the Holy See share a fundamental commitment: AI must serve humanity, not the other way around. Our AI Action Plan will ensure American technology upholds these values on the global stage.\"",
            "\"We see the Rome Call's six principles — transparency, inclusion, responsibility — as complementary to our approach. Responsible development and competitive leadership are not in conflict.\"",
            "\"The U.S. is uniquely positioned to set global standards for AI that reflect our shared values of human dignity and security. We'd welcome the Vatican's continued engagement in that process.\"",
        ],
    },
    "Critical Minerals Strategy 2026 — Secretary Rubio::FAO Digital Agriculture & AI Strategy (2024)": {
        "score": 77, "color": "#22c55e", "label": "Strong Alignment — Natural Partnership Opportunity",
        "agreements": [
            "Both strategies prioritize supply chain resilience and end-to-end traceability as foundational requirements",
            "Shared interest in technology-enabled transparency for raw material sourcing — FAO's traceability tools apply directly to minerals supply chains",
            "FAO's sustainable agriculture framework aligns with U.S. environmental criteria for allied-nation minerals sourcing, particularly for fertilizer inputs",
        ],
        "tensions": [
            "U.S. strategy explicitly excludes Chinese-sourced minerals; FAO's framework is supply-chain neutral and may complicate U.S. bilateral pressure on FAO member states that trade with China",
            "FAO emphasizes open-source digital tools and global data commons; U.S. critical minerals strategy relies on proprietary industry partnerships and U.S.-firm advantage",
        ],
        "approach": "Frame the U.S. critical minerals strategy as enabling food security through fertilizer supply chain security — phosphate and potash sourcing connects both agendas directly. The FAO-OCP Morocco collaboration is a natural bridge. Lead with the food security connection before raising Chinese supplier exclusion requirements.",
        "talking_points": [
            "\"Secure, diverse critical minerals supply chains are not just an energy issue — they're a food security issue. Fertilizers depend on the same minerals we're protecting, and FAO's supply chain traceability work is directly relevant.\"",
            "\"The U.S. critical minerals strategy opens market access for allied-nation producers, many of whom are key FAO partners in the developing world — this is complementary to FAO's agricultural mission, not competing with it.\"",
            "\"We see FAO's traceability framework as a natural complement to our supply chain transparency requirements. There's a genuine collaboration opportunity here — let's explore it.\"",
        ],
    },
    "USUN Rome Cable: WFP Accountability Review (Jan 2026)::FAO Digital Agriculture & AI Strategy (2024)": {
        "score": 71, "color": "#22c55e", "label": "Good Alignment — Reframe Accountability as Investment",
        "agreements": [
            "Both documents prioritize accountability and evidence-based performance measurement in international programming",
            "USUN Rome's reform agenda aligns with FAO Digital Strategy's call for data-driven program evaluation",
            "Shared interest in private sector partnership for program delivery — both emphasize leveraging commercial innovation",
        ],
        "tensions": [
            "USUN Rome cable recommends withholding 15% of assessed contribution — directly conflicts with FAO Digital Strategy's call for stable, long-term financing of digital agriculture programs",
            "U.S. focus on administrative overhead reduction may be perceived as conflicting with FAO's investment in digital infrastructure that drives long-term efficiency gains",
        ],
        "approach": "Reframe the U.S. accountability push as an investment in FAO's digital transformation — better data enables better programs which delivers better outcomes. Connect the efficiency review directly to FAO's own performance metrics framework in the Digital Strategy. The withholding conversation goes better when framed as a conditional bridge to reform, not a punitive measure.",
        "talking_points": [
            "\"The U.S. is FAO's largest contributor because we believe in the mission. Our accountability review is about making sure every dollar achieves maximum impact for the farmers and communities FAO serves.\"",
            "\"FAO's own Digital Agriculture Strategy calls for performance-based management and data-driven evaluation. We see our accountability framework as supporting, not opposing, exactly that vision.\"",
            "\"We're prepared to reinvest efficiency savings directly into FAO's digital agriculture programs — accountability and innovation are the same agenda, not opposing ones.\"",
        ],
    },
    "EO 14179 — American AI Leadership (Jan 2025)::Italian G7 AI Declaration — Naples 2024": {
        "score": 84, "color": "#22c55e", "label": "Strong Alignment — Comfortable Diplomatic Ground",
        "agreements": [
            "Both support risk-based AI regulation that preserves innovation space — shared foundational philosophy",
            "Aligned on competitive positioning vs. authoritarian AI development models — G7 Naples Declaration explicitly references democratic values",
            "Both endorse human oversight requirements for high-risk AI applications",
            "Shared commitment to AI safety research investment alongside accelerated deployment",
        ],
        "tensions": [
            "G7 Naples Declaration calls for binding multilateral AI governance mechanisms; EO 14179 is explicitly framed as unilateral U.S. leadership — manageable but needs bridging",
            "Naples Declaration endorses OECD AI Principles as the governance baseline; EO 14179 does not reference OECD framework — minor alignment gap on standards architecture",
        ],
        "approach": "Strong foundational alignment makes Italy a comfortable diplomatic conversation on AI. Lead with shared values on innovation and human oversight. Frame U.S. leadership as the prerequisite for effective multilateral standards — American technology shapes the standards that multilateral frameworks then codify. Italy's G7 presidency work is a genuine foundation to build on.",
        "talking_points": [
            "\"The G7 Naples Declaration and the administration's AI leadership agenda are pursuing the same goal through complementary paths — American innovation sets the standards that multilateral frameworks can then codify and scale.\"",
            "\"Italy's G7 presidency was a genuine step forward for AI governance. We're building on that foundation with our AI Action Plan, and we see Italy as a natural partner in that work.\"",
            "\"Risk-based regulation that protects innovation space is exactly the right model. The U.S. and Italy are aligned on keeping AI open, competitive, and human-centered.\"",
        ],
    },
    "Critical Minerals Strategy 2026 — Secretary Rubio::Italian G7 AI Declaration — Naples 2024": {
        "score": 79, "color": "#22c55e", "label": "Good Alignment — Leverage Ministerial Momentum",
        "agreements": [
            "Both identify supply chain resilience as a national and collective security imperative — strong shared framing",
            "Italy's G7 work aligns with the U.S. goal of reducing strategic dependence on authoritarian-state materials and technology",
            "Both frameworks support investment in processing capacity in allied nations as a sovereignty tool",
        ],
        "tensions": [
            "G7 Naples Declaration includes China in collaborative technology development language; U.S. Critical Minerals Strategy explicitly excludes Chinese suppliers — creates diplomatic tension in Italian multilateral settings",
            "EU member state sovereignty concerns about U.S. reshoring incentives may complicate Italian ministerial alignment on supply chain requirements",
        ],
        "approach": "Italy is a strong natural ally on critical minerals — ENI and Enel are active in the supply chain, and Italy participated in the February Ministerial. Lead with U.S.-Italy bilateral opportunity and Italian company advantage before raising Chinese supplier exclusion requirements. The Ministerial success creates political cover for deeper cooperation.",
        "talking_points": [
            "\"Italy's participation in the Critical Minerals Ministerial was a strong signal of shared commitment. We see Italy as a core partner in building the allied-nation supply chain — and Italian companies like Enel and ENI are well-positioned to benefit.\"",
            "\"The U.S. critical minerals framework creates investment opportunities for Italian companies — this is about building Italian and European industrial capacity, not just American reshoring.\"",
            "\"Building resilient supply chains together serves both Italian energy security and U.S. national security. This is a genuine win-win partnership, and the Ministerial gave us a strong platform to build from.\"",
        ],
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
for key in ["crm_result", "priority_result", "priority_scenario",
            "alignment_result", "alignment_pair"]:
    if key not in st.session_state:
        st.session_state[key] = None


# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="demo-header">
  <div class="sub">Snowflake AI Data Cloud — Live Demo</div>
  <h1>🏛️ US Mission to the UN Agencies in Rome</h1>
  <div class="badges">
    <span class="hbadge hbadge-blue">September 18, 2026</span>
    <span class="hbadge hbadge-amber">USUN Rome</span>
    <span class="hbadge hbadge-purple">Demo Build</span>
    <span class="hbadge hbadge-green">Cortex AI</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — Mission Context
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏛️ USUN Rome")
    st.markdown('<div class="sb-header">ACTIVE STRATEGIC PRIORITIES</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item">⛏️ Critical minerals supply chain diversification — reduce China dependency</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item">🌾 WFP & FAO accountability — America First efficiency review</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item">🤖 AI diplomacy alignment — Vatican & EU partner engagement</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item">🇮🇹 U.S.-Italy bilateral energy & minerals partnership</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<div class="sb-header">ROME-BASED UN AGENCIES</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">FAO — Food & Agriculture Organization</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">WFP — World Food Programme</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">IFAD — Int\'l Fund for Agricultural Development</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<div class="sb-header">SNOWFLAKE FEATURES SHOWN</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">Cortex Complete</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">Cortex Search</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">Cortex Analyst</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">Document AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-item-dim">Snowflake Data Sharing</div>', unsafe_allow_html=True)

    st.divider()
    st.caption("All data in this demo is synthetic and scripted for demonstration purposes.")


# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "📊  CRM Enrichment Pipeline",
    "⚡  Event Prioritization Engine",
    "📄  Policy Alignment Analyzer",
])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — CRM ENRICHMENT PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("#### Automated CRM Enrichment via Snowflake Cortex")
    st.markdown(
        "Select any CRM contact. Snowflake cross-references internal activity data, external sector intelligence, "
        "and diplomatic signals to produce an enriched stakeholder profile — sector rank, relationship signal, "
        "strategic alignment score, and recommended action.",
        help="In production: this pipeline runs on an automated schedule against your CRM system via Snowflake Data Sharing."
    )

    col_left, col_right = st.columns([1, 2])

    with col_left:
        company_names = [c["name"] for c in CRM_CONTACTS]
        selected = st.selectbox("Select CRM Contact", company_names, key="crm_select")

        # Show raw CRM record
        contact = next(c for c in CRM_CONTACTS if c["name"] == selected)
        st.markdown(f"""
        <div class="sf-card" style="margin-top:12px;">
          <div class="sf-card-title">{contact['name']}</div>
          <div class="sf-card-sub">{contact['type']}</div>
          <div style="margin-top:10px;font-size:12px;color:#94a3b8;line-height:1.8;">
            <b style="color:#cbd5e1;">Country:</b> {contact['country']}<br>
            <b style="color:#cbd5e1;">HQ:</b> {contact['hq']}<br>
            <b style="color:#cbd5e1;">Contact:</b> {contact['contact']}<br>
            <b style="color:#cbd5e1;">Last Interaction:</b> {contact['last']}<br>
          </div>
          <div style="margin-top:10px;font-size:10px;color:#475569;">
            ⚠️ Raw CRM record — unenriched
          </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⚡ Enrich with Snowflake Cortex", key="enrich_btn", use_container_width=True, type="primary"):
            with st.spinner(f"Querying Cortex Search · Fetching sector intelligence · Computing alignment score..."):
                time.sleep(1.8)
            st.session_state.crm_result = selected

    with col_right:
        if st.session_state.crm_result and st.session_state.crm_result in CRM_ENRICHMENT:
            e = CRM_ENRICHMENT[st.session_state.crm_result]

            # Signal badge CSS class
            sig_class = {
                "Warm": "sig-warm", "Neutral": "sig-neutral",
                "Cool": "sig-cool",  "Strategic": "sig-strategic",
            }.get(e["signal"], "sig-neutral")

            # Score color
            score_color = "#22c55e" if e["score"] >= 75 else ("#f59e0b" if e["score"] >= 60 else "#ef4444")

            st.markdown(f"""
            <div class="enrich-card">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
                <div>
                  <div style="font-size:16px;font-weight:700;color:#f1f5f9;">{st.session_state.crm_result}</div>
                  <div style="margin-top:6px;">
                    <span class="sig {sig_class}">{e['signal']}</span>
                    &nbsp;<span style="font-size:12px;color:#94a3b8;">Relationship Signal</span>
                  </div>
                </div>
                <div style="text-align:right;">
                  <div style="font-size:36px;font-weight:800;color:{score_color};line-height:1;">{e['score']}</div>
                  <div style="font-size:11px;color:#64748b;">Alignment Score</div>
                </div>
              </div>
              <div class="enrich-rank" style="margin-top:12px;">🏆 {e['rank']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(e["score"] / 100, text=f"Strategic Alignment: {e['score']}%")

            st.markdown(f"""
            <div style="margin-top:16px;">
              <div class="section-lbl">Intelligence Summary</div>
              <div class="enrich-summary">{e['summary']}</div>
              <div class="section-lbl">Recommended Action</div>
              <div class="enrich-action"><strong>→</strong> {e['action']}</div>
              <div class="data-sources">Powered by <span class="cortex-badge">⬡ {e['feature']}</span>
              &nbsp;&nbsp;·&nbsp;&nbsp; Sources: {e['sources']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align:center;padding:60px 20px;color:#475569;">
                <div style="font-size:40px;margin-bottom:12px;">⬡</div>
                <div style="font-size:14px;">Select a contact and click <strong style="color:#7dd3fc;">Enrich with Snowflake Cortex</strong> to generate the enriched profile.</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — EVENT PRIORITIZATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("#### Ambassador Bandwidth Prioritization — Critical Minerals Summit")
    st.markdown(
        "28 attendees. 4 hours of Ambassador time. Select the mission priority scenario and let "
        "Cortex Analyst match every attendee against USUN Rome's strategic priorities — surfacing the top 8 "
        "contacts with ranked rationale and an opening line for the Ambassador.",
    )

    col_a, col_b = st.columns([1, 3])

    with col_a:
        scenario = st.radio(
            "Mission Priority Scenario",
            list(PRIORITY_OUTPUTS.keys()),
            key="scenario_radio",
        )
        st.markdown(f'<div style="font-size:11px;color:#64748b;margin-top:4px;">{PRIORITY_OUTPUTS[scenario]["description"]}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🎯 Prioritize Ambassador Bandwidth", key="priority_btn", use_container_width=True, type="primary"):
            with st.spinner("Matching 28 attendees against mission priorities via Cortex Analyst..."):
                time.sleep(2.2)
            st.session_state.priority_result = True
            st.session_state.priority_scenario = scenario

        st.markdown('<div class="cortex-badge" style="margin-top:8px;">⬡ Cortex Analyst + Snowflake Data Sharing</div>', unsafe_allow_html=True)

    with col_b:
        df = pd.DataFrame(SUMMIT_ATTENDEES)
        st.markdown('<div class="section-lbl">Full Attendee Roster — Critical Minerals Summit · Rome 2026</div>', unsafe_allow_html=True)
        st.dataframe(df, height=240, use_container_width=True, hide_index=True)

    if st.session_state.priority_result:
        active_scenario = st.session_state.priority_scenario or scenario
        output = PRIORITY_OUTPUTS[active_scenario]

        st.divider()
        st.markdown(f"#### Ambassador Priority List — *{active_scenario}*")

        p_col1, p_col2 = st.columns(2)
        top8 = output["top8"]

        for i, p in enumerate(top8):
            col = p_col1 if i % 2 == 0 else p_col2
            with col:
                st.markdown(f"""
                <div class="priority-card">
                  <div class="p-rank">{p['rank']}</div>
                  <div class="p-name">{p['name']}</div>
                  <div class="p-org">{p['org']}</div>
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;clear:both;">
                    <div style="background:#29B5E8;border-radius:4px;height:6px;width:{p['score']}%;max-width:200px;"></div>
                    <span style="font-size:11px;color:#29B5E8;font-weight:700;">{p['score']}</span>
                  </div>
                  <div class="p-rat">{p['rationale']}</div>
                  <div class="p-open">💬 {p['opening']}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f'<div class="deprior">📋 <strong style="color:#f1f5f9;">Staff Routing:</strong> {output["deprior"]}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — POLICY ALIGNMENT ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("#### Cross-Document Policy Alignment Analysis")
    st.markdown(
        "Select an internal administration document alongside an external policy document. "
        "Cortex Complete cross-references both, scores alignment, identifies points of agreement and tension, "
        "and generates a recommended diplomatic approach with Ambassador talking points.",
    )

    c1, c_mid, c2 = st.columns([5, 1, 5])

    with c1:
        st.markdown('<div class="section-lbl">Internal / Administration Document</div>', unsafe_allow_html=True)
        internal_sel = st.selectbox("Internal Document", list(INTERNAL_DOCS.keys()), key="int_sel", label_visibility="collapsed")
        idoc = INTERNAL_DOCS[internal_sel]
        st.markdown(f"""
        <div class="doc-card">
          <div class="doc-type">{idoc['type']} · {idoc['date']}</div>
          <div class="doc-title">{internal_sel}</div>
          <div class="doc-issuer">Issuer: {idoc['issuer']}</div>
          <div class="doc-preview">{idoc['preview']}</div>
        </div>
        """, unsafe_allow_html=True)

    with c_mid:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;font-size:22px;font-weight:800;color:#334155;padding-top:16px;">VS</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-lbl">External / Partner Document</div>', unsafe_allow_html=True)
        external_sel = st.selectbox("External Document", list(EXTERNAL_DOCS.keys()), key="ext_sel", label_visibility="collapsed")
        edoc = EXTERNAL_DOCS[external_sel]
        st.markdown(f"""
        <div class="doc-card">
          <div class="doc-type">{edoc['type']} · {edoc['date']}</div>
          <div class="doc-title">{external_sel}</div>
          <div class="doc-issuer">Issuer: {edoc['issuer']}</div>
          <div class="doc-preview">{edoc['preview']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    btn_col, _ = st.columns([2, 5])
    with btn_col:
        analyze_clicked = st.button("🔍 Analyze Alignment", key="align_btn", use_container_width=True, type="primary")

    if analyze_clicked:
        pair_key = f"{internal_sel}::{external_sel}"
        if pair_key in ALIGNMENT_OUTPUTS:
            with st.spinner("Running cross-document analysis via Cortex Complete · Scoring alignment · Generating diplomatic guidance..."):
                time.sleep(2.0)
            st.session_state.alignment_result = pair_key
        else:
            st.session_state.alignment_result = "__not_found__"
            st.session_state.alignment_pair = (internal_sel, external_sel)

    if st.session_state.alignment_result and st.session_state.alignment_result != "__not_found__":
        pair_key = st.session_state.alignment_result
        if pair_key in ALIGNMENT_OUTPUTS:
            r = ALIGNMENT_OUTPUTS[pair_key]
            st.divider()

            score_col, details_col = st.columns([1, 3])

            with score_col:
                st.markdown(f"""
                <div class="align-score-box">
                  <div class="align-score-num" style="color:{r['color']};">{r['score']}%</div>
                  <div class="align-score-lbl">{r['label']}</div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(r["score"] / 100)
                st.markdown('<div class="cortex-badge" style="margin-top:12px;width:100%;justify-content:center;">⬡ Cortex Complete + Document AI</div>', unsafe_allow_html=True)

            with details_col:
                # Agreements
                st.markdown('<div class="section-lbl">✅ Points of Agreement</div>', unsafe_allow_html=True)
                for a in r["agreements"]:
                    st.markdown(f'<div class="agree-item"><span>✓</span><span>{a}</span></div>', unsafe_allow_html=True)

                # Tensions
                st.markdown('<div class="section-lbl">⚠️ Points of Tension</div>', unsafe_allow_html=True)
                for t in r["tensions"]:
                    st.markdown(f'<div class="tension-item"><span>↗</span><span>{t}</span></div>', unsafe_allow_html=True)

                # Approach
                st.markdown('<div class="section-lbl">🧭 Recommended Diplomatic Approach</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="approach-box">{r["approach"]}</div>', unsafe_allow_html=True)

                # Talking points
                st.markdown('<div class="section-lbl">💬 Suggested Ambassador Talking Points</div>', unsafe_allow_html=True)
                for tp in r["talking_points"]:
                    st.markdown(f'<div class="tp-box">{tp}</div>', unsafe_allow_html=True)

    elif st.session_state.alignment_result == "__not_found__":
        int_name, ext_name = st.session_state.alignment_pair
        st.info(
            f"Analysis for **{int_name}** ↔ **{ext_name}** is not in the demo library. "
            "Featured pairings: EO 14179 ↔ Vatican Rome Call · Critical Minerals 2026 ↔ FAO Digital Agriculture · "
            "WFP Cable ↔ FAO Digital Agriculture · EO 14179 ↔ G7 Naples · Critical Minerals 2026 ↔ G7 Naples"
        )
