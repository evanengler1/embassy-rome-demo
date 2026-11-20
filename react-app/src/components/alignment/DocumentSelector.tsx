"use client";

import { FileText, Zap } from "lucide-react";
import GlassCard from "../shared/GlassCard";
import type { PolicyDocument } from "@/lib/types";

interface DocumentSelectorProps {
  internalDocs: PolicyDocument[];
  externalDocs: PolicyDocument[];
  selectedInternal: PolicyDocument | null;
  selectedExternal: PolicyDocument | null;
  onSelectInternal: (doc: PolicyDocument) => void;
  onSelectExternal: (doc: PolicyDocument) => void;
}

function DocCard({
  doc,
  selected,
  onSelect,
}: {
  doc: PolicyDocument;
  selected: boolean;
  onSelect: () => void;
}) {
  return (
    <button
      onClick={onSelect}
      className={`text-left w-full transition-all ${selected ? "ring-1 ring-blue-500/50" : ""}`}
    >
      <GlassCard
        animate={false}
        className={`!p-4 cursor-pointer ${selected ? "glow-blue-sm" : ""}`}
      >
        <div className="flex items-start gap-3">
          <FileText size={16} className="text-blue-400 shrink-0 mt-0.5" />
          <div className="min-w-0">
            <h4 className="text-sm font-medium text-white truncate">{doc.DOC_TITLE}</h4>
            <p className="text-xs text-slate-400 mt-0.5">{doc.DOC_TYPE} — {doc.ISSUER}</p>
            <p className="text-xs text-slate-500 mt-1 line-clamp-2">{doc.SUMMARY}</p>
          </div>
        </div>
      </GlassCard>
    </button>
  );
}

export default function DocumentSelector({
  internalDocs,
  externalDocs,
  selectedInternal,
  selectedExternal,
  onSelectInternal,
  onSelectExternal,
}: DocumentSelectorProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-[1fr_auto_1fr] gap-4 items-start">
      <div>
        <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 block">
          U.S. / Administration Documents
        </label>
        <div className="space-y-2">
          {internalDocs.map((d) => (
            <DocCard
              key={d.DOC_ID}
              doc={d}
              selected={selectedInternal?.DOC_ID === d.DOC_ID}
              onSelect={() => onSelectInternal(d)}
            />
          ))}
        </div>
      </div>

      <div className="hidden md:flex flex-col items-center justify-center self-center py-8">
        <div className="w-px h-12 bg-gradient-to-b from-transparent via-blue-500/40 to-transparent" />
        <div className="my-2 px-3 py-1.5 rounded-full glass text-xs font-semibold text-blue-400">
          VS
        </div>
        <div className="w-px h-12 bg-gradient-to-b from-transparent via-blue-500/40 to-transparent" />
      </div>

      <div>
        <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 block">
          External / Partner Documents
        </label>
        <div className="space-y-2">
          {externalDocs.map((d) => (
            <DocCard
              key={d.DOC_ID}
              doc={d}
              selected={selectedExternal?.DOC_ID === d.DOC_ID}
              onSelect={() => onSelectExternal(d)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
