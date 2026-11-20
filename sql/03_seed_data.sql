-- =============================================================================
-- USUN Rome Demo | 03_seed_data.sql
-- Populates all 6 tables with synthetic diplomatic operations data.
-- =============================================================================

USE ROLE DOS_ROME_DEMO_ROLE;
USE WAREHOUSE DOS_ROME_DEMO_WH;
USE DATABASE DOS_ROME_DEMO;
USE SCHEMA BRONZE;

-- =============================================================================
-- TABLE 1: CRM_CONTACTS
-- =============================================================================
INSERT INTO CRM_CONTACTS
    (org_name, sector, country, hq_city, primary_contact_name, primary_contact_title, last_interaction_date, relationship_status, org_description)
VALUES
    ('Enel Green Power', 'Energy / Critical Minerals', 'Italy', 'Rome', 'Maria Rossi', 'VP Government Affairs', '2026-08-12', 'Warm', 'Italy''s largest renewable energy operator and a key partner on grid-scale storage and battery-materials supply chains. Actively courting U.S. financing frameworks for allied lithium and rare-earth sourcing.'),
    ('ENI S.p.A.', 'Oil & Gas / Critical Minerals', 'Italy', 'Rome', 'Roberto Ferretti', 'EU Affairs Director', '2026-06-28', 'Neutral', 'Italian state-linked energy major with expanding interests in critical minerals and energy transition materials. Engagement is cordial but guarded on U.S. supply-chain alignment.'),
    ('APSA (Vatican Investments)', 'Finance / Ethics', 'Vatican City', 'Vatican', 'Msgr. Pietro Conti', 'Secretary', '2026-07-09', 'Strategic', 'Administration of the Patrimony of the Apostolic See, managing Vatican investments with an ethics-driven mandate. A strategic interlocutor on responsible finance and AI-ethics diplomacy.'),
    ('Vulcan Energy Resources', 'Lithium Processing', 'Germany', 'Frankfurt', 'Dr. Marco Van der Berg', 'CTO', '2026-08-05', 'Warm', 'European zero-carbon lithium developer positioned as an allied-nation alternative to Chinese processing capacity. Strong candidate for DFC-backed offtake arrangements.'),
    ('Albemarle Corporation', 'Lithium / Bromine', 'USA', 'Charlotte, NC', 'Thomas Whitmore', 'VP Gov. Affairs', '2026-07-22', 'Warm', 'Leading U.S. lithium and specialty-chemicals producer central to the Critical Minerals Strategy. Coordinates closely with the Mission on Ministerial coalition-building.'),
    ('Yara International', 'Fertilizers / Food Security', 'Norway', 'Oslo', 'Helena Svensson', 'Int''l Relations', '2026-05-30', 'Warm', 'Global fertilizer leader bridging critical-minerals (phosphates, potash) and food-security agendas. Regular participant in FAO and Rome-based food-system dialogues.'),
    ('Cargill International (Rome)', 'Agriculture / Food Security', 'USA', 'Rome (EMEA)', 'James O''Connor', 'Regional Director', '2026-08-18', 'Strategic', 'EMEA regional hub of the U.S. agribusiness giant and a strategic private-sector anchor for FAO and WFP food-security initiatives. Deep alignment with U.S. accountability priorities.'),
    ('OCP Group', 'Critical Minerals / Phosphates', 'Morocco', 'Casablanca', 'Hamid Benali', 'VP International', '2026-03-11', 'Neutral', 'Moroccan phosphate and fertilizer state champion controlling a major share of global phosphate reserves. Engagement balances food-security and critical-minerals interests.'),
    ('Barrick Gold (Italy)', 'Mining', 'Canada', 'Toronto', 'Lucia Fernandez', 'EU Affairs', '2026-01-19', 'Cool', 'Canadian gold and copper mining major with European government-affairs presence. Relationship is currently cool pending clarity on EU permitting exposure.'),
    ('Breakthrough Energy Europe', 'Clean Energy / Minerals', 'Belgium', 'Brussels', 'Sophie Laurent', 'Managing Director', '2026-06-15', 'Warm', 'Gates-founded clean-energy investment vehicle funding minerals and storage innovation in Europe. A useful convener for allied-nation supply-chain financing.'),
    ('FAO Private Sector Advisory Group', 'Food Security / Multi-stakeholder', 'Italy', 'Rome (FAO)', 'Prof. Anna Kessler', 'Chair', '2026-08-20', 'Strategic', 'Multi-stakeholder advisory body linking FAO with private industry on food-system reform. A strategic platform for advancing U.S. accountability and efficiency messaging.'),
    ('World Resources Institute Rome', 'Environmental Policy', 'USA / Italy', 'Rome', 'Dr. Maria Gonzalez', 'Director', '2026-07-03', 'Warm', 'Rome office of the global environmental think tank providing analysis on minerals, land use, and food systems. Frequent source of open-source intelligence for the Mission.'),
    ('IFAD', 'Food Security / Development', 'UN / Italy', 'Rome', 'Dr. Amara Diallo', 'Director, West Africa Program', '2026-08-08', 'Strategic', 'International Fund for Agricultural Development, a Rome-based UN agency financing rural development. Under U.S. review as part of the Rome-agency accountability mandate.'),
    ('WFP', 'Food Security / Humanitarian', 'UN / Italy', 'Rome', 'Fatima Al-Rashid', 'Executive Director, Rome Office', '2026-08-25', 'Strategic', 'World Food Programme, the largest Rome-based UN agency and a primary focus of U.S. accountability and efficiency demands. Central to the WFP reform cable track.'),
    ('Leonardo S.p.A.', 'Defense / Aerospace', 'Italy', 'Rome', 'Gen. (ret.) Paolo Bianchi', 'Director, Institutional Relations', '2026-06-05', 'Neutral', 'Italian defense and aerospace prime with interests in secure supply chains for critical materials. Engagement supports the U.S.-Italy bilateral industrial track.'),
    ('Terna S.p.A.', 'Energy Transmission', 'Italy', 'Rome', 'Dott.ssa Elena Costa', 'Head of Regulatory Affairs', '2026-07-14', 'Warm', 'Italy''s national electricity transmission operator, critical to grid modernization and storage integration. Relevant to bilateral energy-partnership objectives.'),
    ('SQM (Sociedad Quimica y Minera)', 'Lithium Processing', 'Chile', 'Santiago', 'Carlos Matos', 'VP International Affairs', '2026-05-12', 'Neutral', 'Chilean lithium and specialty-fertilizer producer among the world''s largest lithium suppliers. A key allied-nation source for supply-chain diversification.'),
    ('BASF SE', 'Chemicals / Battery Materials', 'Germany', 'Ludwigshafen', 'Dr. Klaus Weber', 'Head of Battery Materials EU', '2026-06-20', 'Warm', 'German chemicals major and cathode-materials producer central to European battery supply chains. Candidate partner for allied processing capacity.'),
    ('Pontifical Academy for Life', 'AI Ethics / Multilateral', 'Vatican City', 'Vatican', 'Bishop Vincenzo Paglia', 'President', '2026-07-28', 'Strategic', 'Vatican body that convenes the Rome Call for AI Ethics and shapes global AI-governance norms. A strategic partner on the Mission''s AI-diplomacy agenda.'),
    ('Italian Ministry of Environment (MASE)', 'Government / Critical Minerals', 'Italy', 'Rome', 'Dr. Isabella Moretti', 'Director, Critical Materials', '2026-08-10', 'Strategic', 'Italy''s Ministry for the Environment and Energy Security, lead on domestic critical-materials policy. Primary government counterpart for the bilateral minerals partnership.'),
    ('European Bank for Reconstruction and Development (EBRD)', 'Finance / Development', 'UK', 'London', 'Margaret O''Brien', 'Director, Climate Investment', '2026-06-02', 'Neutral', 'Multilateral development bank financing energy and minerals projects across emerging Europe and North Africa. Potential co-financier for allied supply-chain projects.'),
    ('African Development Bank (AfDB)', 'Finance / Development', 'Côte d''Ivoire', 'Abidjan', 'Dr. James Achebe', 'Director, Natural Resources', '2026-04-18', 'Neutral', 'Continental development bank financing African minerals and agriculture. Relevant to both critical-minerals sourcing and food-security development tracks.'),
    ('Global Battery Alliance', 'Critical Minerals / Standards', 'Switzerland', 'Geneva', 'Dr. Layla Hassan', 'Executive Director', '2026-07-19', 'Warm', 'WEF-linked multi-stakeholder coalition setting responsible battery supply-chain standards. A useful convening body for the Ministerial coalition.'),
    ('TotalEnergies (Italy office)', 'Energy / Minerals', 'France', 'Rome (Italy)', 'Jean-Pierre Lamartine', 'Country Manager Italy', '2026-05-22', 'Neutral', 'French energy major with Italian operations spanning renewables and battery-storage ventures. Engagement is transactional but constructive.'),
    ('Bayer CropScience (Rome/FAO liaison)', 'Agriculture / Food Security', 'Germany', 'Rome (FAO liaison)', 'Dr. Ingrid Hoffmann', 'FAO Liaison Lead', '2026-08-01', 'Warm', 'Agricultural-science division maintaining a dedicated FAO liaison in Rome on crop innovation and food security. Aligned with private-sector accountability messaging.');

-- =============================================================================
-- TABLE 2: CRM_ACTIVITY_LOG
-- =============================================================================
INSERT INTO CRM_ACTIVITY_LOG
    (activity_id, org_name, activity_type, activity_date, summary, participants, classification)
