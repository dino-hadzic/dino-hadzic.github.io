const base = import.meta.env.BASE_URL.replace(/\/+$/, "");

/** Prefixes a root-absolute path with the configured base path. */
export function withBase(path: string): string {
  return `${base}${path}`;
}

/** Rewrites root-absolute href/src attributes in generated HTML to include the base path. */
export function rewriteBase(html: string): string {
  return base ? html.replace(/(href|src)="\//g, `$1="${base}/`) : html;
}
