"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ExternalLink } from "lucide-react";
import GlassCard from "../shared/GlassCard";
import type { SectorIntel } from "@/lib/types";
import { apiCall } from "@/lib/api";

const SOURCE_COLORS: Record<string, string> = {
  "Trade Press": "#3b82f6",
  "State Dept Cable": "#f59e0b",
  Bloomberg: "#10b981",
  "FAO Press": "#8b5cf6",
  Reuters: "#ef4444",
  "EU Monitor": "#06b6d4",
  "Vatican Press Office": "#f97316",
  WRI: "#84cc16",
  CSIS: "#ec4899",
};

export default function IntelligencePage() {
  const [intel, setIntel] = useState<SectorIntel[]>([]);
  const [sourceFilter, setSourceFilter] = useState<string | null>(null);
  const [sortBy, setSortBy] = useState<"date" | "relevance">("date");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiCall<SectorIntel[]>("getIntelligence")
      .then(setIntel)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const sources = [...new Set(intel.map((i) => i.SOURCE))];

  let filtered = sourceFilter ? intel.filter((i) => i.SOURCE === sourceFilter) : intel;
  if (sortBy === "relevance") {
    filtered = [...filtered].sort((a, b) => b.RELEVANCE_SCORE - a.RELEVANCE_SCORE);
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 flex-wrap">
        <button
          onClick={() => setSourceFilter(null)}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
            !sourceFilter ? "bg-blue-500/20 text-blue-400" : "text-slate-400 hover:bg-white/5"
          }`}
        >
          All Sources
        </button>
        {sources.map((s) => (
          <button
            key={s}
            onClick={() => setSourceFilter(sourceFilter === s ? null : s)}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
              sourceFilter === s ? "bg-blue-500/20 text-blue-400" : "text-slate-400 hover:bg-white/5"
            }`}
          >
            {s}
          </button>
        ))}
        <div className="ml-auto flex items-center gap-1 text-xs">
          <span className="text-slate-500">Sort:</span>
          <button
            onClick={() => setSortBy("date")}
            className={`px-2 py-1 rounded ${sortBy === "date" ? "text-blue-400" : "text-slate-500"}`}
          >
            Date
          </button>
          <button
            onClick={() => setSortBy("relevance")}
            className={`px-2 py-1 rounded ${sortBy === "relevance" ? "text-blue-400" : "text-slate-500"}`}
          >
            Relevance
          </button>
        </div>
      </div>

      {loading && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="glass p-5"><div className="skeleton h-24" /></div>
          ))}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {filtered.map((item, i) => {
          const color = SOURCE_COLORS[item.SOURCE] || "#64748b";
          return (
            <motion.div
              key={item.INTEL_ID}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: Math.min(i * 0.03, 0.4) }}
            >
              <GlassCard animate={false} className="!p-4 space-y-2.5">
                <div className="flex items-start justify-between">
                  <h4 className="text-sm font-medium text-white leading-tight flex-1">{item.HEADLINE}</h4>
                  <ExternalLink size={12} className="text-slate-600 shrink-0 ml-2 mt-0.5" />
                </div>
                <p className="text-xs text-slate-400 leading-relaxed">{item.SUMMARY}</p>
                <div className="flex items-center gap-3 text-xs">
                  <span
                    className="px-2 py-0.5 rounded-full font-medium"
                    style={{ background: `${color}20`, color }}
                  >
                    {item.SOURCE}
                  </span>
                  <span className="text-slate-500">{item.ORG_NAME}</span>
                  <span className="text-slate-600 font-mono">{item.INTEL_DATE}</span>
                  <div className="ml-auto flex items-center gap-1.5">
                    <div className="w-12 h-1.5 rounded-full bg-navy-700 overflow-hidden">
                      <div
                        className="h-full rounded-full bg-blue-500"
                        style={{ width: `${item.RELEVANCE_SCORE}%` }}
                      />
                    </div>
                    <span className="text-slate-500 font-mono">{item.RELEVANCE_SCORE}</span>
                  </div>
                </div>
              </GlassCard>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