VALUES
    -- Enel Green Power
    (1, 'Enel Green Power', 'Meeting', '2025-06-17', 'Ambassador hosted Enel leadership to discuss grid-scale storage and allied battery-materials sourcing.', 'Amb. Blanchard, Maria Rossi, Alessandro Corsi', 'Significant'),
    (2, 'Enel Green Power', 'Cable', '2025-07-09', 'Cable to Washington summarizing Enel''s interest in DFC-backed lithium offtake structures.', 'Econ Section, State/EB', 'Significant'),
    (3, 'Enel Green Power', 'Call', '2025-09-22', 'DCM call with VP Government Affairs to confirm Ministerial participation.', 'DCM Harmon, Maria Rossi', 'Routine'),
    (4, 'Enel Green Power', 'Event', '2026-02-11', 'Enel CEO delivered keynote at the Critical Minerals Ministerial in Rome.', 'Amb. Blanchard, Alessandro Corsi, Dr. Isabella Moretti', 'High-Priority'),
    (5, 'Enel Green Power', 'Email', '2026-05-04', 'Policy staff exchanged terms on a proposed U.S.-Italy storage pilot memo.', 'Econ Officer Vance, Maria Rossi', 'Routine'),
    (6, 'Enel Green Power', 'Meeting', '2026-08-12', 'Follow-up on storage pilot and readout of Enel''s North America investment plans.', 'DCM Harmon, Maria Rossi', 'Significant'),
    (7, 'Enel Green Power', 'Call', '2026-08-27', 'Coordination call ahead of the Rome critical-minerals summit attendee finalization.', 'Econ Section, Maria Rossi', 'Routine'),

    -- ENI S.p.A.
    (8, 'ENI S.p.A.', 'Meeting', '2025-06-25', 'Initial engagement with ENI EU Affairs on critical-minerals adjacencies to its energy portfolio.', 'Econ Counselor, Roberto Ferretti', 'Routine'),
    (9, 'ENI S.p.A.', 'Cable', '2025-08-14', 'Reporting cable assessing ENI''s guarded posture toward U.S. supply-chain frameworks.', 'Econ Section, State/EB', 'Significant'),
    (10, 'ENI S.p.A.', 'Call', '2025-11-06', 'Call on ENI''s North Africa upstream footprint and phosphate adjacencies.', 'Econ Officer Vance, Roberto Ferretti', 'Routine'),
    (11, 'ENI S.p.A.', 'Meeting', '2026-03-19', 'Discussion of ENI role in bilateral energy-partnership deliverables.', 'DCM Harmon, Roberto Ferretti', 'Significant'),
    (12, 'ENI S.p.A.', 'Email', '2026-06-28', 'Exchange on ENI participation in Italian G7 energy follow-up workstream.', 'Econ Section, Roberto Ferretti', 'Routine'),
    (13, 'ENI S.p.A.', 'Event', '2026-07-15', 'ENI representatives attended Mission-hosted energy-security roundtable.', 'DCM Harmon, Roberto Ferretti, Terna reps', 'Routine'),

    -- APSA (Vatican Investments)
    (14, 'APSA (Vatican Investments)', 'Meeting', '2025-07-02', 'Discreet meeting on ethical-investment screening and AI-ethics finance principles.', 'Amb. Blanchard, Msgr. Pietro Conti', 'Significant'),
    (15, 'APSA (Vatican Investments)', 'Cable', '2025-10-17', 'Cable analyzing APSA''s ethics-driven investment mandate and diplomatic openings.', 'Pol Section, State/IO', 'Significant'),
    (16, 'APSA (Vatican Investments)', 'Call', '2026-01-28', 'Call to coordinate Vatican participation in AI-ethics dialogue series.', 'Pol Officer Reyes, Msgr. Pietro Conti', 'Routine'),
    (17, 'APSA (Vatican Investments)', 'Meeting', '2026-04-09', 'Substantive exchange on responsible-finance alignment with U.S. AI leadership agenda.', 'Amb. Blanchard, Msgr. Pietro Conti', 'High-Priority'),
    (18, 'APSA (Vatican Investments)', 'Email', '2026-07-09', 'Correspondence confirming next Rome Call working-session dates.', 'Pol Section, Msgr. Pietro Conti', 'Routine'),
    (19, 'APSA (Vatican Investments)', 'Event', '2026-07-28', 'APSA Secretary attended Rome Call for AI Ethics anniversary convening.', 'Amb. Blanchard, Bishop Vincenzo Paglia, Msgr. Pietro Conti', 'Significant'),

    -- Vulcan Energy Resources
    (20, 'Vulcan Energy Resources', 'Meeting', '2025-07-30', 'Technical briefing on Vulcan''s zero-carbon lithium process as an allied-processing option.', 'Econ Counselor, Dr. Marco Van der Berg', 'Significant'),
    (21, 'Vulcan Energy Resources', 'Cable', '2025-12-03', 'Cable recommending Vulcan for DFC-backed offtake evaluation.', 'Econ Section, State/EB, DFC', 'Significant'),
    (22, 'Vulcan Energy Resources', 'Event', '2026-08-05', 'Vulcan CTO presented at Rome minerals-processing technical session.', 'Econ Officer Vance, Dr. Marco Van der Berg', 'Routine'),

    -- Albemarle Corporation
    (23, 'Albemarle Corporation', 'Meeting', '2025-06-11', 'Strategy session on Ministerial coalition-building and priority-materials framing.', 'Amb. Blanchard, Thomas Whitmore', 'High-Priority'),
    (24, 'Albemarle Corporation', 'Cable', '2025-09-01', 'Cable coordinating Albemarle input into the Critical Minerals Strategy 2026 draft.', 'Econ Section, State/EB', 'Significant'),
    (25, 'Albemarle Corporation', 'Call', '2025-11-20', 'Call on lithium market outlook and Chinese-supply exposure metrics.', 'Econ Officer Vance, Thomas Whitmore', 'Routine'),
    (26, 'Albemarle Corporation', 'Event', '2026-02-11', 'Albemarle VP joined Ministerial industry panel on allied offtake financing.', 'Amb. Blanchard, Thomas Whitmore', 'High-Priority'),
    (27, 'Albemarle Corporation', 'Email', '2026-04-27', 'Exchange finalizing joint messaging on the 50%-reduction defense target.', 'Econ Section, Thomas Whitmore', 'Significant'),
    (28, 'Albemarle Corporation', 'Meeting', '2026-07-22', 'Review of DFC pipeline projects and allied-nation bilateral agreement status.', 'DCM Harmon, Thomas Whitmore', 'Significant'),
    (29, 'Albemarle Corporation', 'Call', '2026-08-19', 'Pre-summit coordination on delegation and speaking roles.', 'Econ Section, Thomas Whitmore', 'Routine'),

    -- Yara International
    (30, 'Yara International', 'Meeting', '2025-06-19', 'Discussion bridging phosphate/potash minerals interests with FAO food-security agenda.', 'Econ Counselor, Helena Svensson', 'Significant'),
    (31, 'Yara International', 'Cable', '2025-08-28', 'Cable on Yara''s role linking fertilizer supply resilience to food security.', 'Econ Section, State/EB', 'Routine'),
    (32, 'Yara International', 'Event', '2025-10-14', 'Yara delegate attended FAO Committee on World Food Security side event.', 'Econ Officer Vance, Helena Svensson', 'Routine'),
    (33, 'Yara International', 'Call', '2026-02-24', 'Call on fertilizer-market disruptions and Ministerial phosphate discussion.', 'Econ Section, Helena Svensson', 'Routine'),
    (34, 'Yara International', 'Email', '2026-05-30', 'Correspondence on Yara input to food-security accountability messaging.', 'Econ Section, Helena Svensson', 'Routine'),
    (35, 'Yara International', 'Meeting', '2026-07-31', 'Review of Yara-FAO private-sector engagement and U.S. priorities.', 'DCM Harmon, Helena Svensson, Prof. Anna Kessler', 'Significant'),

    -- Cargill International (Rome)
    (36, 'Cargill International (Rome)', 'Meeting', '2025-06-30', 'Strategic session on private-sector anchoring of WFP and FAO reform efforts.', 'Amb. Blanchard, James O''Connor', 'High-Priority'),
    (37, 'Cargill International (Rome)', 'Cable', '2025-09-16', 'Cable summarizing Cargill perspective on Rome-agency efficiency gaps.', 'Econ Section, State/IO', 'Significant'),
    (38, 'Cargill International (Rome)', 'Call', '2025-12-10', 'Call on supply-chain traceability pilots relevant to WFP procurement.', 'Econ Officer Vance, James O''Connor', 'Routine'),
    (39, 'Cargill International (Rome)', 'Event', '2026-03-05', 'Cargill co-hosted food-security private-sector forum with the Mission.', 'DCM Harmon, James O''Connor, Prof. Anna Kessler', 'Significant'),
    (40, 'Cargill International (Rome)', 'Email', '2026-06-12', 'Exchange on data-sharing terms for WFP accountability metrics.', 'Econ Section, James O''Connor', 'Routine'),
    (41, 'Cargill International (Rome)', 'Meeting', '2026-08-18', 'Readout on Cargill''s alignment with the accountability mandate deliverables.', 'Amb. Blanchard, James O''Connor', 'High-Priority'),

    -- OCP Group
    (42, 'OCP Group', 'Meeting', '2025-07-21', 'Introductory meeting on phosphate supply and food-security linkages.', 'Econ Counselor, Hamid Benali', 'Routine'),
    (43, 'OCP Group', 'Cable', '2025-10-30', 'Cable assessing OCP''s neutral posture and Morocco supply-chain leverage.', 'Econ Section, State/EB', 'Significant'),
    (44, 'OCP Group', 'Call', '2026-03-11', 'Call on OCP participation in the Ministerial phosphates discussion.', 'Econ Officer Vance, Hamid Benali', 'Routine'),

    -- Barrick Gold (Italy)
    (45, 'Barrick Gold (Italy)', 'Cable', '2025-08-05', 'Cable noting Barrick''s cautious EU permitting posture and cooled engagement.', 'Econ Section, State/EB', 'Routine'),
    (46, 'Barrick Gold (Italy)', 'Call', '2026-01-19', 'Call to reassess engagement given EU regulatory exposure.', 'Econ Officer Vance, Lucia Fernandez', 'Routine'),

    -- Breakthrough Energy Europe
    (47, 'Breakthrough Energy Europe', 'Meeting', '2025-09-09', 'Discussion of minerals-innovation financing and allied co-investment vehicles.', 'Econ Counselor, Sophie Laurent', 'Significant'),
    (48, 'Breakthrough Energy Europe', 'Event', '2026-02-11', 'Breakthrough MD participated in Ministerial financing panel.', 'DCM Harmon, Sophie Laurent', 'Significant'),
    (49, 'Breakthrough Energy Europe', 'Email', '2026-06-15', 'Exchange on convening allied financiers for supply-chain projects.', 'Econ Section, Sophie Laurent', 'Routine'),

    -- FAO Private Sector Advisory Group
    (50, 'FAO Private Sector Advisory Group', 'Meeting', '2025-06-13', 'Engagement on private-sector reform messaging within FAO governance.', 'Amb. Blanchard, Prof. Anna Kessler', 'High-Priority'),
    (51, 'FAO Private Sector Advisory Group', 'Cable', '2025-08-22', 'Cable on advancing accountability and efficiency themes via the advisory group.', 'Econ Section, State/IO', 'Significant'),
    (52, 'FAO Private Sector Advisory Group', 'Event', '2025-11-18', 'PSAG chaired session at FAO Council with U.S. observer participation.', 'DCM Harmon, Prof. Anna Kessler', 'Significant'),
    (53, 'FAO Private Sector Advisory Group', 'Call', '2026-01-30', 'Call to coordinate PSAG input on FAO reform recommendations.', 'Econ Officer Vance, Prof. Anna Kessler', 'Routine'),
    (54, 'FAO Private Sector Advisory Group', 'Email', '2026-05-08', 'Exchange on demonstrating taxpayer return-on-investment framing.', 'Econ Section, Prof. Anna Kessler', 'Significant'),
    (55, 'FAO Private Sector Advisory Group', 'Meeting', '2026-07-24', 'Substantive review of FAO governance-reform trajectory.', 'Amb. Blanchard, Prof. Anna Kessler', 'High-Priority'),
    (56, 'FAO Private Sector Advisory Group', 'Meeting', '2026-08-20', 'Final coordination on PSAG deliverables ahead of Governing Bodies.', 'DCM Harmon, Prof. Anna Kessler', 'Significant'),

    -- World Resources Institute Rome
    (57, 'World Resources Institute Rome', 'Meeting', '2025-07-16', 'Analytical exchange on minerals, land use, and food-system data.', 'Econ Counselor, Dr. Maria Gonzalez', 'Routine'),
    (58, 'World Resources Institute Rome', 'Email', '2025-12-02', 'Correspondence sharing open-source analysis on lithium supply chains.', 'Econ Section, Dr. Maria Gonzalez', 'Routine'),
    (59, 'World Resources Institute Rome', 'Call', '2026-07-03', 'Call on WRI environmental-policy inputs to Ministerial follow-up.', 'Econ Officer Vance, Dr. Maria Gonzalez', 'Routine'),

    -- IFAD
    (60, 'IFAD', 'Meeting', '2025-06-24', 'Engagement on IFAD rural-development financing and U.S. accountability review.', 'DCM Harmon, Dr. Amara Diallo', 'Significant'),
    (61, 'IFAD', 'Cable', '2025-10-08', 'Cable reporting IFAD review findings on program efficiency.', 'Econ Section, State/IO', 'High-Priority'),
    (62, 'IFAD', 'Event', '2026-02-27', 'U.S. delegation attended IFAD Governing Council session.', 'DCM Harmon, Dr. Amara Diallo', 'Significant'),
    (63, 'IFAD', 'Call', '2026-06-16', 'Call on IFAD reform commitments and West Africa program metrics.', 'Econ Officer Vance, Dr. Amara Diallo', 'Routine'),
    (64, 'IFAD', 'Meeting', '2026-08-08', 'Review of IFAD accountability posture within Rome-agency mandate.', 'DCM Harmon, Dr. Amara Diallo', 'Significant'),

    -- WFP
    (65, 'WFP', 'Meeting', '2025-06-05', 'Ambassador engagement with WFP leadership on operational efficiency and overhead.', 'Amb. Blanchard, Fatima Al-Rashid', 'High-Priority'),
    (66, 'WFP', 'Cable', '2025-09-25', 'Cable documenting concern over 23% administrative overhead vs sub-18% target.', 'Econ Section, State/IO', 'High-Priority'),
    (67, 'WFP', 'Call', '2025-12-15', 'Call on duplication between WFP school meals and FAO nutrition initiatives.', 'Econ Officer Vance, Fatima Al-Rashid', 'Significant'),
    (68, 'WFP', 'Cable', '2026-01-14', 'WFP Accountability Review cable recommending 15% contribution withhold pending reform.', 'Amb. Blanchard, State/IO', 'High-Priority'),
    (69, 'WFP', 'Event', '2026-04-15', 'U.S. delegation intervened at WFP Executive Board on reform plan.', 'DCM Harmon, Fatima Al-Rashid', 'High-Priority'),
    (70, 'WFP', 'Meeting', '2026-06-30', 'Review of WFP reform-plan progress against efficiency targets.', 'Amb. Blanchard, Fatima Al-Rashid', 'Significant'),
    (71, 'WFP', 'Meeting', '2026-08-25', 'Status meeting on contribution conditionality and overhead trajectory.', 'Amb. Blanchard, Fatima Al-Rashid', 'High-Priority'),

    -- Leonardo S.p.A.
    (72, 'Leonardo S.p.A.', 'Meeting', '2025-08-19', 'Engagement on secure supply chains for defense-critical materials.', 'DCM Harmon, Gen. (ret.) Paolo Bianchi', 'Significant'),
    (73, 'Leonardo S.p.A.', 'Cable', '2025-11-27', 'Cable on Leonardo interest in U.S.-Italy industrial minerals cooperation.', 'Pol-Mil Section, State/PM', 'Routine'),
    (74, 'Leonardo S.p.A.', 'Call', '2026-06-05', 'Call on bilateral industrial track and materials-security framing.', 'Pol-Mil Officer, Gen. (ret.) Paolo Bianchi', 'Routine'),

    -- Terna S.p.A.
    (75, 'Terna S.p.A.', 'Meeting', '2025-07-11', 'Discussion of grid modernization and storage integration for the bilateral track.', 'Econ Counselor, Dott.ssa Elena Costa', 'Routine'),
    (76, 'Terna S.p.A.', 'Email', '2026-01-22', 'Exchange on regulatory framework for cross-border storage projects.', 'Econ Section, Dott.ssa Elena Costa', 'Routine'),
    (77, 'Terna S.p.A.', 'Meeting', '2026-07-14', 'Review of Terna role in U.S.-Italy energy-partnership deliverables.', 'DCM Harmon, Dott.ssa Elena Costa', 'Significant'),

    -- SQM
    (78, 'SQM (Sociedad Quimica y Minera)', 'Meeting', '2025-09-04', 'Engagement on Chilean lithium supply as an allied-nation diversification source.', 'Econ Counselor, Carlos Matos', 'Significant'),
    (79, 'SQM (Sociedad Quimica y Minera)', 'Cable', '2025-12-19', 'Cable assessing SQM offtake potential and Chile policy environment.', 'Econ Section, State/EB', 'Routine'),
    (80, 'SQM (Sociedad Quimica y Minera)', 'Call', '2026-05-12', 'Call on SQM participation in Ministerial coalition activities.', 'Econ Officer Vance, Carlos Matos', 'Routine'),

    -- BASF SE
    (81, 'BASF SE', 'Meeting', '2025-08-26', 'Engagement on cathode-materials capacity and allied battery supply chains.', 'Econ Counselor, Dr. Klaus Weber', 'Significant'),
    (82, 'BASF SE', 'Email', '2026-02-05', 'Exchange on BASF interest in transatlantic battery-materials frameworks.', 'Econ Section, Dr. Klaus Weber', 'Routine'),
    (83, 'BASF SE', 'Call', '2026-06-20', 'Call on European processing-capacity buildout and offtake terms.', 'Econ Officer Vance, Dr. Klaus Weber', 'Routine'),

    -- Pontifical Academy for Life
    (84, 'Pontifical Academy for Life', 'Meeting', '2025-07-08', 'Engagement on Rome Call for AI Ethics and U.S. AI-leadership alignment.', 'Amb. Blanchard, Bishop Vincenzo Paglia', 'High-Priority'),
    (85, 'Pontifical Academy for Life', 'Cable', '2025-11-20', 'Cable analyzing Vatican AI-ethics positions relative to EO 14179 narrative.', 'Pol Section, State/OES', 'Significant'),
    (86, 'Pontifical Academy for Life', 'Event', '2025-11-15', 'Mission observed the updated Rome Call for AI Ethics signing.', 'Amb. Blanchard, Bishop Vincenzo Paglia', 'Significant'),
    (87, 'Pontifical Academy for Life', 'Meeting', '2026-07-28', 'Substantive session on AI governance and technology-alignment messaging.', 'Amb. Blanchard, Bishop Vincenzo Paglia', 'High-Priority'),

    -- Italian Ministry of Environment (MASE)
    (88, 'Italian Ministry of Environment (MASE)', 'Meeting', '2025-06-16', 'Lead government engagement on Italy''s critical-materials policy.', 'Amb. Blanchard, Dr. Isabella Moretti', 'High-Priority'),
    (89, 'Italian Ministry of Environment (MASE)', 'Cable', '2025-10-03', 'Cable on MASE alignment with EU Critical Raw Materials Act implementation.', 'Econ Section, State/EB', 'Significant'),
    (90, 'Italian Ministry of Environment (MASE)', 'Event', '2026-02-11', 'MASE Director co-chaired the Critical Minerals Ministerial in Rome.', 'Amb. Blanchard, Dr. Isabella Moretti', 'High-Priority'),
    (91, 'Italian Ministry of Environment (MASE)', 'Call', '2026-06-09', 'Call on bilateral minerals-partnership deliverables and G7 follow-up.', 'Econ Counselor, Dr. Isabella Moretti', 'Significant'),
    (92, 'Italian Ministry of Environment (MASE)', 'Meeting', '2026-08-10', 'Review of bilateral partnership progress and joint project pipeline.', 'DCM Harmon, Dr. Isabella Moretti', 'Significant'),

    -- EBRD
    (93, 'European Bank for Reconstruction and Development (EBRD)', 'Meeting', '2025-09-11', 'Engagement on EBRD co-financing for allied minerals projects in emerging Europe.', 'Econ Counselor, Margaret O''Brien', 'Routine'),
    (94, 'European Bank for Reconstruction and Development (EBRD)', 'Email', '2026-01-15', 'Exchange on EBRD climate-investment pipeline and DFC coordination.', 'Econ Section, Margaret O''Brien', 'Routine'),
    (95, 'European Bank for Reconstruction and Development (EBRD)', 'Call', '2026-06-02', 'Call on potential co-financing for a North Africa processing project.', 'Econ Officer Vance, Margaret O''Brien', 'Routine'),

    -- AfDB
    (96, 'African Development Bank (AfDB)', 'Meeting', '2025-08-12', 'Engagement on African minerals financing and food-security development.', 'Econ Counselor, Dr. James Achebe', 'Routine'),
    (97, 'African Development Bank (AfDB)', 'Cable', '2025-12-08', 'Cable on AfDB natural-resources portfolio and U.S. engagement options.', 'Econ Section, State/AF', 'Routine'),
    (98, 'African Development Bank (AfDB)', 'Call', '2026-04-18', 'Call on AfDB role in critical-minerals sourcing partnerships.', 'Econ Officer Vance, Dr. James Achebe', 'Routine'),

    -- Global Battery Alliance
    (99, 'Global Battery Alliance', 'Meeting', '2025-07-24', 'Engagement on responsible battery supply-chain standards for the coalition.', 'Econ Counselor, Dr. Layla Hassan', 'Significant'),
    (100, 'Global Battery Alliance', 'Event', '2026-02-11', 'GBA presented battery-passport standards at the Ministerial.', 'DCM Harmon, Dr. Layla Hassan', 'Significant'),
    (101, 'Global Battery Alliance', 'Email', '2026-07-19', 'Exchange on aligning GBA standards with allied procurement criteria.', 'Econ Section, Dr. Layla Hassan', 'Routine'),

    -- TotalEnergies (Italy office)
    (102, 'TotalEnergies (Italy office)', 'Meeting', '2025-09-18', 'Engagement on TotalEnergies renewables and storage ventures in Italy.', 'Econ Counselor, Jean-Pierre Lamartine', 'Routine'),
    (103, 'TotalEnergies (Italy office)', 'Call', '2026-02-13', 'Call on battery-storage project interest and bilateral relevance.', 'Econ Officer Vance, Jean-Pierre Lamartine', 'Routine'),
    (104, 'TotalEnergies (Italy office)', 'Email', '2026-05-22', 'Exchange on TotalEnergies participation in energy-security roundtable.', 'Econ Section, Jean-Pierre Lamartine', 'Routine'),

    -- Bayer CropScience (Rome/FAO liaison)
    (105, 'Bayer CropScience (Rome/FAO liaison)', 'Meeting', '2025-08-07', 'Engagement on crop-innovation and food-security private-sector messaging.', 'Econ Counselor, Dr. Ingrid Hoffmann', 'Routine'),
    (106, 'Bayer CropScience (Rome/FAO liaison)', 'Event', '2025-10-21', 'Bayer liaison joined FAO private-sector forum on digital agriculture.', 'Econ Officer Vance, Dr. Ingrid Hoffmann', 'Routine'),
    (107, 'Bayer CropScience (Rome/FAO liaison)', 'Cable', '2026-03-27', 'Cable on Bayer alignment with accountability and efficiency framing at FAO.', 'Econ Section, State/IO', 'Routine'),
    (108, 'Bayer CropScience (Rome/FAO liaison)', 'Meeting', '2026-08-01', 'Review of Bayer-FAO liaison activity and U.S. priorities.', 'Econ Counselor, Dr. Ingrid Hoffmann', 'Routine');

