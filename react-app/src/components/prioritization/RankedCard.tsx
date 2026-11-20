"use client";

import { motion } from "framer-motion";
import { Quote } from "lucide-react";
import AnimatedNumber from "../shared/AnimatedNumber";
import type { RankedContact } from "@/lib/types";

interface RankedCardProps {
  item: RankedContact;
  delay: number;
}

function scoreColor(score: number): string {
  if (score >= 70) return "bg-emerald-500";
  if (score >= 40) return "bg-amber-500";
  return "bg-rose-500";
}

export default function RankedCard({ item, delay }: RankedCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay, ease: "easeOut" }}
      className="glass p-4 space-y-3"
    >
      <div className="flex items-start gap-3">
        <span className="text-2xl font-bold font-mono text-blue-400 leading-none">
          {item.rank}
        </span>
        <div className="flex-1 min-w-0">
          <h4 className="text-sm font-medium text-white truncate">{item.name}</h4>
          <p className="text-xs text-slate-400">{item.org}</p>
        </div>
        <div className="text-right shrink-0">
          <AnimatedNumber value={item.score} className="text-lg font-bold text-white" duration={0.8} />
          <div className="w-16 h-1.5 rounded-full bg-navy-700 mt-1 overflow-hidden">
            <motion.div
              className={`h-full rounded-full ${scoreColor(item.score)}`}
              initial={{ width: 0 }}
              animate={{ width: `${item.score}%` }}
              transition={{ duration: 0.8, delay: delay + 0.2, ease: "easeOut" }}
            />
          </div>
        </div>
      </div>

      <p className="text-xs text-slate-300 leading-relaxed">{item.rationale}</p>

      <div className="flex items-start gap-2 p-2.5 rounded-lg bg-navy-800/50 border border-blue-500/10">
        <Quote size={12} className="text-blue-400 shrink-0 mt-0.5" />
        <p className="text-xs text-slate-200 italic leading-relaxed">{item.opening_line}</p>
      </div>
    </motion.div>
  );
}
