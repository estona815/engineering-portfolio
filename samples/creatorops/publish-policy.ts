import type { Approval, Asset, Project, PublishPackage, QCReport } from "@creatorops/domain";

export interface PublishIntent { privacyStatus: "private" | "unlisted" | "public"; publishAt: string | null; containsSyntheticMedia: boolean | null; madeForKids: boolean; paidPromotionReviewed: boolean; }
export interface PolicyDecision { allowed: boolean; reasons: string[]; requiresHumanApproval: boolean; }

export function evaluatePublish(project: Project, publishPackage: PublishPackage, qc: QCReport, approvals: Approval[], assets: Asset[], intent: PublishIntent, uploadFeatureEnabled: boolean): PolicyDecision {
  const reasons: string[] = [];
  const referencedAssetIds = new Set([publishPackage.videoAssetId, ...(publishPackage.thumbnailAssetId ? [publishPackage.thumbnailAssetId] : []), ...publishPackage.captionAssetIds]);
  if (!uploadFeatureEnabled) reasons.push("REAL_UPLOAD_FEATURE_DISABLED");
  if (!qc.passed || qc.items.some(i => i.blocking && !i.resolvedAt)) reasons.push("BLOCKING_QC_REMAINS");
  if (publishPackage.projectId !== project.id) reasons.push("PUBLISH_PACKAGE_PROJECT_MISMATCH");
  if (publishPackage.contentHash !== approvals.find(a => a.stage === "FINAL_APPROVAL" && a.decision === "APPROVED")?.approvedContentHash) reasons.push("CONTENT_CHANGED_AFTER_APPROVAL_OR_APPROVAL_MISSING");
  if (assets.some(a => !a.license || !a.provenance)) reasons.push("ASSET_RIGHTS_OR_PROVENANCE_MISSING");
  if (assets.some(a => referencedAssetIds.has(a.id) && a.provider === "fixture-v1")) reasons.push("FIXTURE_ASSET_NOT_PUBLISHABLE");
  if (intent.containsSyntheticMedia === null) reasons.push("SYNTHETIC_MEDIA_DISCLOSURE_UNCONFIRMED");
  if (!intent.paidPromotionReviewed) reasons.push("PAID_PROMOTION_REVIEW_MISSING");
  if ((intent.privacyStatus === "public" || intent.publishAt) && !approvals.some(a => a.stage === "PUBLIC_PUBLISH" && a.decision === "APPROVED" && a.approvedContentHash === publishPackage.contentHash)) reasons.push("PUBLIC_OR_SCHEDULE_APPROVAL_MISSING");
  return { allowed: reasons.length === 0, reasons, requiresHumanApproval: true };
}

export function screenPromptInjection(text: string): { safeText: string; flagged: boolean } {
  const patterns = [/ignore\s+(all|previous|prior)\s+instructions/gi, /system\s*prompt/gi, /developer\s+message/gi, /reveal\s+(token|secret|key)/gi];
  let safeText = text; let flagged = false;
  for (const pattern of patterns) safeText = safeText.replace(pattern, match => { flagged = true; return `[UNTRUSTED_DIRECTIVE:${match.length}]`; });
  return { safeText, flagged };
}
