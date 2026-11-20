"use client";

import SearchBar from "../shared/SearchBar";
import type { PageId } from "./Sidebar";

interface HeaderProps {
  onNavigate?: (page: PageId) => void;
}

export default function Header({ onNavigate }: HeaderProps) {
  return (
    <header className="border-b border-blue-500/10 bg-navy-950/80 backdrop-blur-md sticky top-0 z-40">
      <div className="px-6 py-4 flex items-center justify-between">
        <div>
          <h1 className="text-lg font-semibold text-white tracking-tight">
            US Embassy in Rome
          </h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Diplomatic Intelligence Platform
          </p>
        </div>
        <SearchBar onSelect={() => onNavigate?.("contacts")} />
      </div>
    </header>
  );
}
