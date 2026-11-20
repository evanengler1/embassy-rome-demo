"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import {
  LayoutDashboard,
  Users,
  Clock,
  Newspaper,
  Sparkles,
  Target,
  Scale,
  Database,
  PanelLeftClose,
  PanelLeftOpen,
} from "lucide-react";

export type PageId =
  | "overview"
  | "contacts"
  | "activity"
  | "intelligence"
  | "crm"
  | "prioritization"
  | "alignment"
  | "architecture";

const dataNav: { id: PageId; label: string; icon: typeof LayoutDashboard }[] = [
  { id: "overview", label: "Overview", icon: LayoutDashboard },
  { id: "contacts", label: "Contacts", icon: Users },
  { id: "activity", label: "Activity", icon: Clock },
  { id: "intelligence", label: "Intelligence", icon: Newspaper },
];

const aiNav: { id: PageId; label: string; icon: typeof Sparkles }[] = [
  { id: "crm", label: "CRM Enrichment", icon: Sparkles },
  { id: "prioritization", label: "Prioritization", icon: Target },
  { id: "alignment", label: "Alignment", icon: Scale },
];

const platformNav: { id: PageId; label: string; icon: typeof Database }[] = [
  { id: "architecture", label: "Data Architecture", icon: Database },
];

interface SidebarProps {
  activePage: PageId;
  onNavigate: (page: PageId) => void;
}

function NavItem({
  id,
  label,
  icon: Icon,
  active,
  collapsed,
  onClick,
}: {
  id: string;
  label: string;
  icon: typeof LayoutDashboard;
  active: boolean;
  collapsed: boolean;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors relative ${
        active
          ? "text-white bg-blue-500/10"
          : "text-slate-400 hover:text-slate-200 hover:bg-white/5"
      }`}
    >
      {active && (
        <motion.div
          layoutId="nav-active"
          className="absolute left-0 top-1 bottom-1 w-0.5 rounded-full bg-blue-500"
          transition={{ type: "spring", stiffness: 400, damping: 30 }}
        />
      )}
      <Icon size={16} className={active ? "text-blue-400" : ""} />
      {!collapsed && <span>{label}</span>}
    </button>
  );
}

export default function Sidebar({ activePage, onNavigate }: SidebarProps) {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <motion.aside
      initial={false}
      animate={{ width: collapsed ? 56 : 240 }}
      transition={{ duration: 0.2, ease: "easeInOut" }}
      className="glass-dark shrink-0 overflow-hidden flex flex-col border-r border-blue-500/10"
    >
      <div className="p-3 flex items-center justify-end border-b border-blue-500/10">
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="text-slate-400 hover:text-white transition-colors p-1"
        >
          {collapsed ? <PanelLeftOpen size={16} /> : <PanelLeftClose size={16} />}
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-2 space-y-6">
        <div>
          {!collapsed && (
            <p className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest px-3 mb-2">
              Data
            </p>
          )}
          <div className="space-y-0.5">
            {dataNav.map((item) => (
              <NavItem
                key={item.id}
                {...item}
                active={activePage === item.id}
                collapsed={collapsed}
                onClick={() => onNavigate(item.id)}
              />
            ))}
          </div>
        </div>

        <div>
          {!collapsed && (
            <p className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest px-3 mb-2">
              AI Tools
            </p>
          )}
          <div className="space-y-0.5">
            {aiNav.map((item) => (
              <NavItem
                key={item.id}
                {...item}
                active={activePage === item.id}
                collapsed={collapsed}
                onClick={() => onNavigate(item.id)}
              />
            ))}
          </div>
        </div>

        <div>
          {!collapsed && (
            <p className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest px-3 mb-2">
              Platform
            </p>
          )}
          <div className="space-y-0.5">
            {platformNav.map((item) => (
              <NavItem
                key={item.id}
                {...item}
                active={activePage === item.id}
                collapsed={collapsed}
                onClick={() => onNavigate(item.id)}
              />
            ))}
          </div>
        </div>
      </div>
    </motion.aside>
  );
}
