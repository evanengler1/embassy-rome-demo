"use client";

import type { SummitAttendee } from "@/lib/types";

interface AttendeeTableProps {
  attendees: SummitAttendee[];
  highlightedNames: string[];
}

export default function AttendeeTable({ attendees, highlightedNames }: AttendeeTableProps) {
  if (attendees.length === 0) return null;

  return (
    <div>
      <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">
        Summit Roster ({attendees.length} attendees)
      </h3>
      <div className="glass overflow-hidden">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-blue-500/10">
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Name</th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Organization</th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Country</th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Title</th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase">Sector</th>
            </tr>
          </thead>
          <tbody>
            {attendees.map((a) => {
              const highlighted = highlightedNames.includes(a.ATTENDEE_NAME.toLowerCase());
              return (
                <tr
                  key={a.ATTENDEE_NAME}
                  className={`border-b border-blue-500/5 transition-colors hover:bg-blue-500/5 ${
                    highlighted ? "border-l-2 border-l-blue-500 bg-blue-500/5" : ""
                  }`}
                >
                  <td className={`px-4 py-2.5 ${highlighted ? "text-white font-medium" : "text-slate-300"}`}>
                    {a.ATTENDEE_NAME}
                  </td>
                  <td className="px-4 py-2.5 text-slate-400">{a.ORGANIZATION}</td>
                  <td className="px-4 py-2.5 text-slate-400">{a.COUNTRY}</td>
                  <td className="px-4 py-2.5 text-slate-400">{a.TITLE}</td>
                  <td className="px-4 py-2.5 text-slate-400">{a.SECTOR}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
