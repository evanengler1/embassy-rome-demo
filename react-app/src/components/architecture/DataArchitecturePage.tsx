"use client";

import { motion } from "framer-motion";
import {
  Database,
  Cpu,
  BrainCircuit,
  AppWindow,
  Zap,
  Search,
  Bot,
  Layers,
  Eye,
  ShieldCheck,
} from "lucide-react";
import GlassCard from "../shared/GlassCard";

const archColumns = [
  {
    title: "Source Data",
    color: "#f59e0b",
    items: [
      "SMART Cables",
      "Salesforce CRM",
      "Policy Documents",
      "Sector Intelligence",
    ],
  },
  {
    title: "Snowflake Platform",
    color: "#3b82f6",
    highlight: true,
    items: [
      "Medallion Architecture",
      "Cortex Search Services",
      "Semantic View",
      "RBAC / Governance",
    ],
  },
  {
    title: "Intelligence Layer",
    color: "#8b5cf6",
    items: [
      "Cortex Complete (LLM)",
      "Cortex Search",
      "Cortex Agent",
      "Dynamic Enrichment",
    ],
  },
  {
    title: "This App",
    color: "#10b981",
    items: [
      "CRM Enrichment",
      "Event Prioritization",
      "Policy Alignment",
      "CoWork Agent",
    ],
  },
];

const capabilities = [
  {
    icon: Zap,
    title: "CORTEX.COMPLETE (gemini-2.5-flash)",
    description:
      "Powers all AI summaries, CRM enrichment, event prioritization, and policy alignment analysis. Context injected from live Snowflake data at query time.",
    color: "#f59e0b",
  },
  {
    icon: Search,
    title: "Cortex Search",
    description:
      "Semantic retrieval over policy documents and sector intelligence. Two search services index full text for real-time contextual grounding.",
    color: "#3b82f6",
  },
  {
    icon: Bot,
    title: "Cortex Agent",
    description:
      "Combines text-to-SQL via Semantic View with Cortex Search tools, enabling natural-language queries across CRM, cables, and policy data.",
    color: "#8b5cf6",
  },
  {
    icon: Layers,
    title: "Medallion Architecture",
    description:
      "Bronze (raw tables), Silver (Cortex Search indexes), Gold (Semantic View) provide governed data progression from ingestion to intelligence.",
    color: "#10b981",
  },
  {
    icon: Eye,
    title: "Semantic View",
    description:
      "Structured analytical model over CRM contacts, activity logs, and summit attendees with defined dimensions, facts, metrics, and relationships.",
    color: "#06b6d4",
  },
  {
    icon: ShieldCheck,
    title: "Role-Based Access",
    description:
      "DOS_ROME_DEMO_ROLE with scoped grants across Bronze, Silver, and Gold schemas. Cortex function access explicitly granted per role.",
    color: "#f43f5e",
  },
];

function AnimatedArrow({ color }: { color: string }) {
  return (
    <div className="flex items-center justify-center w-8 shrink-0 self-stretch">
      <div className="relative h-full flex items-center">
        <div
          className="w-px h-3/5 opacity-20"
          style={{ background: color }}
        />
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="flex flex-col gap-3">
            {[0, 1, 2].map((i) => (
              <motion.div
                key={i}
                className="w-1.5 h-1.5 rounded-full"
                style={{ background: color }}
                animate={{
                  x: [0, 6, 0],
                  opacity: [0.3, 1, 0.3],
                }}
                transition={{
                  duration: 1.5,
                  repeat: Infinity,
                  delay: i * 0.3,
                  ease: "easeInOut",
                }}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function ArchColumn({
  title,
  color,
  highlight,
  items,
  delay,
}: {
  title: string;
  color: string;
  highlight?: boolean;
  items: string[];
  delay: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay, ease: "easeOut" }}
      className="flex-1 rounded-xl border p-4 min-w-0"
      style={{
        borderColor: highlight ? color : "rgba(59, 130, 246, 0.15)",
        background: highlight
          ? `${color}08`
          : "rgba(17, 24, 39, 0.4)",
      }}
    >
      <p
        className="text-xs font-bold uppercase tracking-widest mb-4"
        style={{ color }}
      >
        {title}
      </p>
      <ul className="space-y-2">
        {items.map((item) => (
          <li key={item} className="flex items-center gap-2 text-sm text-slate-300">
            <span
              className="w-1.5 h-1.5 rounded-full shrink-0"
              style={{ background: color }}
            />
            {item}
          </li>
        ))}
      </ul>
    </motion.div>
  );
}

function CapabilityCard({
  icon: Icon,
  title,
  description,
  color,
  delay,
}: {
  icon: typeof Zap;
  title: string;
  description: string;
  color: string;
  delay: number;
}) {
  return (
    <GlassCard delay={delay}>
      <div className="flex items-start gap-3">
        <div
          className="w-1 h-12 rounded-full shrink-0 mt-0.5"
          style={{ background: color }}
        />
        <div className="min-w-0">
          <div className="flex items-center gap-2 mb-2">
            <Icon size={16} style={{ color }} />
            <h4 className="text-sm font-semibold text-white truncate">{title}</h4>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">{description}</p>
        </div>
      </div>
    </GlassCard>
  );
}

export default function DataArchitecturePage() {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-white mb-1">
          Powered by Snowflake
        </h1>
        <p className="text-sm text-slate-400 leading-relaxed max-w-2xl">
          This diplomatic intelligence platform runs entirely on the Snowflake AI
          Data Cloud — one platform for data lakehouse, AI/ML, semantic search,
          and governance.
        </p>
        <div className="flex items-center gap-3 mt-3">
          <span className="text-xs font-bold text-blue-400 px-2.5 py-1 rounded-full border border-blue-500/30 bg-blue-500/10 uppercase tracking-wider">
            Snowflake
          </span>
          <span className="text-xs text-slate-500 font-mono">
            DOS_ROME_DEMO &middot; Bronze / Silver / Gold &middot; live
            connection
          </span>
        </div>
      </div>

      <GlassCard delay={0.1}>
        <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-5">
          Platform Architecture
        </h3>
        <div className="flex items-stretch gap-0">
          {archColumns.map((col, i) => (
            <div key={col.title} className="contents">
              <ArchColumn
                {...col}
                delay={0.15 + i * 0.08}
              />
              {i < archColumns.length - 1 && (
                <AnimatedArrow
                  color={archColumns[i + 1].color}
                />
              )}
            </div>
          ))}
        </div>
      </GlassCard>

      <div>
        <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">
          Snowflake Capabilities in Use
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {capabilities.map((cap, i) => (
            <CapabilityCard
              key={cap.title}
              {...cap}
              delay={0.3 + i * 0.05}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
