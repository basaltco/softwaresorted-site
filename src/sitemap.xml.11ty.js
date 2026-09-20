const fs = require("fs");
const path = require("path");

const DOMAIN = "https://softwaresorted.co.uk";
const DATE_MODIFIED_RE = /"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})"/;

function walk(dir, base = "") {
  let pages = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name.startsWith(".")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      pages = pages.concat(walk(full, `${base}/${entry.name}`));
    } else if (entry.name.endsWith(".html")) {
      const slug = entry.name === "index.html" ? "" : entry.name.replace(/\.html$/, "");
      const urlPath = slug ? `${base}/${slug}/` : `${base}/` || "/";
      const contents = fs.readFileSync(full, "utf8");
      const match = contents.match(DATE_MODIFIED_RE);
      pages.push({ url: urlPath, lastmod: match ? match[1] : null });
    }
  }
  return pages;
}

module.exports = class {
  data() {
    return {
      permalink: "sitemap.xml",
      eleventyExcludeFromCollections: true,
    };
  }

  render() {
    const pages = walk(__dirname)
      .filter((page) => page.url !== "/sitemap.xml/")
      .sort((a, b) => a.url.localeCompare(b.url));
    const urlEntries = pages
      .map((page) => {
        const lastmod = page.lastmod ? `\n    <lastmod>${page.lastmod}</lastmod>` : "";
        return `  <url>\n    <loc>${DOMAIN}${page.url}</loc>${lastmod}\n  </url>`;
      })
      .join("\n");
    return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urlEntries}\n</urlset>\n`;
  }
};
