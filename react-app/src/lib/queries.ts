"use client";

import { useQuery, useMutation, type UseQueryOptions } from "@tanstack/react-query";
import { apiCall } from "./api";
import type {
  CrmContact,
  ActivityLog,
  SectorIntel,
  SummitAttendee,
  MissionPriority,
  PolicyDocument,
  OverviewStats,
  ContactDetail,
  EnrichmentResult,
  PrioritizationResult,
  AlignmentResult,
} from "./types";

export function useOverviewStats() {
  return useQuery<OverviewStats>({ queryKey: ["overviewStats"], queryFn: () => apiCall("getOverviewStats") });
}

export function useContacts() {
  return useQuery<CrmContact[]>({ queryKey: ["contacts"], queryFn: () => apiCall("getContacts") });
}

export function useAttendees() {
  return useQuery<SummitAttendee[]>({ queryKey: ["attendees"], queryFn: () => apiCall("getAttendees") });
}

export function usePriorities() {
  return useQuery<MissionPriority[]>({ queryKey: ["priorities"], queryFn: () => apiCall("getPriorities") });
}

export function useDocuments() {
  return useQuery<PolicyDocument[]>({ queryKey: ["documents"], queryFn: () => apiCall("getDocuments") });
}

export function useActivities() {
  return useQuery<ActivityLog[]>({ queryKey: ["activities"], queryFn: () => apiCall("getActivities") });
}

export function useIntelligence() {
  return useQuery<SectorIntel[]>({ queryKey: ["intelligence"], queryFn: () => apiCall("getIntelligence") });
}

export function useContactDetail(orgName: string | null) {
  return useQuery<ContactDetail>({
    queryKey: ["contactDetail", orgName],
    queryFn: () => apiCall("getContactDetail", { orgName }),
    enabled: !!orgName,
  });
}

export function useEnrichContact() {
  return useMutation<EnrichmentResult, Error, string>({
    mutationFn: (orgName) => apiCall("enrichContact", { orgName }),
  });
}

export function usePrioritize() {
  return useMutation<PrioritizationResult, Error, number>({
    mutationFn: (priorityId) => apiCall("prioritize", { priorityId }),
  });
}

export function useAnalyzeAlignment() {
  return useMutation<AlignmentResult, Error, { internalDocId: number; externalDocId: number }>({
    mutationFn: (params) => apiCall("analyzeAlignment", params),
  });
}
