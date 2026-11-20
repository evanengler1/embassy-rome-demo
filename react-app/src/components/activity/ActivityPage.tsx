"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronDown } from "lucide-react";
import { useActivities } from "@/lib/queries";

const DOT_COLORS: Record<string, string> = {
  Meeting: "#3b82f6",
  Call: "#10b981",
  Cable: "#f59e0b",
  Event: "#f43f5e",
  Email: "#64748b",
};

const TYPE_STYLES: Record<string, { bg: string; text: string }> = {
  Meeting: { bg: "bg-blue-500/15", text: "text-blue-400" },
  Call: { bg: "bg-emerald-500/15", text: "text-emerald-400" },
  Cable: { bg: "bg-amber-500/15", text: "text-amber-400" },
  Event: { bg: "bg-rose-500/15", text: "text-rose-400" },
  Email: { bg: "bg-slate-500/15", text: "text-slate-400" },
};

const CLASS_COLORS: Record<string, string> = {
  "High-Priority": "text-rose-400",
  Significant: "text-amber-400",
  Routine: "text-slate-500",
};

const TYPES = ["All", "Meeting", "Call", "Cable", "Event", "Email"];

export default function ActivityPage() {
  const { data: activities = [], isLoading } = useActivities();
  const [typeFilter, setTypeFilter] = useState("All");
  const [expanded, setExpanded] = useState<number | null>(null);

  const filtered = typeFilter === "All"
    ? activities
    : activities.filter((a) => a.ACTIVITY_TYPE === typeFilter);

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2">
        {TYPES.map((t) => (
          <button
            key={t}
            onClick={() => setTypeFilter(t)}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors cursor-pointer ${
              typeFilter === t ? "bg-blue-500/20 text-blue-400" : "text-slate-400 hover:bg-white/5"
            }`}
          >
            {t}
          </button>
        ))}
        <span className="text-xs text-slate-500 ml-auto">{filtered.length} records</span>
      </div>

      {isLoading && (
        <div className="space-y-2">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="skeleton h-12" />
          ))}
        </div>
      )}

      <div className="relative pl-8">
        {/* Vertical timeline line */}
        <div className="absolute left-3 top-0 bottom-0 w-px bg-blue-500/30" />

        {filtered.map((a, i) => {
          const dotColor = DOT_COLORS[a.ACTIVITY_TYPE] || "#64748b";
          const tc = TYPE_STYLES[a.ACTIVITY_TYPE] || TYPE_STYLES.Email;
          const cc = CLASS_COLORS[a.CLASSIFICATION] || CLASS_COLORS.Routine;
          const isExpanded = expanded === a.ACTIVITY_ID;

          return (
            <motion.div
              key={a.ACTIVITY_ID}
              initial={{ opacity: 0, x: -12 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: Math.min(i * 0.05, 0.5) }}
              className="relative mb-2"
            >
              {/* Timeline dot */}
              <div
                className="absolute -left-5 top-4 w-2.5 h-2.5 rounded-full border-2 border-navy-900"
                style={{ background: dotColor, boxShadow: `0 0 6px ${dotColor}60` }}
              />

              <button
                onClick={() => setExpanded(isExpanded ? null : a.ACTIVITY_ID)}
                className="w-full text-left glass !rounded-lg !p-3 hover:bg-white/[0.08] transition-all duration-200 cursor-pointer"
              >
                <div className="flex items-center gap-3">
                  <span className="text-xs text-slate-500 font-mono w-20 shrink-0">{a.ACTIVITY_DATE}</span>
                  <span className={`text-xs px-2 py-0.5 rounded-full font-medium w-16 text-center shrink-0 ${tc.bg} ${tc.text}`}>
                    {a.ACTIVITY_TYPE}
                  </span>
                  <span className="text-sm text-blue-400 w-44 shrink-0 truncate">{a.ORG_NAME}</span>
                  <span className="text-xs text-slate-300 flex-1 truncate">{a.SUMMARY}</span>
                  <span className={`text-[10px] font-medium shrink-0 ${cc}`}>{a.CLASSIFICATION}</span>
                  <ChevronDown
                    size={14}
                    className={`text-slate-500 shrink-0 transition-transform duration-200 ${isExpanded ? "rotate-180" : ""}`}
                  />
                </div>
              </button>

              <AnimatePresence>
                {isExpanded && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.2 }}
                    className="overflow-hidden"
                  >
                    <div className="glass-dark !rounded-lg !p-4 mt-1 ml-4 space-y-2">
                      <div className="grid grid-cols-2 gap-3 text-xs">
                        <div>
                          <span className="text-slate-500">Organization</span>
                          <p className="text-white mt-0.5">{a.ORG_NAME}</p>
                        </div>
                        <div>
                          <span className="text-slate-500">Participants</span>
                          <p className="text-slate-300 mt-0.5">{a.PARTICIPANTS || "Not recorded"}</p>
                        </div>
                        <div className="col-span-2">
                          <span className="text-slate-500">Summary</span>
                          <p className="text-slate-300 mt-0.5">{a.SUMMARY}</p>
                        </div>
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
