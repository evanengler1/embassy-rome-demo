# Prompt: Build a Polished React App — USUN Rome Diplomatic Intelligence Dashboard

Build a visually stunning, highly interactive React (Next.js) single-page application for the **U.S. Mission to the UN Agencies in Rome (USUN Rome)**. This is a diplomatic intelligence dashboard that demonstrates Snowflake's AI Data Cloud capabilities applied to real diplomatic operations. The app should feel like a premium intelligence platform — think Bloomberg Terminal meets a modern government operations center, with smooth animations, rich micro-interactions, and a dark, authoritative aesthetic.

---

## Tech Stack

- **Framework:** Next.js 14+ (App Router)
- **Styling:** Tailwind CSS + custom CSS for glassmorphism and glow effects
- **Animation:** Framer Motion for page transitions, card reveals, number counters, and micro-interactions
- **Charts:** Recharts or Nivo for any data visualization (radar charts, bar charts, gauges)
- **Icons:** Lucide React
- **Font:** Inter or similar clean sans-serif; monospace accent font for scores/metrics (e.g., JetBrains Mono)
- **State:** React state + server actions (no heavy state library needed)

The app will initially run standalone (local dev / Vercel) and later be deployed as a Snowflake App (SAR / Next.js on SPCS). Structure the project so it is compatible with `snow app` deployment later.

---

## Design Direction

