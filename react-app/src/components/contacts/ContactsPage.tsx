"use client";

import { useState, useEffect } from "react";
import { Search, X, Sparkles, MapPin, User, Calendar, Building2, Clock } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import GlassCard from "../shared/GlassCard";
import SignalBadge from "../shared/SignalBadge";
import { showToast } from "../shared/Toast";
import type { CrmContact, ContactDetail } from "@/lib/types";
import type { PageId } from "../layout/Sidebar";
import { apiCall } from "@/lib/api";

const STATUS_FILTERS = ["All", "Warm", "Strategic", "Neutral", "Cool"];

interface ContactsPageProps {
  onNavigate?: (page: PageId) => void;
}

export default function ContactsPage({ onNavigate }: ContactsPageProps) {
  const [contacts, setContacts] = useState<CrmContact[]>([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");
  const [selectedOrg, setSelectedOrg] = useState<string | null>(null);
  const [detail, setDetail] = useState<ContactDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  useEffect(() => {
    apiCall<CrmContact[]>("getContacts").then(setContacts).catch(console.error);
  }, []);

  useEffect(() => {
    if (!selectedOrg) { setDetail(null); return; }
    setDetailLoading(true);
    apiCall<ContactDetail>("getContactDetail", { orgName: selectedOrg })
      .then(setDetail)
      .catch((err) => showToast(err.message))
      .finally(() => setDetailLoading(false));
  }, [selectedOrg]);

  const filtered = contacts.filter((c) => {
    const matchSearch = c.ORG_NAME.toLowerCase().includes(search.toLowerCase()) ||
      c.SECTOR.toLowerCase().includes(search.toLowerCase());
    const matchStatus = statusFilter === "All" || c.RELATIONSHIP_STATUS === statusFilter;
    return matchSearch && matchStatus;
  });

  return (
    <div className="flex gap-6">
      <div className="flex-1 space-y-4">
        <div className="flex items-center gap-3">
          <div className="flex-1 flex items-center gap-2 glass px-3 py-2">
            <Search size={14} className="text-slate-500" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search contacts..."
              className="bg-transparent text-sm text-white placeholder-slate-500 outline-none w-full"
            />
          </div>
          <div className="flex gap-1">
            {STATUS_FILTERS.map((s) => (
              <button
                key={s}
                onClick={() => setStatusFilter(s)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                  statusFilter === s ? "bg-blue-500/20 text-blue-400" : "text-slate-400 hover:bg-white/5"
                }`}
              >
                {s}
              </button>
            ))}
          </div>
        </div>

        <div className="glass overflow-hidden">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-blue-500/10">
                <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Organization</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Sector</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Country</th>
                <th className="text-center px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Status</th>
                <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Last Contact</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((c) => (
                <tr
                  key={c.ORG_NAME}
                  onClick={() => setSelectedOrg(c.ORG_NAME)}
                  className={`border-b border-blue-500/5 cursor-pointer transition-colors hover:bg-blue-500/5 ${
                    selectedOrg === c.ORG_NAME ? "bg-blue-500/10 border-l-2 border-l-blue-500" : ""
                  }`}
                >
                  <td className="px-4 py-2.5 text-white font-medium">{c.ORG_NAME}</td>
                  <td className="px-4 py-2.5 text-slate-400 text-xs">{c.SECTOR}</td>
                  <td className="px-4 py-2.5 text-slate-400">{c.COUNTRY}</td>
                  <td className="px-4 py-2.5 text-center"><SignalBadge signal={c.RELATIONSHIP_STATUS} pulse={false} /></td>
                  <td className="px-4 py-2.5 text-slate-500 text-xs font-mono">{c.LAST_INTERACTION_DATE}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      <AnimatePresence>
        {selectedOrg && (
          <motion.div
            initial={{ opacity: 0, x: 24 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 24 }}
            className="w-96 shrink-0"
          >
            <GlassCard className="sticky top-6 space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-semibold text-white">{selectedOrg}</h3>
                <button onClick={() => setSelectedOrg(null)} className="text-slate-400 hover:text-white">
                  <X size={14} />
                </button>
              </div>

              {detailLoading && <div className="skeleton h-32" />}

              {detail && !detailLoading && (
                <>
                  <div className="space-y-2 text-sm">
                    <p className="text-xs text-slate-400">{detail.contact.ORG_DESCRIPTION}</p>
                    <div className="grid grid-cols-2 gap-2 text-xs">
                      <div className="flex items-center gap-1.5 text-slate-300">
                        <Building2 size={12} className="text-slate-500" />{detail.contact.SECTOR}
                      </div>
                      <div className="flex items-center gap-1.5 text-slate-300">
                        <MapPin size={12} className="text-slate-500" />{detail.contact.HQ_CITY}
                      </div>
                      <div className="flex items-center gap-1.5 text-slate-300">
                        <User size={12} className="text-slate-500" />{detail.contact.PRIMARY_CONTACT_NAME}
                      </div>
                      <div className="flex items-center gap-1.5 text-slate-300">
                        <Calendar size={12} className="text-slate-500" />{detail.contact.LAST_INTERACTION_DATE}
                      </div>
                    </div>
                  </div>

                  {detail.activities.length > 0 && (
                    <div>
                      <p className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest mb-2">Recent Activity</p>
                      <div className="space-y-1.5">
                        {detail.activities.map((a) => (
                          <div key={a.ACTIVITY_ID} className="flex items-start gap-2 text-xs">
                            <Clock size={10} className="text-slate-500 mt-0.5 shrink-0" />
                            <div>
                              <span className="text-slate-500 font-mono">{a.ACTIVITY_DATE}</span>
                              <span className="text-slate-400 mx-1">—</span>
                              <span className="text-slate-300">{a.SUMMARY}</span>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {detail.intel.length > 0 && (
                    <div>
                      <p className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest mb-2">Sector Intel</p>
                      <div className="space-y-1.5">
                        {detail.intel.map((i) => (
                          <div key={i.INTEL_ID} className="text-xs">
                            <p className="text-slate-300 font-medium">{i.HEADLINE}</p>
                            <p className="text-slate-500">{i.SOURCE} — {i.INTEL_DATE}</p>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  <button
                    onClick={() => onNavigate?.("crm")}
                    className="w-full flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-medium transition-colors"
                  >
                    <Sparkles size={12} />
                    Enrich with AI
                  </button>
                </>
              )}
            </GlassCard>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
