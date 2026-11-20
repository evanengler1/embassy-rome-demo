"use client";

import { motion } from "framer-motion";
import RankedCard from "./RankedCard";
import type { PrioritizationResult } from "@/lib/types";

interface PriorityResultsProps {
  result: PrioritizationResult;
}

export default function PriorityResults({ result }: PriorityResultsProps) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="space-y-4"
    >
      <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
        Top 8 Priority Engagements
      </h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {result.ranked.map((item, i) => (
          <RankedCard key={item.rank} item={item} delay={i * 0.05} />
        ))}
      </div>
      {result.deprioritized_note && (
        <p className="text-xs text-slate-500 italic mt-4 px-1">
          {result.deprioritized_note}
        </p>
      )}
    </motion.div>
  );
}
