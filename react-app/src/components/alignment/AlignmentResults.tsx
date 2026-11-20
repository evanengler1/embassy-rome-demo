"use client";

import { motion } from "framer-motion";
import { CheckCircle, AlertTriangle, Compass, Quote } from "lucide-react";
import GlassCard from "../shared/GlassCard";
import AnimatedNumber from "../shared/AnimatedNumber";
import type { AlignmentResult } from "@/lib/types";

function scoreGradient(score: number): string {
  if (score >= 70) return "from-emerald-500 to-emerald-400";
  if (score >= 40) return "from-amber-500 to-amber-400";
  return "from-rose-500 to-rose-400";
}

interface AlignmentResultsProps {
  result: AlignmentResult;
}

export default function AlignmentResults({ result }: AlignmentResultsProps) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="space-y-6"
    >
      {/* Hero Score */}
      <GlassCard glow delay={0.1} className="text-center">
        <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">
          Alignment Score
        </h3>
        <div className="flex items-center justify-center gap-2">
          <AnimatedNumber
            value={result.alignment_score}
            className="text-5xl font-bold text-white"
            suffix="%"
          />
        </div>
        <div className="w-full h-2 rounded-full bg-navy-700 mt-4 overflow-hidden">
          <motion.div
            className={`h-full rounded-full bg-gradient-to-r ${scoreGradient(result.alignment_score)}`}
            initial={{ width: 0 }}
            animate={{ width: `${result.alignment_score}%` }}
            transition={{ duration: 1, delay: 0.3, ease: "easeOut" }}
          />
        </div>
        <p className="text-sm text-blue-300 mt-3 font-medium">{result.label}</p>
      </GlassCard>

      {/* Agreements and Tensions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <GlassCard delay={0.2}>
          <h4 className="text-xs font-semibold text-emerald-400 uppercase tracking-wider mb-3">
            Points of Agreement
          </h4>
          <ul className="space-y-2.5">
            {result.agreements.map((item, i) => (
              <motion.li
                key={i}
                initial={{ opacity: 0, x: -12 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.3 + i * 0.05 }}
                className="flex items-start gap-2 text-sm text-slate-200"
              >
                <CheckCircle size={14} className="text-emerald-400 shrink-0 mt-0.5" />
                {item}
              </motion.li>
            ))}
          </ul>
        </GlassCard>

        <GlassCard delay={0.3}>
          <h4 className="text-xs font-semibold text-amber-400 uppercase tracking-wider mb-3">
            Points of Tension
          </h4>
          <ul className="space-y-2.5">
            {result.tensions.map((item, i) => (
              <motion.li
                key={i}
                initial={{ opacity: 0, x: -12 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.4 + i * 0.05 }}
                className="flex items-start gap-2 text-sm text-slate-200"
              >
                <AlertTriangle size={14} className="text-amber-400 shrink-0 mt-0.5" />
                {item}
              </motion.li>
            ))}
          </ul>
        </GlassCard>
      </div>

      {/* Diplomatic Approach */}
      <GlassCard delay={0.4} className="border-l-2 border-l-blue-500/50">
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <Compass size={14} className="text-blue-400" />
          Recommended Diplomatic Approach
        </h4>
        <p className="text-sm text-slate-200 leading-relaxed">{result.diplomatic_approach}</p>
      </GlassCard>

      {/* Talking Points */}
      <div>
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">
          Ambassador Talking Points
        </h4>
        <div className="space-y-3">
          {result.talking_points.map((point, i) => (
            <GlassCard key={i} delay={0.5 + i * 0.05} className="!p-4">
              <div className="flex items-start gap-3">
                <div className="flex items-center justify-center w-6 h-6 rounded-full bg-blue-500/20 text-blue-400 text-xs font-bold font-mono shrink-0">
                  {i + 1}
                </div>
                <div className="flex items-start gap-2 flex-1">
                  <Quote size={12} className="text-blue-400/50 shrink-0 mt-0.5" />
                  <p className="text-sm text-slate-200 leading-relaxed">{point}</p>
                </div>
              </div>
            </GlassCard>
          ))}
        </div>
      </div>
    </motion.div>
  );
}
