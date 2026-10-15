import { readdir } from "node:fs/promises";
import { join } from "node:path";

import { PROJECT_ID_PATTERN } from "@instatoon/shared";

export function seoulDateStamp(now = new Date()): string {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "Asia/Seoul",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(now);
  const part = (type: Intl.DateTimeFormatPartTypes): string =>
    parts.find((candidate) => candidate.type === type)?.value ?? "";
  return `${part("year")}${part("month")}${part("day")}`;
}

export async function nextProjectId(projectsDir: string, now = new Date()): Promise<string> {
  const dateStamp = seoulDateStamp(now);
  let entries: string[] = [];
  try {
    entries = await readdir(projectsDir);
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
  }

  const prefix = `EP-${dateStamp}-`;
  const greatest = entries.reduce((maximum, entry) => {
    if (!PROJECT_ID_PATTERN.test(entry) || !entry.startsWith(prefix)) return maximum;
    const sequence = Number.parseInt(entry.slice(prefix.length), 10);
    return Number.isNaN(sequence) ? maximum : Math.max(maximum, sequence);
  }, 0);
  return `${prefix}${String(greatest + 1).padStart(3, "0")}`;
}

export function projectDirectory(workspaceRoot: string, projectId: string): string {
  if (!PROJECT_ID_PATTERN.test(projectId)) {
    throw new Error(`올바르지 않은 프로젝트 ID입니다: ${projectId}`);
  }
  return join(workspaceRoot, "projects", projectId);
}
