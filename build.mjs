// build.js
import esbuild from "esbuild";

esbuild.build({
  entryPoints: ["./src/index.tsx"],
  bundle: true,
  minify: true,
  target: ["es2020"],
  outdir: "lonboard/static/",
  format: "esm",
  // Ref https://github.com/manzt/anywidget/issues/369#issuecomment-1792376003
  define: {
    "define.amd": "false",
  },
});
