module.exports = function (eleventyConfig) {
  // Copy CNAME to output root so GitHub Pages picks up the custom domain.
  // Object syntax is relative to project root (string form would be relative to src/).
  eleventyConfig.addPassthroughCopy({ "CNAME": "CNAME" });

  return {
    dir: {
      input: "src",
      output: "_site",
    },
    // HTML files are self-contained — skip template engine processing
    htmlTemplateEngine: false,
  };
};
