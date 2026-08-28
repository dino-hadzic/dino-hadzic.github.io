import katex from "katex";

const MACROS: Record<string, string> = {
  "\\XOR": "\\mathbin{\\char`\\^}",
  "\\key": "\\textbf{#1}",
};

function unescapeAttr(value: string): string {
  return value
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#x27;/g, "'")
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, "&");
}

/** Replaces the converter's math placeholders with KaTeX output (at build time). */
export function renderMath(html: string): string {
  return html.replace(
    /<span class="math-(inline|display)" data-tex="([^"]*)"><\/span>/g,
    (_match, kind: string, raw: string) => {
      const tex = unescapeAttr(raw);
      const displayMode = kind === "display";
      try {
        const out = katex.renderToString(tex, {
          displayMode,
          throwOnError: true,
          strict: false,
          trust: true,
          macros: MACROS,
        });
        return displayMode ? `<div class="math-block">${out}</div>` : out;
      } catch (error) {
        console.warn(`[math] KaTeX failed for: ${tex}\n  ${String(error)}`);
        const fallback = tex.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        return `<code class="math-raw">${fallback}</code>`;
      }
    },
  );
}
