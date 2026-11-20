"use client";

import { Users, FileStack, Newspaper, FileText, TrendingUp } from "lucide-react";
import { motion } from "framer-motion";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from "recharts";
import GlassCard from "../shared/GlassCard";
import AnimatedNumber from "../shared/AnimatedNumber";
import ScrollSection from "../shared/ScrollSection";
import { useOverviewStats } from "@/lib/queries";

const PIE_COLORS: Record<string, string> = {
  Warm: "#10b981",
  Strategic: "#f59e0b",
  Neutral: "#64748b",
  Cool: "#3b82f6",
};

const TYPE_COLORS: Record<string, string> = {
  Meeting: "#3b82f6",
  Call: "#10b981",
  Cable: "#f59e0b",
  Event: "#f43f5e",
  Email: "#64748b",
};

function KpiCard({ label, value, icon: Icon, delay }: { label: string; value: number; icon: typeof Users; delay: number }) {
  return (
    <GlassCard delay={delay} className="!p-5">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-xs text-slate-400 uppercase tracking-wider">{label}</p>
          <AnimatedNumber value={value} className="text-3xl font-bold text-white mt-1" />
        </div>
        <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
          <Icon size={20} className="text-blue-400" />
        </div>
      </div>
    </GlassCard>
  );
}

export default function OverviewPage() {
  const { data: stats } = useOverviewStats();

  if (!stats) {
    return (
      <div className="grid grid-cols-4 gap-4">
        {Array.from({ length: 4 }).map((_, i) => (
          <div key={i} className="glass p-5"><div className="skeleton h-16" /></div>
        ))}
      </div>
    );
  }

  const pieData = stats.relationship_dist.map((d) => ({
    name: d.RELATIONSHIP_STATUS,
    value: d.CNT,
  }));

  const barData = stats.activity_by_type.map((d) => ({
    type: d.ACTIVITY_TYPE,
    count: d.CNT,
    fill: TYPE_COLORS[d.ACTIVITY_TYPE] || "#3b82f6",
  }));

  return (
    <div className="space-y-6">
      <div className="gradient-mesh rounded-2xl px-6 py-8 -mx-2">
        <h2 className="gradient-text text-3xl font-bold tracking-tight mb-1">US Embassy in Rome</h2>
        <p className="text-sm text-slate-400">Diplomatic Intelligence Overview</p>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
        <KpiCard label="Contacts" value={stats.contact_count} icon={Users} delay={0} />
        <KpiCard label="Activities" value={stats.activity_count} icon={FileStack} delay={0.05} />
        <KpiCard label="Intel Records" value={stats.intel_count} icon={Newspaper} delay={0.1} />
        <KpiCard label="Policy Documents" value={stats.policy_count} icon={FileText} delay={0.15} />
        </div>
      </div>

      <ScrollSection>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <GlassCard delay={0.2}>
          <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">
            Activity by Type
          </h3>
          <div className="h-48">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData} layout="vertical" margin={{ left: 60, right: 16 }}>
                <XAxis type="number" tick={{ fill: "#64748b", fontSize: 12 }} axisLine={false} tickLine={false} />
                <YAxis type="category" dataKey="type" tick={{ fill: "#94a3b8", fontSize: 12 }} axisLine={false} tickLine={false} />
                <Tooltip contentStyle={{ background: "#111827", border: "1px solid rgba(59,130,246,0.2)", borderRadius: 8, color: "#f8fafc", fontSize: 12 }} labelStyle={{ color: "#f8fafc" }} itemStyle={{ color: "#cbd5e1" }} />
                <Bar dataKey="count" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </GlassCard>

        <GlassCard delay={0.25}>
          <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">
            Relationship Distribution
          </h3>
          <div className="h-48 flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={50}
                  outerRadius={70}
                  dataKey="value"
                  paddingAngle={3}
                  stroke="none"
                >
                  {pieData.map((entry) => (
                    <Cell key={entry.name} fill={PIE_COLORS[entry.name] || "#64748b"} />
                  ))}
                </Pie>
                <Tooltip contentStyle={{ background: "#111827", border: "1px solid rgba(59,130,246,0.2)", borderRadius: 8, color: "#f8fafc", fontSize: 12 }} labelStyle={{ color: "#f8fafc" }} itemStyle={{ color: "#cbd5e1" }} />
              </PieChart>
            </ResponsiveContainer>
            <div className="space-y-2 ml-4">
              {pieData.map((d) => (
                <div key={d.name} className="flex items-center gap-2 text-xs">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ background: PIE_COLORS[d.name] || "#64748b" }} />
                  <span className="text-slate-300">{d.name}</span>
                  <span className="text-slate-500">{d.value}</span>
                </div>
              ))}
            </div>
          </div>
        </GlassCard>
      </div>
      </ScrollSection>

      <ScrollSection delay={0.1}>
      <GlassCard delay={0.3}>
        <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">
          <div className="flex items-center gap-1.5">
            <TrendingUp size={12} />
            Recent Activity
          </div>
        </h3>
        <div className="space-y-1">
          {stats.recent_activities.map((a) => (
            <motion.div
              key={a.ACTIVITY_ID}
              initial={{ opacity: 0, x: -8 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-white/5 transition-colors"
            >
              <span className="text-xs text-slate-500 font-mono w-20 shrink-0">{a.ACTIVITY_DATE}</span>
              <span
                className="text-xs px-2 py-0.5 rounded-full font-medium w-16 text-center shrink-0"
                style={{ background: `${TYPE_COLORS[a.ACTIVITY_TYPE] || "#64748b"}20`, color: TYPE_COLORS[a.ACTIVITY_TYPE] || "#64748b" }}
              >
                {a.ACTIVITY_TYPE}
              </span>
              <span className="text-sm text-blue-400 w-40 shrink-0 truncate">{a.ORG_NAME}</span>
              <span className="text-xs text-slate-400 truncate">{a.SUMMARY}</span>
            </motion.div>
          ))}
        </div>
      </GlassCard>
      </ScrollSection>
    </div>
  );
}
