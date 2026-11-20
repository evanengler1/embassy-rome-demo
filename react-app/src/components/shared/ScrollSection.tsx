"use client";

import { useRef } from "react";
import { motion, useInView } from "framer-motion";

interface ScrollSectionProps {
  children: React.ReactNode;
  delay?: number;
  className?: string;
}

export default function ScrollSection({ children, delay = 0, className }: ScrollSectionProps) {
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 60 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 60 }}
      transition={{ duration: 0.8, delay, ease: "easeOut" }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
