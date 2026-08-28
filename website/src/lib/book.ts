import index from "../data/index.json";
import literatura from "../data/literatura.json";

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

export const chapters = index as ChapterMeta[];
export const references = literatura as Reference[];

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
