const fs = require("fs");
const path = require("path");

const DOMAIN = "https://softwaresorted.co.uk";

function walk(dir, base = "") {
  let urls = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name.startsWith(".")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      urls = urls.concat(walk(full, `${base}/${entry.name}`));
    } else if (entry.name.endsWith(".html")) {
      const slug = entry.name === "index.html" ? "" : entry.name.replace(/\.html$/, "");
      const urlPath = slug ? `${base}/${slug}/` : `${base}/` || "/";
      urls.push(urlPath);
    }
  }
  return urls;
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
      .filter((url) => url !== "/sitemap.xml/")
      .sort();
    const urlEntries = pages
      .map((url) => `  <url>\n    <loc>${DOMAIN}${url}</loc>\n  </url>`)
      .join("\n");
    return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urlEntries}\n</urlset>\n`;
  }
};
