import { executeQuery } from "./snowflake";

const MODEL = "gemini-2.5-flash";

export function sqlEscape(s: string): string {
  return s
    .replace(/\\/g, "\\\\")
    .replace(/'/g, "\\'")
    .replace(/\n/g, "\\n")
    .replace(/\r/g, "\\r")
    .replace(/\t/g, "\\t");
}

export function parseLlmJson<T>(raw: string): T {
  let text = raw;
  const fenceMatch = text.match(/```(?:json)?\s*\n?([\s\S]*?)```/);
  if (fenceMatch) {
    text = fenceMatch[1];
  }
  text = text.trim();
  const start = text.indexOf("{");
  const end = text.lastIndexOf("}");
  if (start !== -1 && end !== -1 && end > start) {
    text = text.slice(start, end + 1);
  }
  return JSON.parse(text) as T;
}

export async function cortexComplete(
  systemPrompt: string,
  userPrompt: string,
  temperature = 0.1,
  maxTokens = 4096
): Promise<string> {
  const sysEsc = sqlEscape(systemPrompt);
  const usrEsc = sqlEscape(userPrompt);
  const sql = `
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
      '${MODEL}',
      [
        {'role': 'system', 'content': '${sysEsc}'},
        {'role': 'user', 'content': '${usrEsc}'}
      ],
      {'temperature': ${temperature}, 'max_tokens': ${maxTokens}}
    ) AS response
  `;
  const rows = await executeQuery<{ RESPONSE: string }>(sql);
  const raw = rows[0].RESPONSE;
  const obj = typeof raw === 'string' ? JSON.parse(raw) : raw;
  return obj.choices?.[0]?.messages ?? obj.choices?.[0]?.message?.content ?? (typeof raw === 'string' ? raw : JSON.stringify(raw));
}

export async function cortexSearch(
  service: string,
  query: string,
  columns: string[],
  limit = 3
): Promise<Record<string, string>[]> {
  const colsJson = columns.map((c) => `"${c}"`).join(", ");
  const payload = `{"query": "${sqlEscape(query)}", "columns": [${colsJson}], "limit": ${limit}}`;
  const sql = `
    SELECT SNOWFLAKE.CORTEX.SEARCH_PREVIEW(
      '${service}',
      '${sqlEscape(payload)}'
    ) AS results
  `;
  const rows = await executeQuery<{ RESULTS: string }>(sql);
  const raw = rows[0].RESULTS;
  const parsed = typeof raw === 'string' ? JSON.parse(raw) : raw;
  return parsed.results || [];
}
