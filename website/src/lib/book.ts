import index from "../data/index.json";
import literatura from "../data/literatura.json";
import summaries from "../data/summaries.json";
import { withBase } from "./url";

export type SectionMeta = {
  id: string;
  title: string;
  level: number;
};

export type ChapterMeta = {
  slug: string;
  number: number | null;
  title: string;
  part: string | null;
  sections: SectionMeta[];
};

export type Chapter = ChapterMeta & { html: string };

export type Reference = { key: string; html: string };

export type ChapterCard = ChapterMeta & {
  opis: string;
  image: string;
  tier: "neutral" | "tier-1" | "tier-2" | "tier-3";
};

export const chapters = index as ChapterMeta[];
export const references = literatura as Reference[];
const summaryBySlug = new Map(
  (summaries as { slug: string; opis: string }[]).map((summary) => [summary.slug, summary]),
);

/** Chapters grouped by book part, in reading order. */
export function chaptersByPart(): { part: string; chapters: ChapterMeta[] }[] {
  const groups: { part: string; chapters: ChapterMeta[] }[] = [];
  for (const chapter of chapters) {
    if (chapter.number === null) continue;
    const part = chapter.part ?? "Poglavlja";
    let group = groups.find((g) => g.part === part);
    if (!group) {
      group = { part, chapters: [] };
      groups.push(group);
    }
    group.chapters.push(chapter);
  }
  return groups;
}

export function chapterLabel(chapter: ChapterMeta): string {
  return chapter.number === null ? chapter.title : `${chapter.number}. ${chapter.title}`;
}

function chapterTier(number: number | null): ChapterCard["tier"] {
  if (number === null) return "neutral";
  if (number <= 10) return "tier-1";
  if (number <= 20) return "tier-2";
  return "tier-3";
}

/** Chapter metadata enriched with the authored description and illustration path. */
export function chapterCards(): ChapterCard[] {
  return chapters.map((chapter) => {
    const summary = summaryBySlug.get(chapter.slug);
    if (!summary) {
      throw new Error(`Missing chapter summary for slug "${chapter.slug}"`);
    }
    return {
      ...chapter,
      opis: summary.opis,
      image: withBase(`/art/${chapter.slug}.jpg`),
      tier: chapterTier(chapter.number),
    };
  });
}

export function neighbours(slug: string): { prev: ChapterMeta | null; next: ChapterMeta | null } {
  const i = chapters.findIndex((c) => c.slug === slug);
  return {
    prev: i > 0 ? chapters[i - 1] : null,
    next: i >= 0 && i < chapters.length - 1 ? chapters[i + 1] : null,
  };
}

export async function loadChapter(slug: string): Promise<Chapter> {
  const data = await import(`../data/${slug}.json`);
  return (data.default ?? data) as Chapter;
}