-- =============================================================================
-- TABLE 3: SECTOR_INTELLIGENCE
-- =============================================================================
INSERT INTO SECTOR_INTELLIGENCE
    (intel_id, org_name, intel_type, intel_date, headline, summary, source, relevance_score)
VALUES
    (1, 'Enel Green Power', 'News', '2025-07-15', 'Enel unveils grid-scale storage expansion across Southern Italy', 'Enel Green Power announced a multi-gigawatt battery-storage buildout tied to renewable capacity. The plan increases demand for allied-sourced lithium and positions Enel as a bilateral partner.', 'Reuters', 82),
    (2, 'Enel Green Power', 'Ministerial', '2026-02-12', 'Enel CEO headlines Critical Minerals Ministerial in Rome', 'Enel''s CEO delivered a keynote endorsing allied-nation offtake financing at the Rome Ministerial. Remarks aligned closely with U.S. supply-chain diversification messaging.', 'State Dept Cable', 90),
    (3, 'Enel Green Power', 'Partnership', '2026-05-20', 'Enel explores U.S. storage pilot with DFC backing', 'Reports indicate Enel is evaluating a U.S.-Italy storage pilot supported by development financing. The initiative would deepen the bilateral energy track.', 'Trade Press', 78),

    (4, 'ENI S.p.A.', 'News', '2025-08-30', 'ENI signals cautious approach to U.S. minerals frameworks', 'ENI leadership publicly emphasized commercial neutrality on Western supply-chain blocs. Analysts read the posture as hedging between EU, U.S., and North African interests.', 'Bloomberg', 68),
    (5, 'ENI S.p.A.', 'Regulatory', '2026-03-22', 'ENI adjusts strategy under EU Critical Raw Materials Act', 'ENI outlined compliance plans for the CRMA, including reporting on strategic-material adjacencies. The move opens dialogue on U.S.-EU alignment.', 'EU Monitor', 71),

    (6, 'APSA (Vatican Investments)', 'Analysis', '2025-10-20', 'Vatican investment arm tightens ethical screening', 'APSA reportedly expanded ethical-investment screens to cover AI and surveillance technologies. The shift reinforces Vatican leadership on responsible finance.', 'Vatican Press Office', 74),
    (7, 'APSA (Vatican Investments)', 'Partnership', '2026-04-11', 'APSA signals interest in responsible-AI finance dialogue', 'APSA indicated willingness to engage U.S. counterparts on AI-ethics-aligned investment principles. The opening supports the Mission''s AI-diplomacy objectives.', 'State Dept Cable', 80),

    (8, 'Vulcan Energy Resources', 'News', '2025-11-04', 'Vulcan advances zero-carbon lithium at commercial scale', 'Vulcan Energy reported progress on its geothermal-lithium process in Germany. The company is increasingly cited as an allied alternative to Chinese processing.', 'Trade Press', 85),
    (9, 'Vulcan Energy Resources', 'Analysis', '2026-06-10', 'Analysts flag Vulcan as prime DFC offtake candidate', 'A supply-chain analysis identified Vulcan as a leading candidate for U.S.-backed offtake. The assessment cites process economics and EU location.', 'CSIS', 83),

    (10, 'Albemarle Corporation', 'News', '2025-09-02', 'Albemarle expands lithium capacity amid price volatility', 'Albemarle announced capacity investments despite soft lithium prices, betting on defense and EV demand. The move underpins U.S. diversification goals.', 'Bloomberg', 84),
    (11, 'Albemarle Corporation', 'Ministerial', '2026-02-12', 'Albemarle backs 50% China-reduction defense target at Ministerial', 'Albemarle publicly endorsed the U.S. goal to halve Chinese-sourced defense minerals by 2030. The endorsement strengthened coalition messaging.', 'State Dept Cable', 91),
    (12, 'Albemarle Corporation', 'Partnership', '2026-07-25', 'Albemarle joins allied offtake financing consortium', 'Albemarle reportedly joined a consortium structuring DFC-backed offtake for allied projects. The step operationalizes the Critical Minerals Strategy.', 'Trade Press', 86),

    (13, 'Yara International', 'News', '2025-08-28', 'Yara warns of fertilizer-supply fragility amid geopolitics', 'Yara flagged risks to global fertilizer supply from energy and phosphate disruptions. The warning links minerals security to food security.', 'Reuters', 76),
    (14, 'Yara International', 'Analysis', '2026-02-25', 'Phosphate access rises on Ministerial agenda', 'Analysts noted growing attention to phosphate supply at the Rome Ministerial, with Yara among key voices. Food-security framing gained traction.', 'FAO Press', 72),

    (15, 'Cargill International (Rome)', 'Analysis', '2025-09-18', 'Cargill data cited in WFP procurement-efficiency debate', 'Cargill supply-chain data featured in discussions on WFP procurement inefficiencies. The private-sector benchmark reinforced U.S. accountability arguments.', 'State Dept Cable', 82),
    (16, 'Cargill International (Rome)', 'Partnership', '2026-03-06', 'Cargill co-hosts food-security private-sector forum in Rome', 'Cargill partnered with the Mission on a forum linking industry to Rome-agency reform. The event advanced return-on-investment messaging.', 'FAO Press', 79),
    (17, 'Cargill International (Rome)', 'News', '2026-08-19', 'Cargill pilots traceability tools relevant to aid delivery', 'Cargill announced traceability pilots that could improve accountability in humanitarian food procurement. WFP is a potential adopter.', 'Trade Press', 77),

    (18, 'OCP Group', 'News', '2025-10-31', 'OCP leverages phosphate dominance amid supply concerns', 'OCP emphasized its central role in global phosphate supply during a period of tight markets. Morocco''s leverage shapes food-security diplomacy.', 'Bloomberg', 70),
    (19, 'OCP Group', 'Ministerial', '2026-02-12', 'OCP participates in Ministerial phosphates session', 'OCP joined a Ministerial discussion on phosphate supply resilience. Engagement remained neutral but constructive.', 'State Dept Cable', 66),

    (20, 'Barrick Gold (Italy)', 'Regulatory', '2025-08-06', 'Barrick faces EU permitting headwinds', 'Barrick flagged permitting delays affecting European-linked projects under tightening EU rules. The friction cooled its engagement posture.', 'EU Monitor', 58),
    (21, 'Barrick Gold (Italy)', 'News', '2026-01-20', 'Barrick reassesses European government-affairs footprint', 'Barrick signaled a leaner EU engagement strategy amid regulatory uncertainty. Analysts see reduced near-term diplomatic activity.', 'Trade Press', 55),

    (22, 'Breakthrough Energy Europe', 'Partnership', '2025-09-10', 'Breakthrough targets minerals-innovation financing in Europe', 'Breakthrough Energy Europe outlined funds for critical-minerals and storage innovation. The vehicle could co-finance allied supply-chain projects.', 'Trade Press', 75),
    (23, 'Breakthrough Energy Europe', 'Ministerial', '2026-02-12', 'Breakthrough MD joins Ministerial financing panel', 'Breakthrough''s managing director discussed blended finance for allied minerals at the Ministerial. The intervention supported coalition financing goals.', 'State Dept Cable', 78),

    (24, 'FAO Private Sector Advisory Group', 'Ministerial', '2025-11-18', 'PSAG presses FAO governance-reform agenda at Council', 'The FAO PSAG advanced reform themes at the FAO Council, emphasizing efficiency and private-sector accountability. U.S. observers welcomed the momentum.', 'FAO Press', 84),
    (25, 'FAO Private Sector Advisory Group', 'Analysis', '2026-05-09', 'PSAG frames taxpayer return-on-investment for FAO programs', 'A PSAG paper articulated return-on-investment metrics for donor contributions. The framing aligns with the America First accountability mandate.', 'State Dept Cable', 88),
    (26, 'FAO Private Sector Advisory Group', 'News', '2026-08-21', 'PSAG finalizes reform recommendations ahead of Governing Bodies', 'The PSAG completed a set of reform recommendations for FAO Governing Bodies. Recommendations stress efficiency and duplication reduction.', 'FAO Press', 85),

    (27, 'World Resources Institute Rome', 'Analysis', '2025-12-03', 'WRI report maps lithium supply-chain concentration risks', 'A WRI Rome analysis mapped concentration risk in lithium processing. Findings inform allied diversification strategy.', 'WRI', 73),
    (28, 'World Resources Institute Rome', 'News', '2026-07-04', 'WRI publishes food-system land-use assessment for Med region', 'WRI released a Mediterranean land-use and food-system assessment relevant to FAO programming. The report offers open-source intelligence.', 'Trade Press', 64),

    (29, 'IFAD', 'Analysis', '2025-10-09', 'IFAD program-efficiency review surfaces overhead concerns', 'A review of IFAD rural-development programs highlighted efficiency gaps. U.S. reporting flagged accountability implications.', 'State Dept Cable', 81),
    (30, 'IFAD', 'Ministerial', '2026-02-28', 'IFAD Governing Council debates reform commitments', 'IFAD''s Governing Council took up reform and efficiency commitments. The U.S. delegation pressed for measurable metrics.', 'FAO Press', 79),
    (31, 'IFAD', 'News', '2026-08-09', 'IFAD signals West Africa program metric improvements', 'IFAD reported progress on West Africa program metrics tied to reform pledges. Verification remains a U.S. priority.', 'Trade Press', 72),

    (32, 'WFP', 'Analysis', '2025-09-26', 'WFP administrative overhead reaches 23%, above donor targets', 'Analysis showed WFP administrative overhead at 23%, well above the sub-18% donor benchmark. The figure anchors U.S. reform demands.', 'State Dept Cable', 92),
    (33, 'WFP', 'News', '2025-12-16', 'Overlap between WFP and FAO nutrition programs draws scrutiny', 'Reports highlighted duplication between WFP school-meals and FAO nutrition initiatives. Consolidation is under discussion.', 'Reuters', 84),
    (34, 'WFP', 'Regulatory', '2026-04-16', 'U.S. floats contribution conditionality at WFP Executive Board', 'The U.S. delegation signaled possible conditioning of contributions on a reform plan at the Executive Board. The intervention raised the stakes on efficiency.', 'State Dept Cable', 93),
    (35, 'WFP', 'News', '2026-08-26', 'WFP publishes interim reform plan amid donor pressure', 'WFP released an interim reform plan targeting overhead reduction. Donors, including the U.S., are assessing adequacy.', 'Bloomberg', 89),

    (36, 'Leonardo S.p.A.', 'News', '2025-11-28', 'Leonardo seeks secure sourcing for defense-critical materials', 'Leonardo emphasized supply security for defense-critical minerals amid geopolitical risk. The stance supports U.S.-Italy industrial cooperation.', 'Trade Press', 69),
    (37, 'Leonardo S.p.A.', 'Partnership', '2026-06-06', 'Leonardo explores U.S.-Italy materials-security cooperation', 'Leonardo signaled interest in bilateral cooperation on materials security. Talks feed the industrial track of the partnership.', 'State Dept Cable', 71),

    (38, 'Terna S.p.A.', 'Regulatory', '2026-01-23', 'Terna updates rules for cross-border storage integration', 'Terna proposed regulatory changes to accommodate storage integration on the Italian grid. The reform aids bilateral storage projects.', 'EU Monitor', 67),
    (39, 'Terna S.p.A.', 'News', '2026-07-15', 'Terna advances grid-modernization plan tied to renewables', 'Terna announced grid-modernization investments enabling higher renewable penetration. Storage demand supports minerals-sourcing objectives.', 'Trade Press', 65),

    (40, 'SQM (Sociedad Quimica y Minera)', 'News', '2025-12-20', 'SQM expands lithium output for allied markets', 'SQM outlined output expansion oriented toward diversified allied buyers. Chile remains a key diversification source.', 'Bloomberg', 80),
    (41, 'SQM (Sociedad Quimica y Minera)', 'Regulatory', '2026-05-13', 'Chile policy shifts shape SQM export outlook', 'Chilean policy changes on lithium governance affected SQM''s export planning. Analysts weigh implications for allied offtake.', 'Reuters', 74),

    (42, 'BASF SE', 'News', '2025-08-27', 'BASF scales cathode-materials capacity in Europe', 'BASF advanced cathode-materials production in Europe, strengthening allied battery supply. The buildout is relevant to transatlantic frameworks.', 'Bloomberg', 79),
    (43, 'BASF SE', 'Partnership', '2026-06-21', 'BASF weighs transatlantic battery-materials collaboration', 'BASF signaled openness to transatlantic collaboration on battery materials. Talks could yield allied processing capacity.', 'Trade Press', 76),

    (44, 'Pontifical Academy for Life', 'Ministerial', '2025-11-16', 'Updated Rome Call for AI Ethics gains new signatories', 'The Pontifical Academy renewed the Rome Call for AI Ethics with additional corporate and academic signatories. The declaration shapes global AI norms.', 'Vatican Press Office', 86),
    (45, 'Pontifical Academy for Life', 'Analysis', '2026-07-29', 'Vatican AI-ethics stance intersects U.S. leadership narrative', 'Analysis examined overlaps between Vatican AI-ethics principles and the U.S. AI-leadership agenda. Alignment opportunities were noted alongside tensions on binding governance.', 'State Dept Cable', 83),

    (46, 'Italian Ministry of Environment (MASE)', 'Regulatory', '2025-10-04', 'MASE implements EU Critical Raw Materials Act provisions', 'MASE moved to implement CRMA provisions on strategic-material projects. The steps create openings for bilateral cooperation.', 'EU Monitor', 82),
    (47, 'Italian Ministry of Environment (MASE)', 'Ministerial', '2026-02-12', 'MASE co-chairs Critical Minerals Ministerial in Rome', 'MASE''s critical-materials director co-chaired the Rome Ministerial. Italian leadership reinforced the bilateral partnership.', 'State Dept Cable', 90),
    (48, 'Italian Ministry of Environment (MASE)', 'News', '2026-08-11', 'MASE outlines domestic critical-materials project pipeline', 'MASE published a pipeline of domestic critical-materials projects. Several align with joint U.S.-Italy objectives.', 'Trade Press', 78),

    (49, 'European Bank for Reconstruction and Development (EBRD)', 'Partnership', '2026-01-16', 'EBRD expands climate and minerals financing pipeline', 'EBRD detailed an expanded pipeline for climate and minerals projects in emerging Europe. Co-financing with U.S. instruments is under exploration.', 'EU Monitor', 70),
    (50, 'European Bank for Reconstruction and Development (EBRD)', 'News', '2026-06-03', 'EBRD eyes North Africa processing co-financing', 'EBRD signaled interest in co-financing a North Africa processing project. The move could complement DFC efforts.', 'Trade Press', 68),

    (51, 'African Development Bank (AfDB)', 'Analysis', '2025-12-09', 'AfDB natural-resources portfolio draws allied interest', 'An assessment of AfDB''s natural-resources portfolio highlighted allied-engagement options. Both minerals and food-security tracks are relevant.', 'State Dept Cable', 66),
    (52, 'African Development Bank (AfDB)', 'Partnership', '2026-04-19', 'AfDB explores minerals-sourcing partnership frameworks', 'AfDB discussed frameworks for critical-minerals sourcing partnerships. Engagement remains exploratory.', 'Trade Press', 63),

    (53, 'Global Battery Alliance', 'Ministerial', '2026-02-12', 'GBA presents battery-passport standards at Ministerial', 'The Global Battery Alliance showcased battery-passport standards at the Rome Ministerial. Standards could underpin allied procurement criteria.', 'State Dept Cable', 81),
    (54, 'Global Battery Alliance', 'News', '2026-07-20', 'GBA advances responsible supply-chain certification', 'GBA announced progress on responsible supply-chain certification. Alignment with U.S. procurement rules is under review.', 'Trade Press', 74),

    (55, 'TotalEnergies (Italy office)', 'News', '2025-09-19', 'TotalEnergies expands storage ventures in Italy', 'TotalEnergies announced battery-storage ventures in Italy tied to renewables. The projects touch bilateral energy interests.', 'Reuters', 62),
    (56, 'TotalEnergies (Italy office)', 'Partnership', '2026-05-23', 'TotalEnergies weighs role in energy-security roundtable', 'TotalEnergies considered participation in a Mission energy-security roundtable. Engagement is transactional.', 'Trade Press', 60),

    (57, 'Bayer CropScience (Rome/FAO liaison)', 'News', '2025-10-22', 'Bayer promotes digital-agriculture tools at FAO forum', 'Bayer showcased digital-agriculture tools at an FAO private-sector forum. The tools intersect food-security and data-governance debates.', 'FAO Press', 67),
    (58, 'Bayer CropScience (Rome/FAO liaison)', 'Analysis', '2026-03-28', 'Bayer aligns with FAO efficiency-and-accountability framing', 'Analysis noted Bayer''s alignment with efficiency and accountability themes at FAO. The stance supports U.S. private-sector messaging.', 'State Dept Cable', 69),
    (59, 'Bayer CropScience (Rome/FAO liaison)', 'Partnership', '2026-08-02', 'Bayer deepens FAO liaison on crop-innovation programs', 'Bayer expanded its FAO liaison work on crop-innovation programs. Cooperation reinforces food-security private-sector engagement.', 'Trade Press', 65);

