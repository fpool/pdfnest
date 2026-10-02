# -*- coding: utf-8 -*-
"""PdfNest — PDF 工具集生成器(4 语言 + 暗黑模式)
运行: python build.py → index + 8 工具 × 4 语言 + privacy/about × 4 语言 + sitemap.xml
"""
import sys
from pathlib import Path
from i18n import TR

sys.stdout.reconfigure(encoding="utf-8")
BASE_URL = "https://pdfnest.pages.dev"
LANGS = ["en", "de", "fr", "es"]

HOME_TRI = {
 "en": {"title":"Free PDF Tools — Merge, Split, Rotate, Convert | PdfNest",
   "meta":"Free online PDF tools: merge, split, rotate, delete pages, images to PDF, PDF to images, extract text and page numbers. 100% private — files never leave your browser.",
   "h1":"Free PDF Tools — No Upload Needed",
   "sub":"Fast, private PDF tools that run <b>entirely in your browser</b> — your documents never touch a server. Unlike other “free” converters, there is no upload step, because there doesn't need to be.",
   "h2":"Private by architecture, not by promise",
   "p1":"Every tool on PdfNest processes your files locally using JavaScript and WebAssembly. Your documents are never sent anywhere — which is why they're safe for contracts, IDs and anything personal.",
   "p2":"Free forever: no signup, no watermarks, no daily limits, no “premium” tier."},
 "de": {"title":"Kostenlose PDF-Werkzeuge — Zusammenführen, Teilen, Drehen | PdfNest",
   "meta":"Kostenlose Online-PDF-Werkzeuge: zusammenführen, teilen, drehen, Seiten löschen, Bilder zu PDF, PDF zu Bilder, Text extrahieren und Seitenzahlen. 100 % privat — Dateien verlassen nie Ihren Browser.",
   "h1":"Kostenlose PDF-Werkzeuge — Ohne Upload",
   "sub":"Schnelle, private PDF-Werkzeuge, die <b>vollständig in Ihrem Browser</b> laufen — Ihre Dokumente berühren keinen Server. Anders als bei anderen „kostenlosen“ Konvertern gibt es keinen Upload-Schritt, weil es keinen braucht.",
   "h2":"Privat durch Architektur, nicht durch Versprechen",
   "p1":"Jedes Werkzeug auf PdfNest verarbeitet Ihre Dateien lokal mit JavaScript und WebAssembly. Ihre Dokumente werden nie gesendet — deshalb sind sie sicher für Verträge, Ausweise und alles Persönliche.",
   "p2":"Für immer kostenlos: keine Anmeldung, keine Wasserzeichen, keine Tageslimits, kein „Premium“."},
 "fr": {"title":"Outils PDF gratuits — Fusionner, diviser, pivoter | PdfNest",
   "meta":"Outils PDF gratuits en ligne : fusionner, diviser, pivoter, supprimer des pages, images vers PDF, PDF vers images, extraire le texte et numéros de page. 100 % privé — vos fichiers ne quittent jamais votre navigateur.",
   "h1":"Outils PDF gratuits — Sans téléversement",
   "sub":"Des outils PDF rapides et privés qui fonctionnent <b>entièrement dans votre navigateur</b> — vos documents ne touchent jamais un serveur. Contrairement aux autres convertisseurs « gratuits », il n'y a pas d'étape de téléversement, car elle n'est pas nécessaire.",
   "h2":"Privé par architecture, pas par promesse",
   "p1":"Chaque outil de PdfNest traite vos fichiers localement en JavaScript et WebAssembly. Vos documents ne sont jamais envoyés — c'est pourquoi ils sont sûrs pour les contrats, les pièces d'identité et tout ce qui est personnel.",
   "p2":"Gratuit pour toujours : sans inscription, sans filigrane, sans limites quotidiennes, sans « premium »."},
 "es": {"title":"Herramientas PDF gratis — Combinar, dividir, rotar | PdfNest",
   "meta":"Herramientas PDF gratis en línea: combinar, dividir, rotar, eliminar páginas, imágenes a PDF, PDF a imágenes, extraer texto y números de página. 100 % privado — los archivos nunca salen de tu navegador.",
   "h1":"Herramientas PDF gratis — Sin subidas",
   "sub":"Herramientas PDF rápidas y privadas que funcionan <b>enteramente en tu navegador</b> — tus documentos nunca tocan un servidor. A diferencia de otros conversores «gratis», no hay paso de subida, porque no hace falta.",
   "h2":"Privado por arquitectura, no por promesa",
   "p1":"Cada herramienta de PdfNest procesa tus archivos localmente con JavaScript y WebAssembly. Tus documentos nunca se envían — por eso son seguros para contratos, identificaciones y todo lo personal.",
   "p2":"Gratis para siempre: sin registro, sin marcas de agua, sin límites diarios, sin «premium»."},
}

