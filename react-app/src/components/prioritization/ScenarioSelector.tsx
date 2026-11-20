"use client";

import GlassCard from "../shared/GlassCard";
import type { MissionPriority } from "@/lib/types";

const colorMap: Record<number, string> = {
  1: "border-blue-500/40 hover:border-blue-500/60",
  2: "border-amber-500/40 hover:border-amber-500/60",
  3: "border-emerald-500/40 hover:border-emerald-500/60",
  4: "border-rose-500/40 hover:border-rose-500/60",
};

const dotColor: Record<number, string> = {
  1: "bg-blue-500",
  2: "bg-amber-500",
  3: "bg-emerald-500",
  4: "bg-rose-500",
};

interface ScenarioSelectorProps {
  priorities: MissionPriority[];
  selected: MissionPriority | null;
  onSelect: (p: MissionPriority) => void;
}

export default function ScenarioSelector({ priorities, selected, onSelect }: ScenarioSelectorProps) {
  return (
    <div>
      <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 block">
        Mission Priority Scenario
      </label>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {priorities.map((p, i) => {
          const isSelected = selected?.PRIORITY_ID === p.PRIORITY_ID;
          const idx = (i % 4) + 1;
          return (
            <button
              key={p.PRIORITY_ID}
              onClick={() => onSelect(p)}
              className={`text-left transition-all ${isSelected ? "ring-1 ring-blue-500/50" : ""}`}
            >
              <GlassCard
                animate={false}
                className={`!p-4 cursor-pointer border ${colorMap[idx] || colorMap[1]} ${isSelected ? "glow-blue-sm" : ""}`}
              >
                <div className="flex items-start gap-2">
                  <span className={`w-2 h-2 rounded-full mt-1.5 shrink-0 ${dotColor[idx] || dotColor[1]}`} />
                  <div>
                    <h4 className="text-sm font-medium text-white">{p.PRIORITY_NAME}</h4>
                    <p className="text-xs text-slate-400 mt-1 line-clamp-2">{p.DESCRIPTION}</p>
                  </div>
                </div>
              </GlassCard>
            </button>
          );
        })}
      </div>
    </div>
  );
}