-- =============================================================================
-- TABLE 4: SUMMIT_ATTENDEES
-- =============================================================================
INSERT INTO SUMMIT_ATTENDEES
    (attendee_name, organization, country, title, sector)
VALUES
    ('Alessandro Corsi', 'Enel Green Power', 'Italy', 'CEO', 'Critical Minerals / Energy'),
    ('Dr. Sarah Chen', 'U.S. Dept of Energy', 'USA', 'Dep. Asst. Secretary, Minerals', 'Critical Minerals'),
    ('Dr. Marco Van der Berg', 'Vulcan Energy Resources', 'Germany', 'Chief Technology Officer', 'Lithium Processing'),
    ('Thomas Whitmore', 'Albemarle Corporation', 'USA', 'VP Government Affairs', 'Lithium Supply Chain'),
    ('Kenji Tanaka', 'Japan Critical Minerals Agency', 'Japan', 'Director General', 'Critical Minerals'),
    ('Fatima Al-Rashid', 'WFP Rome Liaison', 'UN / Italy', 'Executive Director, Rome Office', 'Food Security'),
    ('Dr. Emmanuel Osei', 'FAO', 'UN / Italy', 'Deputy Director-General', 'Food Security / Agriculture'),
    ('Helena Svensson', 'Yara International', 'Norway', 'Director, International Relations', 'Fertilizers / Food Security'),
    ('Miguel Fernandez', 'Brazilian Ministry of Agriculture', 'Brazil', 'Special Agricultural Attache', 'Agriculture / Food Security'),
    ('Dr. Amara Diallo', 'IFAD', 'UN / Italy', 'Director, West Africa Program', 'Food Security / Development'),
    ('Dr. Isabella Moretti', 'Italian Ministry of MASE', 'Italy', 'Director, Critical Materials', 'Critical Minerals'),
    ('Pierre Dubois', 'European Commission', 'EU / Belgium', 'Commissioner, Critical Raw Materials', 'Critical Minerals'),
    ('Anna Kowalski', 'Polish Ministry of Mining', 'Poland', 'Deputy Minister', 'Critical Minerals'),
    ('Bjorn Eriksson', 'Swedish Ministry of Trade', 'Sweden', 'Critical Minerals Attache', 'Critical Minerals'),
    ('Hamid Benali', 'OCP Group', 'Morocco', 'VP International Affairs', 'Critical Minerals / Phosphates'),
    ('Lucia Fernandez', 'Barrick Gold', 'Canada', 'Director, EU Government Affairs', 'Mining'),
    ('Dr. James Achebe', 'African Minerals Dev. Centre', 'DRC', 'Executive Chairman', 'Critical Minerals / Africa'),
    ('Pham Thi Lan', 'Vietnamese Ministry of Resources', 'Vietnam', 'Deputy Minister', 'Critical Minerals'),
    ('Carlos Matos', 'Lithium Americas (Chile JV)', 'Chile', 'CEO, Americas Operations', 'Lithium'),
    ('Sophie Laurent', 'Breakthrough Energy Europe', 'Belgium', 'Managing Director', 'Clean Energy / Minerals'),
    ('David Kim', 'IFC Critical Minerals Fund', 'South Korea', 'Partner', 'Finance / Development'),
    ('Margaret O''Brien', 'European Investment Bank', 'EU / Ireland', 'Director, Climate Investment', 'Finance / Energy'),
    ('Prof. Roberto Ricci', 'Mediterranean Energy Policy Institute', 'Italy', 'Director General', 'Policy / Research'),
    ('Dr. Layla Hassan', 'CSIS Critical Minerals Program', 'USA', 'Senior Fellow', 'Policy / Research'),
    ('Ambassador Chen Wei', 'Chinese Mission, UN Rome', 'China', 'Charge d''Affaires', 'Diplomacy'),
    ('H.E. Beatriz Santos', 'Portuguese Government', 'Portugal', 'Special Envoy, Critical Minerals', 'Critical Minerals / Diplomacy'),
    ('Dr. Stavros Papadopoulos', 'Greek Ministry of Energy', 'Greece', 'Deputy Minister', 'Energy / Minerals'),
    ('Rt. Hon. James Hartley', 'UK Dept for Energy Security', 'UK', 'Deputy Minister, Mining & Minerals', 'Critical Minerals');