CSS = """
  :root { --brand:#7c3aed; --brand-soft:#f3e8ff; --bg:#f8fafc; --card:#fff; --text:#0f172a; --muted:#475569; --faint:#64748b; --border:#e2e8f0; --shadow:rgba(0,0,0,.07); --ok:#067647; --ok-bg:#ecfdf5; }
  [data-theme="dark"] { --brand:#a78bfa; --brand-soft:#2a1d4a; --bg:#0b1220; --card:#111a2c; --text:#e6edf7; --muted:#9fb0c7; --faint:#7c8aa0; --border:#1e293b; --shadow:rgba(0,0,0,.45); --ok:#34d399; --ok-bg:#0c2a22; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif; color:var(--text); background:var(--bg); line-height:1.7; display:flex; flex-direction:column; min-height:100vh; }
  header { position:sticky; top:0; z-index:100; background:var(--card); border-bottom:1px solid var(--border); padding:12px 24px; box-shadow:0 1px 10px var(--shadow); }
  .header-inner { max-width:960px; margin:0 auto; display:flex; align-items:center; justify-content:space-between; }
  .logo { font-weight:800; font-size:20px; color:var(--brand); text-decoration:none; white-space:nowrap; }
  .nav-links { display:flex; align-items:center; gap:22px; }
  .nav-links a { color:var(--muted); text-decoration:none; font-size:14px; white-space:nowrap; }
  .nav-links a:hover { color:var(--brand); }
  .controls { display:flex; align-items:center; gap:10px; margin-left:12px; }
  .lang { position:relative; }
  #langBtn { display:flex; align-items:center; gap:6px; background:none; border:0; padding:6px 4px; color:var(--text); font-size:14px; font-weight:700; cursor:pointer; white-space:nowrap; }
  #langBtn:hover { color:var(--brand); }
  #langBtn .chev { width:15px; height:15px; fill:none; stroke:currentColor; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round; transition:transform .2s; }
  .lang.open #langBtn .chev { transform:rotate(180deg); }
  .lang-menu { display:none; position:absolute; right:0; top:calc(100% + 8px); background:var(--card); border:1px solid var(--border); border-radius:12px; box-shadow:0 8px 24px var(--shadow); min-width:170px; padding:6px; z-index:60; }
  .lang.open .lang-menu { display:block; }
  .lang-menu a { display:block; padding:8px 14px; border-radius:8px; color:var(--text); text-decoration:none; font-size:14px; }
  .lang-menu a:hover { background:var(--brand-soft); }
  .lang-menu a.cur { color:var(--brand); font-weight:700; }
  .lang-menu a.cur::after { content:" ✓"; }
  #themeBtn { display:flex; align-items:center; justify-content:center; background:var(--card); border:1px solid var(--border); border-radius:10px; width:36px; height:36px; cursor:pointer; color:var(--muted); }
  #themeBtn:hover { color:var(--brand); border-color:var(--brand); }
  #themeBtn svg { width:17px; height:17px; fill:none; stroke:currentColor; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
  #themeBtn .icon-sun { display:none; }
  [data-theme="dark"] #themeBtn .icon-moon { display:none; }
  [data-theme="dark"] #themeBtn .icon-sun { display:block; }
  main { max-width:960px; margin:0 auto; padding:32px 20px 48px; width:100%; flex:1; }
  h1 { font-size:28px; margin-bottom:8px; }
  h2 { font-size:20px; margin:30px 0 10px; }
  .sub { color:var(--muted); margin-bottom:24px; font-size:16px; }
  .drop { border:2px dashed #a78bfa; border-radius:16px; background:var(--card); padding:44px 24px; text-align:center; cursor:pointer; transition:.2s; }
  .drop:hover,.drop.over { border-color:var(--brand); background:var(--brand-soft); }
  .drop .icon { font-size:42px; }
  .drop p { font-size:16px; margin-top:8px; color:var(--text); }
  .drop .hint { font-size:13px; color:var(--faint); margin-top:6px; }
  .filelist { margin-top:14px; font-size:14px; color:var(--muted); text-align:left; }
  .filelist div { padding:4px 10px; background:var(--card); border:1px solid var(--border); border-radius:8px; margin-top:6px; }
  .field { margin-top:16px; text-align:left; }
  .field label { display:block; font-size:13px; color:var(--muted); margin-bottom:4px; font-weight:600; }
  .field input, .field select { width:100%; padding:10px 12px; border:1px solid var(--border); border-radius:8px; background:var(--bg); color:var(--text); font-size:15px; }
  .btn { margin-top:16px; width:100%; background:var(--brand); color:#fff; border:0; border-radius:10px; padding:12px; font-size:16px; font-weight:700; cursor:pointer; }
  .btn:hover { filter:brightness(1.1); }
  .btn:disabled { opacity:.5; cursor:not-allowed; }
  .status { text-align:center; margin-top:14px; font-size:14px; color:var(--muted); min-height:22px; }
  .dl { display:none; margin-top:14px; }
  .dl a { display:block; text-align:center; background:var(--ok); color:#fff; text-decoration:none; border-radius:10px; padding:12px; font-size:15px; font-weight:700; }
  p, li { color:var(--muted); font-size:15px; margin-bottom:10px; }
  ul { padding-left:22px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:18px; margin-top:16px; }
  .grid a { background:var(--card); border:1px solid var(--border); border-radius:12px; padding:16px; text-decoration:none; color:var(--text); font-weight:600; font-size:14px; box-shadow:0 1px 3px var(--shadow); }
  .grid a:hover { border-color:var(--brand); color:var(--brand); }
  .grid a span { display:block; font-weight:400; color:var(--muted); font-size:13px; margin-top:4px; }
  .privacy-note { background:var(--ok-bg); border:1px solid transparent; border-radius:12px; padding:14px 18px; margin-top:24px; font-size:14px; color:var(--ok); }
  footer { text-align:center; color:var(--faint); font-size:13px; padding:28px; border-top:1px solid var(--border); margin-top:40px; }
"""

