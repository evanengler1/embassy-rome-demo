"use client";

import { motion } from "framer-motion";

type Signal = "Warm" | "Neutral" | "Cool" | "Strategic";

const signalColors: Record<Signal, { bg: string; text: string; glow: string }> = {
  Warm: { bg: "bg-emerald-500/20", text: "text-emerald-400", glow: "shadow-emerald-500/30" },
  Neutral: { bg: "bg-slate-500/20", text: "text-slate-300", glow: "shadow-slate-500/30" },
  Cool: { bg: "bg-blue-500/20", text: "text-blue-400", glow: "shadow-blue-500/30" },
  Strategic: { bg: "bg-amber-500/20", text: "text-amber-400", glow: "shadow-amber-500/30" },
};

interface SignalBadgeProps {
  signal: string;
  pulse?: boolean;
}

export default function SignalBadge({ signal, pulse = true }: SignalBadgeProps) {
  const key = signal as Signal;
  const colors = signalColors[key] || signalColors.Neutral;

  return (
    <motion.span
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      className={`inline-flex items-center justify-center px-3 py-1 rounded-full text-xs font-medium ${colors.bg} ${colors.text} ${pulse ? "pulse-glow" : ""}`}
      style={pulse ? { boxShadow: `0 0 12px ${colors.glow}` } : undefined}
    >
      {signal}
    </motion.span>
  );
}