-- =============================================================================
-- TABLE 5: MISSION_PRIORITIES
-- =============================================================================
INSERT INTO MISSION_PRIORITIES
    (priority_id, priority_name, description, weight, status)
VALUES
    (1, 'Critical Minerals Supply Chain Diversification', 'Reduce U.S. dependency on Chinese-sourced critical minerals through allied-nation partnerships. Priority materials: lithium, cobalt, nickel, graphite, rare earths. Instruments: DFC financing, bilateral minerals agreements, Ministerial coalition building.', 0.35, 'Active'),
    (2, 'FAO/WFP Accountability and Reform', 'America First food security accountability mandate. Drive FAO governance reform, WFP efficiency review, and demonstrate U.S. taxpayer return on investment across Rome-based UN agencies (FAO, WFP, IFAD).', 0.30, 'Active'),
    (3, 'AI Diplomacy and Technology Alignment', 'Advance U.S. AI leadership agenda through strategic engagement with Vatican, EU, and Italian government partners. Align EO 14179 narrative with multilateral AI governance frameworks. Counter Chinese technology influence.', 0.20, 'Active'),
    (4, 'U.S.-Italy Bilateral Energy and Minerals Partnership', 'Deepen bilateral energy partnership with Italy leveraging ENI, Enel, and Italian government engagement. Connect Italian industrial capacity to U.S. supply chain frameworks. Support Italian G7 presidency outcomes.', 0.15, 'Active');

