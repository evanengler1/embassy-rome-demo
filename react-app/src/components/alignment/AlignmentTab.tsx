"use client";

import { useState, useEffect } from "react";
import { Scale, FileText } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";
import DocumentSelector from "./DocumentSelector";
import AlignmentResults from "./AlignmentResults";
import SkeletonLoader from "../shared/SkeletonLoader";
import { showToast } from "../shared/Toast";
import type { PolicyDocument, AlignmentResult } from "@/lib/types";
import { apiCall } from "@/lib/api";

export default function AlignmentTab() {
  const [documents, setDocuments] = useState<PolicyDocument[]>([]);
  const [internalDoc, setInternalDoc] = useState<PolicyDocument | null>(null);
  const [externalDoc, setExternalDoc] = useState<PolicyDocument | null>(null);
  const [result, setResult] = useState<AlignmentResult | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    apiCall<PolicyDocument[]>("getDocuments")
      .then(setDocuments)
      .catch(console.error);
  }, []);

  const internalDocs = documents.filter((d) => d.CLASSIFICATION === "Internal");
  const externalDocs = documents.filter((d) => d.CLASSIFICATION === "External");

  async function handleAnalyze() {
    if (!internalDoc || !externalDoc) return;
    setLoading(true);
    setResult(null);
    try {
      const data = await apiCall<AlignmentResult>("analyzeAlignment", {
        internalDocId: internalDoc.DOC_ID,
        externalDocId: externalDoc.DOC_ID,
      });
      setResult(data);
    } catch (err) {
      showToast(err instanceof Error ? err.message : "Analysis failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-6">
      <DocumentSelector
        internalDocs={internalDocs}
        externalDocs={externalDocs}
        selectedInternal={internalDoc}
        selectedExternal={externalDoc}
        onSelectInternal={(d) => { setInternalDoc(d); setResult(null); }}
        onSelectExternal={(d) => { setExternalDoc(d); setResult(null); }}
      />

      {internalDoc && externalDoc && (
        <div className="flex justify-center">
          <button
            onClick={handleAnalyze}
            disabled={loading}
            className="flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium text-sm transition-all glow-blue-sm hover:glow-blue"
          >
            {loading ? (
              <span className="loading-dots">Analyzing via Cortex</span>
            ) : (
              <>
                <Scale size={16} />
                Analyze Alignment
              </>
            )}
          </button>
        </div>
      )}

      {loading && (
        <div className="space-y-4">
          <div className="glass p-6"><SkeletonLoader lines={2} /></div>
          <div className="grid grid-cols-2 gap-4">
            <div className="glass p-6"><SkeletonLoader lines={4} /></div>
            <div className="glass p-6"><SkeletonLoader lines={4} /></div>
          </div>
          <div className="glass p-6"><SkeletonLoader lines={3} /></div>
        </div>
      )}

      <AnimatePresence mode="wait">
        {result && !loading && <AlignmentResults key="results" result={result} />}
      </AnimatePresence>

      {!internalDoc && !externalDoc && documents.length === 0 && (
        <div className="flex flex-col items-center justify-center py-16 text-center">
          <FileText size={40} className="text-slate-600 mb-3" />
          <p className="text-sm text-slate-500">Select an internal and external document to compare.</p>
        </div>
      )}
    </div>
  );
}
