"use client";

import { ReactNode } from "react";
import { motion } from "framer-motion";

interface GlassCardProps {
  children: ReactNode;
  className?: string;
  glow?: boolean;
  dark?: boolean;
  animate?: boolean;
  delay?: number;
}

export default function GlassCard({
  children,
  className = "",
  glow = false,
  dark = false,
  animate = true,
  delay = 0,
}: GlassCardProps) {
  const baseClass = dark ? "glass-dark" : "glass";
  const glowClass = glow ? "glow-blue" : "";

  if (!animate) {
    return (
      <div className={`${baseClass} ${glowClass} p-6 transition-all duration-300 hover:bg-white/[0.08] hover:border-white/20 hover:shadow-[0_0_30px_rgba(59,130,246,0.1)] ${className}`}>
        {children}
      </div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay, ease: "easeOut" }}
      className={`${baseClass} ${glowClass} p-6 transition-all duration-300 hover:bg-white/[0.08] hover:border-white/20 hover:shadow-[0_0_30px_rgba(59,130,246,0.1)] ${className}`}
    >
      {children}
    </motion.div>
  );
}