HEAD = """<!DOCTYPE html>
<html lang="__LANG__">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>try{const t=localStorage.getItem('theme');if(t==='dark'||(!t&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.dataset.theme='dark';}catch(e){}</script>
<title>__TITLE__</title>
<meta name="description" content="__META__">
<link rel="canonical" href="__URL__">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PdfNest">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__META__">
<meta property="og:url" content="__URL__">
<meta name="twitter:card" content="summary">
__HREFLANGS__
<script type="application/ld+json">__LD_WEBAPP__</script>
__LD_FAQ__
<script defer src="/assets/pdf-lib.min.js"></script>
<script defer src="/assets/pdf.min.js"></script>
<script defer src="/assets/pdf.worker.min.js"></script>
<script defer src="/assets/jszip.min.js"></script>
<style>__CSS__</style>
</head>
<body>
<header><div class="header-inner">
  <a class="logo" href="__HOME_HREF__">📄 PdfNest</a>
  <nav class="nav-links">
    <a href="__PRIVACY_HREF__">__NAV_PRIVACY__</a><a href="__ABOUT_HREF__">__NAV_ABOUT__</a>
    <button id="themeBtn" title="Toggle dark mode" aria-label="Toggle dark mode">
      <svg class="icon-moon" viewBox="0 0 24 24"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
    </button>
    __LANGSWITCH__
  </nav>
</div></header>
<main>
__MAIN__
</main>
<footer>__FOOTER__</footer>
<script>
try {
const themeBtn = document.getElementById('themeBtn');
themeBtn.addEventListener('click', function () {
  const dark = document.documentElement.dataset.theme === 'dark';
  if (dark) delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme = 'dark';
  try { localStorage.setItem('theme', dark ? 'light' : 'dark'); } catch (e) {}
});
const langBox = document.querySelector('.lang');
if (langBox) {
  document.getElementById('langBtn').addEventListener('click', function (e) { e.stopPropagation(); langBox.classList.toggle('open'); });
  document.addEventListener('click', function (e) { if (!langBox.contains(e.target)) langBox.classList.remove('open'); });
}
} catch (e) {}
</script>
</body>
</html>
"""

# ---------------- 工具定义(英文基准;JS 中 out/UI 标签 key 化) ----------------
TOOL_JS_HELPERS = """
function setStatus(t) { document.getElementById('status').textContent = t; }
function parseRanges(str, max) {
  if (!str || !str.trim()) return Array.from({length: max}, function(_, i){ return i + 1; });
  const out = [];
  str.split(',').forEach(function (part) {
    const m = part.trim().match(/^(\\d+)(?:-(\\d+))?$/);
    if (m) { let a = +m[1], b = m[2] ? +m[2] : a;
      for (let i = a; i <= b; i++) if (i >= 1 && i <= max && out.indexOf(i) < 0) out.push(i); }
  });
  return out.sort(function (x, y) { return x - y; });
}
function setupWorker() {
  if (window.pdfjsLib && !window.__PW__) {
    pdfjsLib.GlobalWorkerOptions.workerSrc = '/assets/pdf.worker.min.js';
    window.__PW__ = true;
  }
}
const F$ = function (v) { return Number(v).toLocaleString('en-US'); };
let LAST_URL = '';
function downloadBlob(blob, name) {
  if (LAST_URL) URL.revokeObjectURL(LAST_URL);
  LAST_URL = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = LAST_URL; a.download = name;
  document.body.appendChild(a); a.click(); a.remove();
}
function showDl(name) {
  if (!LAST_URL) return;
  const box = document.getElementById('dlbox');
  const link = document.getElementById('dllink');
  link.textContent = TRW.dl;
  link.href = LAST_URL; link.download = name;
  box.style.display = 'block';
}
function libsReady() {
  return new Promise(function (res) {
    if (document.readyState === 'complete') return res();
    window.addEventListener('load', res, { once: true });
  });
}
function extOk(f) {
  const acc = fileEl.accept || '';
  const exts = acc.split(',').map(function (a) { return a.trim().toLowerCase(); })
    .filter(function (a) { return a.charAt(0) === '.'; });
  if (!exts.length) return true;
  const n = f.name.toLowerCase();
  return exts.some(function (e) { return n.slice(-e.length) === e; });
}
"""

