"use client";

import { useState, useEffect } from "react";
import { Search, ChevronDown } from "lucide-react";
import type { CrmContact } from "@/lib/types";
import { apiCall } from "@/lib/api";

interface ContactSelectorProps {
  selectedOrg: string | null;
  onSelect: (contact: CrmContact) => void;
}

export default function ContactSelector({ selectedOrg, onSelect }: ContactSelectorProps) {
  const [contacts, setContacts] = useState<CrmContact[]>([]);
  const [search, setSearch] = useState("");
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiCall<CrmContact[]>("getContacts")
      .then(setContacts)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const filtered = contacts.filter((c) =>
    c.ORG_NAME.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="relative">
      <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2 block">
        Select Organization
      </label>
      <button
        onClick={() => setOpen(!open)}
        className="w-full glass flex items-center justify-between px-4 py-3 text-left text-sm hover:border-blue-500/30 transition-colors"
      >
        <span className={selectedOrg ? "text-white" : "text-slate-500"}>
          {loading ? "Loading contacts..." : selectedOrg || "Choose a stakeholder organization..."}
        </span>
        <ChevronDown size={16} className={`text-slate-400 transition-transform ${open ? "rotate-180" : ""}`} />
      </button>

      {open && (
        <div className="absolute z-30 w-full mt-1 glass-dark max-h-72 overflow-hidden flex flex-col">
          <div className="p-2 border-b border-blue-500/10">
            <div className="flex items-center gap-2 px-2 py-1.5 rounded bg-navy-800/50">
              <Search size={14} className="text-slate-500" />
              <input
                type="text"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder="Search..."
                className="bg-transparent text-sm text-white placeholder-slate-500 outline-none w-full"
                autoFocus
              />
            </div>
          </div>
          <div className="overflow-y-auto max-h-56">
            {filtered.map((c) => (
              <button
                key={c.ORG_NAME}
                onClick={() => { onSelect(c); setOpen(false); setSearch(""); }}
                className={`w-full text-left px-4 py-2.5 text-sm hover:bg-blue-500/10 transition-colors flex items-center justify-between ${
                  selectedOrg === c.ORG_NAME ? "text-blue-400 bg-blue-500/5" : "text-slate-300"
                }`}
              >
                <span>{c.ORG_NAME}</span>
                <span className="text-xs text-slate-500">{c.SECTOR}</span>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