-- =============================================================================
-- TABLE 6: POLICY_DOCUMENTS
-- =============================================================================
INSERT INTO POLICY_DOCUMENTS
    (doc_id, doc_title, doc_type, issuer, issue_date, classification, full_text, summary)
VALUES
    (1,
     'EO 14179 — Removing Barriers to American Leadership in Artificial Intelligence',
     'Executive Order',
     'The White House',
     '2025-01-23',
     'Internal',
     'By the authority vested in me as President by the Constitution and the laws of the United States of America, it is hereby ordered as follows.

Section 1. Purpose. The United States has long been the global leader in artificial intelligence, and it is the policy of this Administration to sustain and expand that leadership. Recent regulatory approaches have imposed unnecessary barriers to American AI innovation, ceding ground to strategic competitors and constraining the private-sector ingenuity that has made the United States the world''s foremost technological power. This order removes those barriers and reasserts American dominance in artificial intelligence to promote national security, economic competitiveness, and human flourishing.

Sec. 2. Revocation of Prior Policy. The prior Administration''s executive order on the safe, secure, and trustworthy development of artificial intelligence, together with its implementing directives, is hereby revoked. Executive departments and agencies shall immediately suspend, revise, or rescind all actions taken pursuant to that revoked order that are inconsistent with the policy set forth in section 1. Agencies shall report to the Assistant to the President for Science and Technology within 60 days on the status of such actions.

Sec. 3. Policy of Innovation First. It is the policy of the United States to prioritize AI innovation and adoption across the Federal Government and the broader economy. Agencies shall interpret and apply existing statutory authorities to minimize regulatory burden on the development, deployment, and commercialization of artificial intelligence, consistent with law. Agencies shall avoid imposing new requirements that would disadvantage American developers relative to foreign competitors, particularly the People''s Republic of China.

Sec. 4. AI Action Plan. Within 180 days of the date of this order, the Assistant to the President for Science and Technology, in coordination with the Secretary of Commerce, the Secretary of Energy, the Secretary of Defense, and the Director of the Office of Management and Budget, shall develop and submit an AI Action Plan. The plan shall identify concrete measures to accelerate American AI leadership, including actions to expand domestic compute capacity, streamline permitting for AI-enabling infrastructure, strengthen the AI talent pipeline, and secure critical supply chains for advanced semiconductors and the materials on which they depend.

Sec. 5. Accelerating Federal Adoption. The Department of Defense, the Department of Energy, and the Department of Commerce shall take all appropriate steps to accelerate the responsible adoption of artificial intelligence within their missions. The Secretary of Defense shall prioritize AI applications that enhance warfighter capability and decision advantage. The Secretary of Energy shall leverage the national laboratories and available energy resources to support large-scale AI research and the compute infrastructure it requires. The Secretary of Commerce shall promote American AI exports and standards leadership in international bodies.

Sec. 6. Countering Strategic Competitors. Agencies shall coordinate to ensure that United States AI policy advances national security and counters the influence of authoritarian competitors. This includes protecting American AI intellectual property, guarding against technology transfer that would benefit strategic rivals, and promoting democratic values in the international governance of artificial intelligence.

Sec. 7. General Provisions. This order shall be implemented consistent with applicable law and subject to the availability of appropriations. Nothing in this order shall be construed to impair or otherwise affect the authority granted by law to an executive department or agency, or the head thereof. This order is not intended to, and does not, create any right or benefit, substantive or procedural, enforceable at law or in equity by any party against the United States, its departments, agencies, or entities, its officers, employees, or agents, or any other person.',
     'Revokes the prior Administration''s AI safety order and directs agencies to prioritize AI innovation, remove regulatory barriers, and accelerate Federal adoption. Mandates an AI Action Plan within 180 days and directs DOD, DOE, and Commerce to expand compute, secure supply chains, and counter Chinese technology influence.'),

    (2,
     'Critical Minerals Strategy 2026',
     'Strategic Document',
     'U.S. Department of State',
     '2026-01-15',
     'Internal',
     'Executive Summary. The Critical Minerals Strategy 2026 sets forth the United States'' approach to securing reliable, diversified, and allied supply chains for the minerals essential to national defense, clean energy, and advanced manufacturing. The strategy responds to the strategic vulnerability created by the People''s Republic of China''s dominance over the mining and, especially, the processing of critical minerals. It establishes clear objectives, financing instruments, and diplomatic mechanisms to reduce that dependency in cooperation with allied and partner nations.

Strategic Objective. The overarching objective is a fifty percent reduction in Chinese-sourced critical minerals for U.S. defense supply chains by 2030. Achieving this target requires coordinated action across mining, processing, and offtake, with particular emphasis on processing capacity, where allied dependence on the PRC is most acute.

Priority Materials. The strategy designates the following priority materials: lithium, cobalt, nickel, graphite, and rare earth elements. These materials are indispensable to batteries, magnets, and defense platforms, and each faces significant supply concentration risk. Agencies shall prioritize projects and partnerships that expand allied capacity across these five material classes.

Financing Instruments. The centerpiece financing instrument is a four billion dollar commitment through the U.S. International Development Finance Corporation to support allied-nation minerals projects. DFC financing will be directed toward projects that expand mining and processing outside the PRC, with preference for those that establish long-term offtake to U.S. and allied buyers. Financing will be coordinated with allied development banks and private capital to maximize leverage and de-risk early-stage projects.

Ministerial Coalition. The United States will lead a Ministerial coalition of allied and partner governments to align standards, coordinate investment, and pool demand. The coalition will convene regularly, beginning with the Critical Minerals Ministerial hosted in Rome, and will pursue common approaches to responsible sourcing, transparency, and market resilience. Coalition activity will be reinforced by multi-stakeholder bodies such as the Global Battery Alliance.

Bilateral Agreements Framework. The strategy establishes a framework for bilateral minerals agreements with resource-holding and processing partners. These agreements will provide predictable terms for investment, offtake, environmental and labor standards, and dispute resolution. Priority partners include allied processors in Europe, resource holders in Africa and South America, and industrial partners such as Italy under the U.S.-Italy bilateral track.

Implementation and Oversight. The Department of State, in coordination with the Departments of Energy, Commerce, and Defense and the DFC, will oversee implementation. Missions abroad, including the U.S. Mission in Rome, will support the strategy through engagement with host governments, multilateral institutions, and the private sector. Progress will be measured against the 2030 reduction target and reported annually, with metrics on financing deployed, capacity added, and dependency reduced.

Conclusion. The Critical Minerals Strategy 2026 aligns diplomacy, finance, and industrial policy behind a single objective: durable, allied supply chains that free the United States and its partners from strategic dependence on the PRC. Success will require sustained coalition leadership, disciplined use of financing, and close coordination between Washington and Missions in the field.',
     'Sets a target of 50% reduction in Chinese-sourced defense critical minerals by 2030, backed by $4B in DFC financing for allied-nation projects. Prioritizes lithium, cobalt, nickel, graphite, and rare earths, and establishes a Ministerial coalition and bilateral agreements framework, with Rome-based engagement supporting implementation.'),

    (3,
     'USUN Rome Cable: WFP Accountability Review',
     'Diplomatic Cable',
     'USUN Rome / Ambassador Blanchard',
     '2026-01-14',
     'Internal',
     'SUMMARY. Ambassador Blanchard met with World Food Programme leadership on January 13 to press U.S. concerns regarding operational efficiency and accountability. The Ambassador conveyed that continued U.S. support is contingent on demonstrable reform, and previewed a recommendation to condition a portion of the U.S. assessed contribution on adoption of a credible reform plan. This cable reports the engagement and provides recommendations for Department consideration. END SUMMARY.

BACKGROUND. The World Food Programme remains the largest of the Rome-based United Nations agencies and a significant recipient of U.S. contributions. Consistent with the Administration''s America First accountability mandate, the Mission has intensified scrutiny of WFP''s administrative costs, program overlap, and results reporting. This review draws on WFP financial disclosures, comparative benchmarks provided by private-sector partners, and parallel findings from the Mission''s IFAD review.

ADMINISTRATIVE OVERHEAD. The central concern is WFP''s administrative overhead, currently assessed at approximately 23 percent of expenditures. This figure substantially exceeds the sub-18 percent benchmark that donors, including the United States, regard as consistent with efficient humanitarian operations. The Ambassador stressed that overhead at current levels erodes donor confidence and diverts resources from beneficiaries. WFP leadership acknowledged the figure and cited security, logistics, and access costs in high-risk environments as contributing factors, but did not dispute the need for improvement.

PROGRAM DUPLICATION. The review identified material duplication between WFP school-meals programming and FAO nutrition initiatives. Overlapping mandates, parallel field structures, and uncoordinated procurement increase cost and complicate accountability. The Ambassador urged WFP and FAO to pursue consolidation and joint delivery where mandates converge, and noted that the Mission would raise the matter with the FAO Private Sector Advisory Group and in relevant governing bodies.

IFAD REVIEW LINKAGE. The Mission''s parallel review of the International Fund for Agricultural Development surfaced comparable efficiency concerns, reinforcing the case for a Rome-agency-wide accountability approach. Findings suggest that inefficiencies are systemic across the Rome-based agencies rather than confined to any single organization, and that a coordinated donor strategy will be more effective than agency-by-agency pressure.

RECOMMENDATION. The Mission recommends that the Department authorize signaling that fifteen percent of the U.S. assessed contribution to WFP be withheld pending WFP''s submission and adoption of a credible reform plan. Such a plan should include a time-bound commitment to reduce administrative overhead toward the sub-18 percent benchmark, a concrete framework to eliminate duplication with FAO, and enhanced results reporting demonstrating taxpayer return on investment. The Mission assesses that a conditional posture, applied consistently across the Rome agencies, offers the strongest leverage for durable reform.

NEXT STEPS. The Mission will continue engagement with WFP leadership and the Executive Board, coordinate with like-minded donors, and report progress against the benchmarks above. The Ambassador requests Department guidance on the proposed conditionality by the next Executive Board session. END CABLE.',
     'Reports Ambassador Blanchard''s engagement with WFP leadership on efficiency, flagging 23% administrative overhead against a sub-18% target and duplication with FAO nutrition programs. Recommends withholding 15% of the U.S. assessed contribution pending a credible reform plan, and links the findings to a parallel IFAD review supporting a Rome-agency-wide accountability approach.'),

    (4,
     'Rome Call for AI Ethics (Updated 2025)',
     'Multilateral Declaration',
     'Pontifical Academy for Life',
     '2025-11-15',
     'External',
     'Preamble. The Rome Call for AI Ethics, first proclaimed in 2020, is renewed and updated in 2025 to reflect the accelerating development and diffusion of artificial intelligence. Convened by the Pontifical Academy for Life and endorsed by His Holiness Pope Francis, the Call is co-signed by leading technology companies, including IBM and Microsoft, and by more than twenty-five Catholic universities and research institutions from around the world. It affirms that artificial intelligence must be developed and deployed in service of human dignity and the common good.

The Vision of Algor-ethics. The Call advances the concept of algor-ethics: the embedding of ethical principles into the design, development, and governance of algorithmic systems. Technology must not be an end in itself but a means to promote the integral development of the human person and the flourishing of communities, with particular attention to the vulnerable and the marginalized.

Six Principles. The Call sets forth six principles to guide the ethical development of artificial intelligence. First, transparency: AI systems must be explainable and open to scrutiny. Second, inclusion: the benefits of AI must be available to all, and systems must not discriminate. Third, responsibility: those who design and deploy AI must be accountable for its effects. Fourth, impartiality: AI must not create or act on bias, safeguarding fairness and human dignity. Fifth, reliability: AI systems must operate dependably and safely. Sixth, security and privacy: systems must respect privacy and be robust against misuse.

Human Dignity and the Common Good. The updated Call reaffirms that artificial intelligence must always serve, and never diminish, human dignity. It insists that decisions with significant consequences for human life and rights remain under meaningful human control. It warns against the reduction of persons to data points and against uses of AI that undermine autonomy, solidarity, or the dignity of work.

Governance. The 2025 update strengthens the Call''s appeal for binding international governance of artificial intelligence. It holds that voluntary commitments, while valuable, are insufficient to address the scale of risk, and it calls on governments and international institutions to establish enforceable norms. It urges that such governance be inclusive of the Global South and attentive to the digital divide.

Weapons and Surveillance. The Call expresses particular concern regarding the application of artificial intelligence to weapons systems and to mass surveillance. It calls for meaningful human control over the use of force and warns that autonomous weapons and pervasive surveillance threaten human dignity, civil liberties, and international stability. Signatories commit to opposing uses of AI that enable indiscriminate harm or the suppression of fundamental freedoms.

Commitment of Signatories. In signing the updated Rome Call, the parties commit to promoting these principles within their organizations and in the wider world, to fostering education in algor-ethics, and to collaborating across sectors and faith traditions. The Pontifical Academy for Life invites additional governments, companies, religious communities, and institutions to join, in the conviction that the ethical development of artificial intelligence is a shared responsibility of the whole human family.',
     'An updated iteration of the 2020 Rome Call convened by the Pontifical Academy for Life, co-signed by IBM, Microsoft, and 25+ Catholic universities and endorsed by Pope Francis. It sets six AI principles—transparency, inclusion, responsibility, impartiality, reliability, and security—insists AI serve human dignity and the common good, calls for binding international governance, and warns against AI in weapons and mass surveillance.'),

    (5,
     'FAO Digital Agriculture and AI Strategy',
     'Organizational Strategy',
     'Food and Agriculture Organization (FAO)',
     '2024-10-01',
     'External',
     'Introduction. The Food and Agriculture Organization of the United Nations presents this strategy to guide the responsible adoption of digital technologies and artificial intelligence in food and agriculture. The strategy reflects FAO''s mandate to achieve food security for all and its conviction that digital innovation, if governed inclusively, can accelerate progress toward the Sustainable Development Goals while safeguarding the interests of the world''s smallholder farmers.

Guiding Principle: Small-Scale Farmer Access. The strategy places small-scale and family farmers at its center. Digital and AI tools must be accessible, affordable, and appropriate to the realities of smallholders, who produce a large share of the world''s food yet often lack connectivity, capital, and data literacy. FAO commits to prioritizing solutions that reach these producers and to resisting a two-tier digital agriculture in which benefits accrue only to large, well-resourced operators.

Applications. The strategy identifies priority applications of artificial intelligence in food and agriculture. These include food-security prediction and early-warning modeling to anticipate shocks and target assistance; supply-chain traceability to improve transparency, food safety, and market access; precision advisory services to improve yields and resource efficiency; and pest and disease surveillance. In each case, FAO emphasizes that tools must augment, not displace, the knowledge and agency of farmers.

Open-Source and Public-Good Development. FAO advocates for open-source and public-good approaches to AI development in agriculture. Open models, shared datasets, and interoperable standards lower barriers to entry, enable local adaptation, and reduce dependence on proprietary systems. FAO will support the development of open resources and encourage member states and partners to contribute to shared digital public goods.

Data Governance and Caution Against Monopolization. The strategy warns against the proprietary monopolization of food-system data. Concentration of agricultural data in the hands of a few private actors risks entrenching market power, undermining farmer autonomy, and constraining public-interest research. FAO calls for data-governance frameworks that protect farmers'' rights over their data, promote fair value-sharing, and preserve public access to information essential to food security.

Alignment with UN AI Governance. FAO endorses the emerging United Nations principles for the governance of artificial intelligence and commits to aligning its digital-agriculture work with those principles. This includes attention to transparency, accountability, human rights, and inclusion, and coordination with sister agencies and multilateral processes to ensure coherence across the UN system.

Bridging the Digital Divide. The strategy confronts the digital divide directly. Gaps in connectivity, electricity, devices, and skills threaten to exclude the very populations most in need of the benefits of digital agriculture. FAO commits to investing in enabling infrastructure, capacity building, and partnerships that extend access to underserved regions, with particular attention to women, youth, and marginalized communities.

Implementation. FAO will implement this strategy through its technical programs, country offices, and partnerships with governments, research institutions, and the private sector, including engagement with private-sector advisory mechanisms. Progress will be monitored against indicators of access, inclusion, and impact, and the strategy will be periodically reviewed to keep pace with technological change.',
     'FAO''s framework for responsible AI and digital adoption in food and agriculture, centered on small-scale farmer access. It prioritizes food-security prediction, supply-chain traceability, and open-source development, cautions against proprietary monopolization of food-system data, endorses UN AI governance principles, and commits to bridging the digital divide.'),

    (6,
     'Italian G7 AI Declaration — Naples 2024',
     'G7 Declaration',
     'G7 Leaders (Italian Presidency)',
     '2024-07-15',
     'External',
     'Preamble. We, the Leaders of the Group of Seven, meeting under the Italian Presidency in Naples, affirm our shared commitment to the responsible development and deployment of artificial intelligence. We recognize the transformative potential of AI to advance prosperity, address global challenges, and improve the lives of our citizens, and we are equally mindful of the risks that must be managed to ensure that AI serves people and upholds our shared democratic values.

Responsible Development. We commit to fostering the responsible development of artificial intelligence in a manner that is safe, secure, and trustworthy. We affirm that innovation and responsibility are complementary, and that well-designed governance can strengthen public trust and thereby accelerate the beneficial adoption of AI. We will promote research, investment, and international cooperation to advance these aims.

Endorsement of OECD AI Principles. We reaffirm our endorsement of the OECD AI Principles as a common foundation for trustworthy artificial intelligence. These principles—including respect for human rights, transparency, robustness, and accountability—provide shared reference points for our national approaches and for international cooperation, and we encourage their wide adoption.

Risk-Based Regulation. We support a risk-based approach to the regulation of artificial intelligence that preserves innovation while addressing genuine harms. Regulatory measures should be proportionate, focused on high-risk applications, and designed to avoid unnecessary burdens that would impede beneficial uses or disadvantage responsible developers. We will seek interoperability among our respective frameworks to reduce fragmentation.

Human Oversight in High-Risk Applications. We affirm the importance of meaningful human oversight, particularly in high-risk applications of artificial intelligence. Decisions that materially affect human rights, safety, or access to essential services should remain subject to appropriate human control and review. We are especially attentive to applications in critical infrastructure, public services, and security.

G7 AI Incident Reporting Framework. We commit to establishing a joint G7 framework for the reporting and sharing of information on significant AI incidents. By exchanging lessons from failures, near-misses, and emerging risks, we aim to strengthen collective resilience, improve the safety of AI systems, and inform proportionate policy responses. We will task relevant officials to develop the framework''s modalities.

Democratic Values in AI Governance. We are determined that the governance of artificial intelligence reflect democratic values, the rule of law, and respect for human rights. We will work together and with partners to promote these values in international standards and institutions, and to ensure that AI strengthens open societies rather than eroding them.

Countering Authoritarian Models. We express concern regarding the use of artificial intelligence by authoritarian actors to enable mass surveillance, censorship, disinformation, and the suppression of fundamental freedoms. We commit to cooperating to counter such uses, to protect the integrity of our information environments and democratic processes, and to offer a positive, rights-respecting model of AI development to partners around the world.

Conclusion. We task our relevant Ministers and officials to advance the commitments set out in this Declaration and to report on progress under future presidencies. We invite partners who share our values to join us in building a future in which artificial intelligence is developed and used responsibly, for the benefit of all.',
     'A G7 Leaders'' declaration under the Italian Presidency affirming responsible, trustworthy AI. It endorses the OECD AI Principles, supports risk-based regulation that preserves innovation, requires human oversight in high-risk applications, establishes a joint G7 AI incident-reporting framework, and commits to democratic values in AI governance while countering authoritarian AI models.');