BOOT_JS = """
let CHSEN = [];
const dropEl = document.getElementById('drop');
const fileEl = document.getElementById('file');
const listEl = document.getElementById('filelist');
const goEl = document.getElementById('go');
fileEl.addEventListener('change', function () { setFiles([...fileEl.files]); });
dropEl.addEventListener('click', function () { fileEl.click(); });
dropEl.addEventListener('keydown', function (e) {
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fileEl.click(); }
});
dropEl.addEventListener('dragover', function (e) { e.preventDefault(); dropEl.classList.add('over'); });
dropEl.addEventListener('dragleave', function () { dropEl.classList.remove('over'); });
dropEl.addEventListener('drop', function (e) {
  e.preventDefault(); dropEl.classList.remove('over');
  if (e.dataTransfer.files.length) setFiles([...e.dataTransfer.files]);
});
function setFiles(fs) {
  const good = fs.filter(extOk);
  if (good.length !== fs.length) setStatus(TRW.bad_type);
  CHSEN = good;
  listEl.innerHTML = CHSEN.map(function (f) {
    return '<div>' + f.name + ' \u2014 ' + Math.max(1, Math.round(f.size / 1024)) + ' KB</div>';
  }).join('');
  goEl.disabled = CHSEN.length === 0;
}
goEl.addEventListener('click', async function () {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  goEl.disabled = true;
  setStatus(TRW.processing);
  try {
    await libsReady();
    await processFiles();
  } catch (err) {
    if (window.console) console.error(err);
    setStatus(TRW.error + ': ' + ((err && err.message) || err));
  } finally {
    goEl.disabled = false;
  }
});
"""

TOOLS = [
dict(slug="merge", nav="Merge PDF", multi=True, accept="application/pdf,.pdf",
 tool_inputs="",
 title="Merge PDF — Combine Files, Free & No Upload | PdfNest",
 h1="Merge PDF",
 meta="Merge multiple PDF files online for free. 100% private — files never leave your browser. No signup, no watermark.",
 intro="Combine two or more PDF files into a single document, in the order you choose.",
 faq=[("Is it really private?","Yes — merging runs as JavaScript in your browser. Your files are never uploaded."),
      ("How many files can I merge?","Practically unlimited — limited only by your device's memory."),
      ("Is quality preserved?","Yes — pages are copied without recompression: text and quality stay intact.")]),
dict(slug="split", nav="Split PDF", multi=False, accept="application/pdf,.pdf",
 tool_inputs='''  <div class="field"><label>__PAGES_LBL__</label><input type="text" id="pages" placeholder="1-3,5"></div>''',
 title="Split PDF — Every Page as Its Own File | PdfNest",
 h1="Split PDF",
 meta="Split a PDF online for free — every page becomes its own file, downloaded as ZIP. Private, no upload.",
 intro="Split a PDF into individual pages — each page becomes its own PDF file, all packaged as a ZIP.",
 faq=[("Can I specify page ranges?","Yes — enter e.g. 1-3,5 in the pages field; only those pages will be split."),
      ("How are output files named?","Original name with page number, e.g. document_p2.pdf."),
      ("Is it really private?","Yes — everything runs in your browser, nothing is uploaded.")]),
dict(slug="rotate", nav="Rotate PDF", multi=False, accept="application/pdf,.pdf",
 tool_inputs='''  <div class="field"><label>__ANGLE_LBL__</label><select id="angle"><option value="90">90°</option><option value="180">180°</option><option value="270">270°</option></select></div>
  <div class="field"><label>__PAGES_LBL__</label><input type="text" id="pages" placeholder="1-3,7"></div>''',
 title="Rotate PDF Pages — Free & No Upload | PdfNest",
 h1="Rotate PDF Pages",
 meta="Rotate PDF pages online by 90/180/270 degrees for free. Private — files never leave your browser.",
 intro="Rotate specific or all pages of a PDF by 90, 180 or 270 degrees.",
 faq=[("Can I rotate only certain pages?","Yes — leave the pages field empty for all pages, or enter e.g. 1-3,7."),
      ("Is the rotation permanent?","Yes — pages are physically saved rotated in the new PDF."),
      ("Are text and quality preserved?","Yes — only the page view rotates, content stays intact.")]),
dict(slug="delete-pages", nav="Delete pages", multi=False, accept="application/pdf,.pdf",
 tool_inputs='''  <div class="field"><label>__PAGES_LBL__</label><input type="text" id="pages" placeholder="2,5-7"></div>''',
 title="Delete PDF Pages — Free & No Upload | PdfNest",
 h1="Delete PDF Pages",
 meta="Delete pages from a PDF online for free. Private — files never leave your browser.",
 intro="Remove unwanted pages — the rest stays as a clean PDF.",
 faq=[("How do I specify pages to delete?","Individually or ranges, e.g. 2,5-7. Those pages are removed, all others stay."),
      ("Can I undo?","Just load the original file again — your originals are untouched, everything happens locally."),
      ("Are bookmarks and text preserved?","Yes — the rest of the document stays unchanged.")]),
dict(slug="images-to-pdf", nav="Images to PDF", multi=True, accept="image/jpeg,image/png,.jpg,.jpeg,.png",
 tool_inputs="",
 title="Images to PDF — Convert JPG/PNG Free | PdfNest",
 h1="Images to PDF",
 meta="Convert JPG and PNG images to a PDF online for free. Private — images never leave your browser.",
 intro="Convert multiple images (JPG/PNG) into one PDF — each image becomes a page, in the order you choose.",
 faq=[("Which formats are supported?","JPG/JPEG and PNG. Each image becomes a full page at the image's own size."),
      ("Is image quality preserved?","Yes — images are embedded without recompression."),
      ("Can I change the order?","Files are processed in selection order — select them in the order you want.")]),
dict(slug="pdf-to-images", nav="PDF to images", multi=False, accept="application/pdf,.pdf",
 tool_inputs='''  <div class="field"><label>__PAGES_LBL__</label><input type="text" id="pages" placeholder="1-5"></div>''',
 title="PDF to Images — Export Pages as JPG | PdfNest",
 h1="PDF to Images",
 meta="Export PDF pages as JPG images online for free. Private — files never leave your browser.",
 intro="Export each page of a PDF as a JPG image — ideal for previews, presentations or messaging apps.",
 faq=[("What resolution are the images?","Pages render at high quality (2x scale) — sharp for screen and print."),
      ("All pages or specific ones?","All by default; enter ranges in the pages field, e.g. 1-5."),
      ("How do I get all images?","As individual JPGs or all in a ZIP — both with one click.")]),
dict(slug="extract-text", nav="Extract text", multi=False, accept="application/pdf,.pdf",
 tool_inputs="",
 title="Extract Text from PDF — Free & No Upload | PdfNest",
 h1="Extract Text from PDF",
 meta="Extract text from PDF files online for free. Private — files never leave your browser.",
 intro="Extract all the text from a PDF — with page markers, ready to copy or save as a TXT file.",
 faq=[("Does it work on scanned PDFs?","No — scanned pages are images without a text layer; that would require OCR (not part of this tool)."),
      ("Is the layout preserved?","Text is extracted per page in reading order — complex layouts are simplified."),
      ("How do I save the text?","Download as TXT or simply select and copy.")]),
dict(slug="page-numbers", nav="Page numbers", multi=False, accept="application/pdf,.pdf",
 tool_inputs='''  <div class="field"><label>__START_LBL__</label><input type="number" id="start" value="1" min="0"></div>''',
 title="Add Page Numbers to PDF — Free & No Upload | PdfNest",
 h1="Add Page Numbers",
 meta="Add page numbers to a PDF online for free — position and starting number selectable. Private, no upload.",
 intro="Add page numbers to a PDF — position and starting number freely selectable.",
 faq=[("Can I start at a different number?","Yes — the starting number is free, e.g. 1 on a cover page that stays unnumbered."),
      ("Where does the number appear?","By default bottom center of every page."),
      ("Is the rest unchanged?","Yes — only the numbers are added, content and layout stay intact.")]),
]

