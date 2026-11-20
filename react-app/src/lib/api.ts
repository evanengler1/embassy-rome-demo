import type { ApiAction } from "./types";

export async function apiCall<T>(action: ApiAction, params?: Record<string, unknown>): Promise<T> {
  const res = await fetch("/api/snowflake", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ action, ...params }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: "Request failed" }));
    throw new Error(err.error || `HTTP ${res.status}`);
  }
  return res.json();
}