### Overall Aesthetic
- **Dark theme** — deep navy/slate background (#0a0f1a or similar), not pure black
- **Glassmorphism** — frosted-glass card surfaces with subtle backdrop-blur, thin white/blue border highlights
- **Government/intelligence feel** — clean grid layout, data-dense but not cluttered, typography-driven hierarchy
- **Accent colors:** Electric blue (#3b82f6) as primary accent, amber/gold (#f59e0b) for warnings/scores, emerald (#10b981) for positive signals, rose (#f43f5e) for tensions
- **Subtle background pattern** — faint dot grid or topographic map lines to evoke a command center
- **Glow effects** — soft blue glow on active elements, hover states, and score indicators

### Animations & Interactions
- Page/tab transitions: smooth crossfade with slight vertical slide (Framer Motion AnimatePresence)
- Cards: staggered fade-in on load (each card 50ms delayed from the previous)
- Score counters: animate from 0 to final value over ~1s using a counting animation
- Progress bars / gauges: animate fill on reveal
- Buttons: subtle scale + glow on hover, satisfying press feedback
- Loading states: skeleton shimmer effects (not spinners) while AI is processing; a pulsing "Cortex is thinking..." indicator with animated dots
- Tooltips: smooth fade with slight scale on hover over data points
- Data tables: row highlight on hover with subtle left-border accent color

### Layout
- Full-width app, max-width ~1400px centered
- Top navigation bar with the USUN Rome title, a subtle US flag / eagle icon, and tab navigation
- Three main sections accessed via tabs (or a vertical sidebar nav):
  1. CRM Enrichment
  2. Event Prioritization
  3. Policy Alignment
- Sidebar (collapsible) showing Mission Context — strategic priorities, key agencies

---

## Data Source — Snowflake

All data lives in the Snowflake account `<YOUR_ACCOUNT>`, database `DOS_ROME_DEMO`, organized in a medallion architecture (BRONZE / SILVER / GOLD schemas).

The app should connect to Snowflake via a backend API route (Next.js API routes or server actions) using the Snowflake Node.js driver (`snowflake-sdk`). For AI features, call `SNOWFLAKE.CORTEX.COMPLETE('mistral-large2', ...)` and Cortex Search via SQL.

### Tables (all in `DOS_ROME_DEMO.BRONZE`)

**CRM_CONTACTS** (25 rows) — Diplomatic stakeholder organizations
- Columns: `ORG_NAME`, `SECTOR_TYPE`, `COUNTRY`, `HQ`, `PRIMARY_CONTACT`, `LAST_INTERACTION`
- Sectors: Critical Minerals, Food Security, AI Ethics, Bilateral Energy, Multilateral Governance

**CRM_ACTIVITY_LOG** (108 rows) — Diplomatic interaction history
- Columns: `ORG_NAME`, `ACTIVITY_DATE`, `ACTIVITY_TYPE`, `ACTIVITY_DETAIL`
- Types: Ambassador Meeting, Diplomatic Cable, DCM Call, Ministerial Event, Policy Email

**SECTOR_INTELLIGENCE** (59 rows) — External intel records
- Columns: `ORG_NAME`, `INTEL_DATE`, `INTEL_SUMMARY`, `SOURCE`
- Sources: Reuters, Bloomberg, FAO Press, State Dept cables, EU Monitor, Vatican Press Office

**SUMMIT_ATTENDEES** (28 rows) — Critical Minerals Summit roster
- Columns: `NAME`, `ORGANIZATION`, `COUNTRY`, `TITLE`, `SECTOR`

**MISSION_PRIORITIES** (4 rows) — USUN Rome strategic priorities
- Columns: `PRIORITY_NAME`, `DESCRIPTION`
- Priorities: Lithium Supply Chain Security, FAO/WFP Accountability, AI Governance Alignment, U.S.-Italy Bilateral Energy

**POLICY_DOCUMENTS** (6 rows) — Internal and external policy docs with full text
- Columns: `DOC_TITLE`, `DOC_TYPE`, `DOC_DATE`, `ISSUER`, `CLASSIFICATION` (Internal/External), `SUMMARY`, `FULL_TEXT`

### AI Services (in `DOS_ROME_DEMO.SILVER`)

**POLICY_DOCS_SEARCH** — Cortex Search Service over policy document text
**SECTOR_INTEL_SEARCH** — Cortex Search Service over sector intelligence

### LLM

All AI generation uses `SNOWFLAKE.CORTEX.COMPLETE('mistral-large2', ...)` with chat-style messages (system + user prompts). Temperature 0.1 for structured JSON output.

---

## Feature Specifications

### Tab 1: CRM Enrichment Pipeline

**Left panel — Contact selector:**
- Dropdown or searchable list showing all 25 CRM contacts
- When a contact is selected, display a compact "raw CRM card" showing: org name, sector type, country, HQ, primary contact, last interaction date
- Style: muted card with a "RAW" badge, subtle dot pattern background to convey "unprocessed"
- A prominent "Enrich with Cortex" button with a blue glow effect

**Right panel — Enriched profile (appears after enrichment):**
- Animated reveal: the raw card "transforms" — glass card slides in from right or morphs with a shimmer
- **Alignment Score:** Large animated number (0-100) with a circular gauge or radial progress indicator. Color-coded: green >70, amber 40-70, red <40
- **Relationship Signal:** Pill badge — "Warm" (green), "Neutral" (gray), "Cool" (blue), "Strategic" (gold) with a subtle pulse animation on reveal
- **Sector Rank:** One-line assessment in a highlighted text block
- **Intelligence Summary:** 3-4 sentence paragraph in a card with a subtle left border accent
- **Recommended Action:** Highlighted action card with an arrow icon, distinct from the summary
- Footer caption: "Powered by Cortex Complete + Cortex Search" with animated service badges

**Under the hood:**
1. Query `CRM_ACTIVITY_LOG` for the selected org (top 5 by date)
2. Query `SECTOR_INTELLIGENCE` for the selected org (top 3 by date)
3. Call Cortex Search on `POLICY_DOCS_SEARCH` with the org name + sector context
4. Send all gathered context to `CORTEX.COMPLETE` with this system prompt: "You are a diplomatic intelligence analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You assess private-sector and multilateral stakeholders against U.S. strategic priorities: critical minerals supply chain diversification away from China, WFP/FAO accountability reform, and AI-diplomacy alignment. You are precise, sober, and action-oriented. You output ONLY valid JSON."
5. Request JSON with keys: `sector_rank`, `relationship_signal`, `alignment_score` (int 0-100), `intelligence_summary`, `recommended_action`

### Tab 2: Event Prioritization Engine

**Left panel — Scenario selector:**
- Radio buttons or stylized cards for the 4 mission priority scenarios
- Each shows the priority name and a one-line description
- A prominent "Prioritize Ambassador Bandwidth" button

**Main area — Summit roster:**
- A sleek data table showing all 28 summit attendees: Name, Organization, Country, Title, Sector
- Row hover highlights with subtle left-border color accent
- Before prioritization: all rows neutral styling

**Results area (appears after prioritization):**
- The top 8 prioritized contacts displayed as **ranked cards** with staggered animation reveal
- Each card shows:
  - Rank number (large, bold, accent-colored)
  - Name + Organization (country)
  - Priority Score: animated number (0-100) with a small horizontal progress bar
  - Rationale: 1-2 sentence explanation
  - Opening Line: in italics or a distinct "quote" styled block — the exact words the Ambassador should use
- Cards arranged in a 2x4 grid or a vertical ranked list with decreasing visual emphasis
- A "deprioritized note" footer explaining how remaining attendees are handled
- Bonus: a radar chart or dot plot showing score distribution across all 8

**Under the hood:**
1. Load all `SUMMIT_ATTENDEES` as a roster
2. Load the selected `MISSION_PRIORITIES` scenario description
3. Call Cortex Search on `POLICY_DOCS_SEARCH` for relevant policy context
4. Send everything to `CORTEX.COMPLETE` with system prompt: "You are a strategic scheduling analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You match summit attendees against a stated mission priority and rank the highest-value engagements for the Ambassador."
5. Request JSON with `ranked` array (8 items: rank, name, org, score, rationale, opening_line) and `deprioritized_note`

### Tab 3: Policy Alignment Analyzer

**Top area — Document pair selector:**
- Two side-by-side selection panels:
  - Left: Internal/Administration documents (filtered by CLASSIFICATION = 'Internal')
  - Right: External/Partner documents (filtered by CLASSIFICATION = 'External')
- Each selected document shows: title, type, date, issuer, and summary preview
- Style: two glass cards side-by-side, a visual "vs" divider between them with a subtle glow line
- "Analyze Alignment" button centered below

**Results area (appears after analysis):**
- **Alignment Score:** Hero metric — large animated percentage with a horizontal gradient bar (red → amber → green). Below it, a label like "Strong Alignment — Natural Partnership Opportunity"
- **Points of Agreement:** Bulleted list with green check icons, each item with a fade-in stagger
- **Points of Tension:** Bulleted list with amber/red warning icons, staggered reveal
- **Diplomatic Approach:** A distinct card with a strategy icon, the full paragraph recommendation
- **Ambassador Talking Points:** Numbered list in a highlighted "briefing card" style — looks like something you'd hand to someone before a meeting. Each point in its own mini-card with a quote icon.
- Bonus: A side-by-side "document comparison" mini-view showing which sections of each doc were referenced

**Under the hood:**
1. Load selected internal and external `POLICY_DOCUMENTS` (including FULL_TEXT)
2. Send both full texts to `CORTEX.COMPLETE` with system prompt: "You are a senior policy alignment analyst for the U.S. Mission to the UN Agencies in Rome (USUN Rome). You compare a U.S./administration policy document against an external or partner policy document, quantify alignment, and produce diplomatic guidance the Ambassador can act on. You are candid about genuine tensions rather than papering over them."
3. Request JSON with: `alignment_score` (int 0-100), `label`, `agreements` (array), `tensions` (array), `diplomatic_approach` (string), `talking_points` (array of 3)

---

## Sidebar — Mission Context

Always visible (collapsible on mobile):
- **Header:** "Mission Context" with a subtle seal/shield icon
- **Strategic Priorities:** Bulleted list of the 4 priorities, each with a small colored dot
- **Rome-Based UN Agencies:** FAO, WFP, IFAD
- **Footer:** "All data is synthetic for demonstration purposes" disclaimer
- Style: darker glass panel, more subdued than main content

---

## Header / Navigation

- App title: "U.S. Mission to the UN Agencies in Rome" — large, clean typography
- Subtitle: "Snowflake AI Data Cloud — Intelligence Dashboard"
- Tab navigation with animated underline indicator that slides between tabs
- Optional: a small "Powered by Snowflake" badge in the corner with the Snowflake logo

---

## Loading & Error States

- **Loading (AI processing):** Skeleton shimmer cards in the results area. A pulsing "Analyzing via Cortex..." text with animated ellipsis. The button shows a subtle loading ring.
- **Error:** Toast notification in the bottom-right with a red accent, auto-dismiss after 5s. Errors should not crash the UI — show a "retry" option.
- **Empty state:** Before any analysis is run, show a tasteful placeholder with an icon and text like "Select a contact and enrich to begin."

---

## Project Structure

```
react-app/
  src/
    app/
      layout.tsx           # Root layout with dark theme, fonts, metadata
      page.tsx             # Main dashboard page with tab routing
      api/
        snowflake/
          route.ts         # API route for Snowflake queries (SQL + Cortex)
    components/
      layout/
        Header.tsx
        Sidebar.tsx
        TabNav.tsx
      crm/
        ContactSelector.tsx
        RawContactCard.tsx
        EnrichedProfile.tsx
        AlignmentGauge.tsx
      prioritization/
        ScenarioSelector.tsx
        AttendeeTable.tsx
        RankedCard.tsx
        PriorityResults.tsx
      alignment/
        DocumentSelector.tsx
        AlignmentScore.tsx
        AgreementsList.tsx
        TensionsList.tsx
        TalkingPoints.tsx
      shared/
        GlassCard.tsx      # Reusable glassmorphism container
        AnimatedNumber.tsx  # Counting animation for scores
        SkeletonLoader.tsx  # Shimmer loading placeholder
        SignalBadge.tsx     # Colored pill for relationship signals
        ProgressGauge.tsx   # Radial or linear animated progress
    lib/
      snowflake.ts         # Snowflake connection + query helpers
      cortex.ts            # Cortex Complete + Cortex Search wrappers
      types.ts             # TypeScript interfaces for all data models
    styles/
      globals.css          # Tailwind base + custom glass/glow utilities
  public/
    ...
  tailwind.config.ts
  next.config.js
  package.json
```

---

## Important Notes

- Every visual element should feel intentional and polished — no default browser styling, no unstyled scrollbars, no janky transitions
- The app should feel fast even when waiting for AI — loading states should be engaging, not frustrating
- Responsive is nice-to-have but the primary target is a widescreen laptop display (demo setting)
- All data is synthetic and for demonstration purposes — the app should include a small disclaimer
- Keep the codebase clean and well-typed (TypeScript throughout, no `any` types)
- The Snowflake connection config should use environment variables (SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, etc.) — never hardcode credentials