# ---------------- 渲染引擎 ----------------
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def site_url(base, lang):
    return BASE_URL + ("/" if (base == "index" and lang == "en")
                      else "/" + page_file(base, lang).replace(".html", ""))

def page_file(base, lang):
    return (base + ".html") if lang == "en" else (base + "-" + lang + ".html")

def lang_switcher(cur, base):
    hf = lambda c: page_file(base, c)
    items = "".join(
        '<a href="' + hf(c) + ('" class="cur"' if c == cur else '"') + '>'
        + (TR.get(c) or {}).get("name", "English") + '</a>' for c in LANGS)
    btn = ('<button id="langBtn" aria-haspopup="true" aria-expanded="false">'
           + (TR.get(cur) or {}).get("name", "English")
           + '<svg class="chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg></button>')
    return '<div class="lang">' + btn + '<div class="lang-menu">' + items + '</div></div>'

def render(lang, base, title, meta, body, cur, ld_faq=None, ld_name="PdfNest"):
    tr = TR.get(lang) or {}
    url = site_url(base, lang)
    ld_w = LD_WEBAPP_T.replace("__NAME__", ld_name).replace("__URL__", url).replace("__META__", meta)
    ent = ""
    if ld_faq:
        ents = ",".join('{"@type":"Question","name":"' + esc(q).replace('"', '\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + esc(a).replace('"', '\\"') + '"}}' for q, a in ld_faq)
        ent = LD_FAQ_T.replace("__ENTITIES__", ents)
    hreflangs = "\n".join(
        '  <link rel="alternate" hreflang="' + c + '" href="' + BASE_URL + '/' + page_file(base, c).replace(".html", "") + '">'
        for c in LANGS) + '\n  <link rel="alternate" hreflang="x-default" href="' + BASE_URL + '/' + page_file(base, "en").replace(".html", "") + '">'
    html = (HEAD.replace("__LANG__", lang)
            .replace("__TITLE__", title).replace("__META__", meta)
            .replace("__URL__", url).replace("__CSS__", CSS)
            .replace("__HREFLANGS__", hreflangs)
            .replace("__LD_WEBAPP__", ld_w).replace("__LD_FAQ__", ent)
            .replace("__NAV_PRIVACY__", tr.get("nav_privacy", "Privacy"))
            .replace("__NAV_ABOUT__", tr.get("nav_about", "About"))
            .replace("__LANGSWITCH__", lang_switcher(lang, base))
            .replace("__HOME_HREF__", "/" if lang == "en" else "/index-" + lang)
            .replace("__PRIVACY_HREF__", "/privacy.html" if lang == "en" else "/privacy-" + lang + ".html")
            .replace("__ABOUT_HREF__", "/about.html" if lang == "en" else "/about-" + lang + ".html")
            .replace("__MAIN__", body)
            .replace("__FOOTER__", FOOTERS.get(lang, FOOTERS["en"])))
    # 清理未消费占位符(隐私页无 FAQ LD 等)
    for p in ["__LD_FAQ__", "__LD_WEBAPP__"]:
        html = html.replace(p, "")
    return html

def tool_page(lang, tool):
    tr = TR.get(lang) or {}
    tt = (tr.get("tools") or {}).get(tool["slug"]) or {}
    title = tt.get("title", tool["title"])
    meta = tt.get("meta", tool["meta"])
    h1 = tt.get("h1", tool["h1"])
    intro = tt.get("intro", tool["intro"])
    faq = tt.get("faq", tool["faq"])
    drop = tr.get("drop", "Drop files here or click to choose")
    pages_lbl = tr.get("pages_lbl", "Pages (empty = all), e.g. 1-3,5")
    angle_lbl = tr.get("angle_lbl", "Rotation angle")
    start_lbl = tr.get("start_lbl", "Starting number")
    btn = tr.get("btn", "Process")
    processing = tr.get("processing", "Processing …")
    done = tr.get("done", "Done!")
    dl = tr.get("download", "Download")
    no_files = tr.get("no_files", "Please choose files first.")
    error = tr.get("error", "Error")
    bad_type = tr.get("bad_type", "Unsupported file type.")
    note = tr.get("privacy_note", "<b>100% private:</b> everything runs locally in your browser. Your files are never uploaded to any server.")
    faq_h = tr.get("faq_title", "FAQ")
    body = f"""
  <h1>{esc(h1)}</h1>
  <p class="sub">{esc(intro)}</p>
  {tool["tool_inputs"].replace("__PAGES_LBL__", esc(pages_lbl)).replace("__ANGLE_LBL__", esc(angle_lbl)).replace("__START_LBL__", esc(start_lbl))}
  {drop_html(tool["multi"], tool["accept"])}
  <button class="btn" id="go" disabled>{esc(btn)}</button>
  <div class="status" id="status"></div>
  <div class="dl" id="dlbox"><a id="dllink" href="#">{esc(dl)}</a></div>
  <div class="privacy-note">🔒 {note}</div>
  <h2>{esc(faq_h)}</h2>
  {"".join('<p><b>' + esc(q) + '</b> ' + esc(a) + '</p>' for q, a in faq)}
  <script>
__BOOT_JS__
const TRW = {{drop: __J_DROP__, processing: __J_PROC__, done: __J_DONE__, dl: __J_DL__, no_files: __J_NOFILES__, error: __J_ERR__, bad_type: __J_BAD__}};
__HELPERS__
__TOOL_JS__
</script>
"""
    body = body.replace("__DROP__", esc(drop))
    body = body.replace("__BOOT_JS__", BOOT_JS).replace("__HELPERS__", TOOL_JS_HELPERS)
    body = (body.replace("__J_DROP__", '"' + esc(drop) + '"')
                .replace("__J_PROC__", '"' + esc(processing) + '"')
                .replace("__J_DONE__", '"' + esc(done) + '"')
                .replace("__J_DL__", '"' + esc(dl) + '"')
                .replace("__J_ERR__", '"' + esc(error) + '"')
                .replace("__J_BAD__", '"' + esc(bad_type) + '"')
                .replace("__J_NOFILES__", '"' + esc(no_files) + '"')
                .replace("__TOOL_JS__", tool["tool_js"]))
    return render(lang, tool["slug"], title, meta, body, tool["slug"],
                  ld_faq=[(q, a) for q, a in faq], ld_name="PdfNest — " + h1)

def drop_html(multi, accept):
    m = "multiple" if multi else ""
    return f"""  <div id="drop" class="drop" role="button" tabindex="0" aria-label="__DROP__">
    <div class="icon">📄</div>
    <p>__DROP__</p>
    <div class="hint">{accept}</div>
    <input type="file" id="file" {m} accept="{accept}" style="display:none">
  </div>
  <div class="filelist" id="filelist"></div>"""

# ---------------- 工具 JS(每个工具的 processFiles) ----------------
TOOL_JS = {
"merge": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  setStatus(TRW.processing);
  const out = await PDFLib.PDFDocument.create();
  for (const f of CHSEN) {
    const doc = await PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
    const pages = await out.copyPages(doc, doc.getPageIndices());
    pages.forEach(function (p) { out.addPage(p); });
  }
  const bytes = await out.save();
  downloadBlob(new Blob([bytes], { type: 'application/pdf' }), 'merged.pdf');
  setStatus('✅ ' + TRW.done);
  showDl('merged.pdf');
}""",
"split": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing);
  const src = await PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
  const max = src.getPageCount();
  const pns = parseRanges(document.getElementById('pages').value, max);
  const zip = new JSZip(); const base = f.name.replace(/\\.pdf$/i, '');
  for (const pn of pns) {
    const doc = await PDFLib.PDFDocument.create();
    const pg = await doc.copyPages(src, [pn - 1]);
    doc.addPage(pg[0]);
    zip.file(base + '_p' + pn + '.pdf', await doc.save());
  }
  downloadBlob(await zip.generateAsync({ type: 'blob' }), base + '_split.zip');
  setStatus('✅ ' + TRW.done);
}""",
"rotate": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing);
  const src = await PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
  const max = src.getPageCount();
  const pns = parseRanges(document.getElementById('pages').value, max);
  const deg = +document.getElementById('angle').value;
  pns.forEach(function (pn) {
    const pg = src.getPage(pn - 1);
    pg.setRotation(PDFLib.degrees((pg.getRotation().angle + deg) % 360));
  });
  const bytes = await src.save();
  downloadBlob(new Blob([bytes], { type: 'application/pdf' }), 'rotated.pdf');
  setStatus('✅ ' + TRW.done);
}""",
"delete-pages": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing);
  const src = await PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
  const max = src.getPageCount();
  let pns = parseRanges(document.getElementById('pages').value, max);
  if (pns.length >= max) return setStatus('Error: cannot delete every page');
  pns.slice().sort(function (a, b) { return b - a; }).forEach(function (pn) { src.removePage(pn - 1); });
  const bytes = await src.save();
  downloadBlob(new Blob([bytes], { type: 'application/pdf' }), 'cleaned.pdf');
  setStatus('✅ ' + TRW.done);
}""",
"images-to-pdf": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  setStatus(TRW.processing);
  const out = await PDFLib.PDFDocument.create();
  for (const f of CHSEN) {
    const bytes = await f.arrayBuffer();
    const img = (/\\.png$/i.test(f.name) || f.type === 'image/png') ? await out.embedPng(bytes) : await out.embedJpg(bytes);
    const dim = img.size();
    const page = out.addPage([dim.width, dim.height]);
    page.drawImage(img, { x: 0, y: 0, width: dim.width, height: dim.height });
  }
  const bytes = await out.save();
  downloadBlob(new Blob([bytes], { type: 'application/pdf' }), 'images.pdf');
  setStatus('✅ ' + TRW.done);
}""",
"pdf-to-images": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing); setupWorker();
  const pdf = await pdfjsLib.getDocument({ data: await f.arrayBuffer() }).promise;
  const max = pdf.numPages;
  const pns = parseRanges(document.getElementById('pages').value, max);
  const zip = new JSZip(); const base = f.name.replace(/\\.pdf$/i, '');
  for (const pn of pns) {
    const page = await pdf.getPage(pn);
    const vp = page.getViewport({ scale: 2 });
    const cv = document.createElement('canvas');
    cv.width = vp.width; cv.height = vp.height;
    await page.render({ canvasContext: cv.getContext('2d'), viewport: vp }).promise;
    const blob = await new Promise(function (r) { cv.toBlob(r, 'image/jpeg', 0.92); });
    zip.file(base + '_p' + pn + '.jpg', blob);
  }
  downloadBlob(await zip.generateAsync({ type: 'blob' }), base + '_images.zip');
  setStatus('✅ ' + TRW.done);
}""",
"extract-text": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing); setupWorker();
  const pdf = await pdfjsLib.getDocument({ data: await f.arrayBuffer() }).promise;
  let text = '';
  for (let pn = 1; pn <= pdf.numPages; pn++) {
    const page = await pdf.getPage(pn);
    const tc = await page.getTextContent();
    text += '\\n\\n===== ' + pn + ' =====\\n' + tc.items.map(function (it) { return it.str; }).join(' ');
  }
  downloadBlob(new Blob([text], { type: 'text/plain' }), f.name.replace(/\\.pdf$/i, '') + '.txt');
  setStatus('✅ ' + TRW.done); showDl(f.name.replace(/\\.pdf$/i, '') + '.txt');
}""",
"page-numbers": """
async function processFiles() {
  if (!CHSEN.length) return setStatus(TRW.no_files);
  const f = CHSEN[0];
  setStatus(TRW.processing);
  const src = await PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
  const start = +(document.getElementById('start').value || 1);
  const font = await src.embedFont(PDFLib.StandardFonts.Helvetica);
  src.getPages().forEach(function (pg, idx) {
    const num = String(start + idx);
    const w = font.widthOfTextAtSize(num, 12);
    pg.drawText(num, { x: pg.getWidth() / 2 - w / 2, y: 24, size: 12, font, color: PDFLib.rgb(0.3, 0.3, 0.3) });
  });
  const bytes = await src.save();
  downloadBlob(new Blob([bytes], { type: 'application/pdf' }), 'numbered.pdf');
  setStatus('✅ ' + TRW.done);
}""",
}
for t in TOOLS:
    t["tool_js"] = TOOL_JS[t["slug"]]

# ---------------- 生成循环 ----------------
FOOTERS = {
 "en": "PdfNest — free private PDF tools. Files never leave your browser. © 2026",
 "de": "PdfNest — kostenlose private PDF-Werkzeuge. Dateien verlassen nie Ihren Browser. © 2026",
 "fr": "PdfNest — outils PDF gratuits et privés. Les fichiers ne quittent jamais votre navigateur. © 2026",
 "es": "PdfNest — herramientas PDF gratuitas y privadas. Los archivos nunca salen de tu navegador. © 2026",
}

LD_WEBAPP_T = '{"@context":"https://schema.org","@type":"WebApplication","name":"__NAME__","url":"__URL__","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","browserRequirements":"Requires JavaScript","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"description":"__META__"}'
LD_FAQ_T = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[__ENTITIES__]}'

for lang in LANGS:
    tr = TR.get(lang) or {}
    # 首页
    grid = "".join(
        '<a href="/' + t["slug"] + ('' if lang == "en" else '-' + lang) + '.html">'
        + ((tr.get("tools") or {}).get(t["slug"], {}).get("h1", t["h1"]) if tr else t["h1"])
        + '<span>' + ((tr.get("tools") or {}).get(t["slug"], {}).get("intro", t["intro"])[:80] + '…') + '</span></a>'
        for t in TOOLS)
    hm = HOME_TRI.get(lang) or HOME_TRI["en"]
    hb = f"""
  <h1>{hm["h1"]}</h1>
  <p class="sub">{hm["sub"]}</p>
  <div class="grid">{grid}</div>
  <h2>{hm["h2"]}</h2>
  <p>{hm["p1"]}</p>
  <p>{hm["p2"]}</p>
