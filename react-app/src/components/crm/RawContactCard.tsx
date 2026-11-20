"use client";

import { MapPin, User, Calendar, Building2 } from "lucide-react";
import GlassCard from "../shared/GlassCard";
import type { CrmContact } from "@/lib/types";

interface RawContactCardProps {
  contact: CrmContact;
}

export default function RawContactCard({ contact }: RawContactCardProps) {
  return (
    <GlassCard className="relative">
      <h3 className="text-lg font-semibold text-white mb-1">{contact.ORG_NAME}</h3>
      <p className="text-sm text-slate-400 mb-4">{contact.ORG_DESCRIPTION}</p>

      <div className="grid grid-cols-2 gap-3 text-sm">
        <div className="flex items-center gap-2 text-slate-300">
          <Building2 size={14} className="text-slate-500" />
          <span>{contact.SECTOR}</span>
        </div>
        <div className="flex items-center gap-2 text-slate-300">
          <MapPin size={14} className="text-slate-500" />
          <span>{contact.HQ_CITY}, {contact.COUNTRY}</span>
        </div>
        <div className="flex items-center gap-2 text-slate-300">
          <User size={14} className="text-slate-500" />
          <span>{contact.PRIMARY_CONTACT_NAME}</span>
        </div>
        <div className="flex items-center gap-2 text-slate-300">
          <Calendar size={14} className="text-slate-500" />
          <span>{contact.LAST_INTERACTION_DATE}</span>
        </div>
      </div>
    </GlassCard>
  );
}
