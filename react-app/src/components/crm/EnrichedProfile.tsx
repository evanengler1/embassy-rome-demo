"use client";

import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import GlassCard from "../shared/GlassCard";
import ProgressGauge from "../shared/ProgressGauge";
import SignalBadge from "../shared/SignalBadge";
import type { EnrichmentResult } from "@/lib/types";

interface EnrichedProfileProps {
  result: EnrichmentResult;
}

export default function EnrichedProfile({ result }: EnrichedProfileProps) {
  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
      className="space-y-4"
    >
      <GlassCard glow delay={0.1}>
        <div className="flex items-start gap-6">
          <ProgressGauge value={result.alignment_score} size={100} strokeWidth={6} />
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-2">
              <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-wider">
                Alignment Score
              </h3>
              <SignalBadge signal={result.relationship_signal} />
            </div>
            <p className="text-sm text-slate-300 mt-2">
              <span className="text-xs text-slate-500 uppercase tracking-wider block mb-1">Sector Rank</span>
              {result.sector_rank}
            </p>
          </div>
        </div>
      </GlassCard>

      <GlassCard delay={0.2} className="border-l-2 border-l-blue-500/50">
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">
          Intelligence Summary
        </h4>
        <p className="text-sm text-slate-200 leading-relaxed">{result.intelligence_summary}</p>
      </GlassCard>

      <GlassCard delay={0.3} className="border-l-2 border-l-amber-500/50">
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <ArrowRight size={14} className="text-amber-400" />
          Recommended Action
        </h4>
        <p className="text-sm text-slate-200 leading-relaxed">{result.recommended_action}</p>
      </GlassCard>
    </motion.div>
  );
}