"""
    pf = Path(page_file("index", lang))
    pf.write_text(render(lang, "index", hm["title"], hm["meta"], hb, "home"), encoding="utf-8")
    print("生成:", pf.name)
    # 工具页
    for t in TOOLS:
        body = tool_page(lang, t)
        pf = Path(page_file(t["slug"], lang))
        pf.write_text(body, encoding="utf-8")
        print("生成:", pf.name)
    # privacy / about
    EN_PAGES = {
      "privacy": {"title": "Privacy Policy | PdfNest", "meta": "PdfNest privacy policy — local-only PDF processing, cookies and advertising disclosure.",
        "body": """
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: October 2, 2026</p>
  <p>PdfNest ("we") provides free PDF tools that run <b>entirely in your browser</b>. This policy explains what data is — and is not — collected.</p>
  <h2>1. Your files</h2>
  <p><b>We never see your files.</b> Every processing step happens locally on your device via JavaScript/WebAssembly. Nothing is uploaded to any server, stored, or logged.</p>
  <h2>2. Server logs</h2>
  <p>Our hosting provider (Cloudflare) automatically records standard technical request data — IP address, browser type, URL, timestamp — for security and performance, governed by <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare's privacy policy</a>.</p>
  <h2>3. Cookies and advertising</h2>
  <p>We plan to display advertising served by Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on prior visits. Opt out via <a href="https://www.google.com/settings/ads">Google Ads Settings</a>; blocking cookies does not affect the tools.</p>
  <h2>4. Contact</h2>
  <p>Questions: <b>liuyulong667@gmail.com</b>.</p>"""},
      "about": {"title": "About PdfNest | PdfNest", "meta": "About PdfNest — free PDF tools in the browser, no upload required.",
        "body": """
  <h1>About PdfNest</h1>
  <p>PdfNest is a collection of fast, free PDF tools that run <b>entirely in your browser</b> — your documents are never uploaded to a server.</p>
  <h2>Why PdfNest exists</h2>
  <p>The big online PDF services make you upload private documents to their servers just to merge or rotate pages. We think that's backwards — at PdfNest everything happens locally.</p>
  <h2>Principles</h2>
  <ul><li><b>Local by default.</b> No upload step, because there never was one.</li>
  <li><b>Free means free.</b> No signup, no watermark, no limits.</li>
  <li><b>Tool first.</b> One task, done in seconds.</li></ul>
  <h2>Contact</h2>
  <p>Feedback: <b>liuyulong667@gmail.com</b>.</p>"""},
    }
    for kind in ["privacy", "about"]:
        d = tr.get(kind) if tr else None
        body = d["body"] if d else EN_PAGES[kind]["body"]
        title = d["title"] if d else EN_PAGES[kind]["title"]
        meta = d["meta"] if d else EN_PAGES[kind]["meta"]
        pf = Path(page_file(kind, lang))
        pf.write_text(render(lang, kind, title, meta, body, None), encoding="utf-8")
        print("生成:", pf.name)

# sitemap
lines = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for lang in LANGS:
    for base in ["index", *[t["slug"] for t in TOOLS], "privacy", "about"]:
        loc = site_url(base, lang)
        lines.append("  <url><loc>" + loc + "</loc></url>")
lines.append("</urlset>")
Path("sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("生成: sitemap.xml")

print("完成:", len(LANGS), "语言 ×", 2 + len(TOOLS), "页 =", len(LANGS) * (2 + len(TOOLS)), "页")
