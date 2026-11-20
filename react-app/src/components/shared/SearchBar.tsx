"use client";

import { useState, useRef, useEffect } from "react";
import { Search, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { apiCall } from "@/lib/api";
import type { CrmContact } from "@/lib/types";

interface SearchBarProps {
  onSelect: (orgName: string) => void;
}

export default function SearchBar({ onSelect }: SearchBarProps) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<CrmContact[]>([]);
  const [allContacts, setAllContacts] = useState<CrmContact[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    apiCall<CrmContact[]>("getContacts").then(setAllContacts).catch(console.error);
  }, []);

  useEffect(() => {
    if (query.length < 2) { setResults([]); return; }
    const q = query.toLowerCase();
    setResults(
      allContacts.filter(
        (c) =>
          c.ORG_NAME.toLowerCase().includes(q) ||
          c.SECTOR?.toLowerCase().includes(q) ||
          c.COUNTRY?.toLowerCase().includes(q)
      ).slice(0, 6)
    );
  }, [query, allContacts]);

  useEffect(() => {
    if (open) inputRef.current?.focus();
  }, [open]);

  return (
    <div className="relative">
      {!open ? (
        <button onClick={() => setOpen(true)} className="p-2 rounded-lg text-slate-400 hover:text-white hover:bg-white/5 transition-colors cursor-pointer">
          <Search size={16} />
        </button>
      ) : (
        <div className="flex items-center gap-2">
          <div className="relative">
            <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
            <input
              ref={inputRef}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search contacts, orgs..."
              className="w-64 pl-9 pr-3 py-1.5 rounded-lg bg-white/5 border border-white/10 text-sm text-white placeholder:text-slate-500 focus:outline-none focus:border-blue-500/40 focus:shadow-[0_0_12px_rgba(59,130,246,0.2)] transition-all"
            />
          </div>
          <button onClick={() => { setOpen(false); setQuery(""); setResults([]); }} className="p-1.5 rounded-lg text-slate-500 hover:text-white hover:bg-white/5 transition-colors cursor-pointer">
            <X size={14} />
          </button>
        </div>
      )}

      <AnimatePresence>
        {results.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: -4, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -4, scale: 0.98 }}
            className="absolute top-full right-0 mt-2 w-80 glass-dark rounded-xl overflow-hidden z-50 shadow-xl"
          >
            {results.map((c) => (
              <button
                key={c.ORG_NAME}
                onClick={() => { onSelect(c.ORG_NAME); setOpen(false); setQuery(""); setResults([]); }}
                className="w-full text-left px-4 py-3 hover:bg-white/10 transition-colors border-b border-white/5 last:border-0 cursor-pointer"
              >
                <p className="text-sm text-white font-medium">{c.ORG_NAME}</p>
                <p className="text-xs text-slate-500">{c.SECTOR} &middot; {c.COUNTRY}</p>
              </button>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
