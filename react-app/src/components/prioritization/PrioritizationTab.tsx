"use client";

import { useState, useEffect } from "react";
import { Target, Calendar } from "lucide-react";
import { AnimatePresence } from "framer-motion";
import ScenarioSelector from "./ScenarioSelector";
import AttendeeTable from "./AttendeeTable";
import PriorityResults from "./PriorityResults";
import SkeletonLoader from "../shared/SkeletonLoader";
import { showToast } from "../shared/Toast";
import type { MissionPriority, SummitAttendee, PrioritizationResult } from "@/lib/types";
import { apiCall } from "@/lib/api";

export default function PrioritizationTab() {
  const [priorities, setPriorities] = useState<MissionPriority[]>([]);
  const [attendees, setAttendees] = useState<SummitAttendee[]>([]);
  const [selectedPriority, setSelectedPriority] = useState<MissionPriority | null>(null);
  const [result, setResult] = useState<PrioritizationResult | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    Promise.all([
      apiCall<MissionPriority[]>("getPriorities"),
      apiCall<SummitAttendee[]>("getAttendees"),
    ])
      .then(([p, a]) => { setPriorities(p); setAttendees(a); })
      .catch(console.error);
  }, []);

  async function handlePrioritize() {
    if (!selectedPriority) return;
    setLoading(true);
    setResult(null);
    try {
      const data = await apiCall<PrioritizationResult>("prioritize", {
        priorityId: selectedPriority.PRIORITY_ID,
      });
      setResult(data);
    } catch (err) {
      showToast(err instanceof Error ? err.message : "Prioritization failed");
    } finally {
      setLoading(false);
    }
  }

  const rankedNames = result ? result.ranked.map((r) => r.name.toLowerCase()) : [];

  return (
    <div className="space-y-6">
      <ScenarioSelector
        priorities={priorities}
        selected={selectedPriority}
        onSelect={(p) => { setSelectedPriority(p); setResult(null); }}
      />

      {selectedPriority && (
        <button
          onClick={handlePrioritize}
          disabled={loading}
          className="flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium text-sm transition-all glow-blue-sm hover:glow-blue"
        >
          {loading ? (
            <span className="loading-dots">Analyzing via Cortex</span>
          ) : (
            <>
              <Target size={16} />
              Prioritize Ambassador Bandwidth
            </>
          )}
        </button>
      )}

      {loading && (
        <div className="grid grid-cols-2 gap-4">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="glass p-6"><SkeletonLoader lines={4} /></div>
          ))}
        </div>
      )}

      <AnimatePresence mode="wait">
        {result && !loading && <PriorityResults key="results" result={result} />}
      </AnimatePresence>

      <AttendeeTable attendees={attendees} highlightedNames={rankedNames} />

      {!selectedPriority && attendees.length === 0 && (
        <div className="flex flex-col items-center justify-center py-16 text-center">
          <Calendar size={40} className="text-slate-600 mb-3" />
          <p className="text-sm text-slate-500">Select a mission priority to analyze summit attendees.</p>
        </div>
      )}
    </div>
  );
}
