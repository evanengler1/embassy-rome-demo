"use client";

import { useState } from "react";
import { Sparkles, Users } from "lucide-react";
import { AnimatePresence } from "framer-motion";
import ContactSelector from "./ContactSelector";
import RawContactCard from "./RawContactCard";
import EnrichedProfile from "./EnrichedProfile";
import SkeletonLoader from "../shared/SkeletonLoader";
import { showToast } from "../shared/Toast";
import type { CrmContact, EnrichmentResult } from "@/lib/types";
import { apiCall } from "@/lib/api";

export default function CrmTab() {
  const [contact, setContact] = useState<CrmContact | null>(null);
  const [result, setResult] = useState<EnrichmentResult | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleEnrich() {
    if (!contact) return;
    setLoading(true);
    setResult(null);
    try {
      const data = await apiCall<EnrichmentResult>("enrichContact", { orgName: contact.ORG_NAME });
      setResult(data);
    } catch (err) {
      showToast(err instanceof Error ? err.message : "Enrichment failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div className="space-y-4">
        <ContactSelector
          selectedOrg={contact?.ORG_NAME ?? null}
          onSelect={(c) => { setContact(c); setResult(null); }}
        />

        <AnimatePresence mode="wait">
          {contact && <RawContactCard key={contact.ORG_NAME} contact={contact} />}
        </AnimatePresence>

        {contact && (
          <button
            onClick={handleEnrich}
            disabled={loading}
            className="w-full flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium text-sm transition-all glow-blue-sm hover:glow-blue"
          >
            {loading ? (
              <span className="loading-dots">Analyzing via Cortex</span>
            ) : (
              <>
                <Sparkles size={16} />
                Enrich with Cortex
              </>
            )}
          </button>
        )}

        {!contact && (
          <div className="flex flex-col items-center justify-center py-16 text-center">
            <Users size={40} className="text-slate-600 mb-3" />
            <p className="text-sm text-slate-500">Select a contact and enrich to begin.</p>
          </div>
        )}
      </div>

      <div>
        {loading && (
          <div className="space-y-4">
            <div className="glass p-6"><SkeletonLoader lines={4} /></div>
            <div className="glass p-6"><SkeletonLoader lines={3} /></div>
            <div className="glass p-6"><SkeletonLoader lines={2} /></div>
          </div>
        )}
        <AnimatePresence mode="wait">
          {result && !loading && <EnrichedProfile key="enriched" result={result} />}
        </AnimatePresence>
      </div>
    </div>
  );
}
