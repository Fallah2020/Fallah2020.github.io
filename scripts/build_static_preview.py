"""Produce a browser-ready local preview from this website's HTML-authored QMD pages.

This is a preview tool, not a replacement for `quarto render` on GitHub Pages.
Usage: python3 scripts/build_publications.py && python3 scripts/build_static_preview.py --out-dir /tmp/profile_preview
"""
from pathlib import Path
from argparse import ArgumentParser
import html
import re
import shutil

root=Path(__file__).resolve().parents[1]
parser=ArgumentParser()
parser.add_argument('--out-dir',type=Path,default=root/'_preview')
a=parser.parse_args()
out=a.out_dir
out.mkdir(parents=True,exist_ok=True)
nav=[('Home','index.html'),('About','about.html'),('Research','research.html'),('Publications','publications.html'),('Research Tools','tools.html'),('Teaching','teaching.html'),('CV','cv.html'),('Contact','contact.html')]
navbar=''.join(f'<a class="nav-link" href="{href}">{html.escape(label)}</a>' for label,href in nav)
nav_style='''.nav-header{position:sticky;top:0;z-index:100;background:#fff;border-bottom:1px solid #dae2de}.nav-inner{display:flex;justify-content:space-between;align-items:center;gap:24px;min-height:68px}.nav-inner .navbar-nav{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end;align-items:center}.nav-header .navbar-brand{font-weight:800;letter-spacing:.11em;font-size:1rem;text-decoration:none;white-space:nowrap}.nav-footer{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}@media(max-width:900px){.nav-inner{display:block;padding:14px 0}.nav-inner .navbar-nav{justify-content:flex-start;gap:4px}.nav-link{padding:.35rem .4rem!important;font-size:.75rem!important}}@media(max-width:530px){.nav-header .navbar-brand{display:block;margin-bottom:9px}.nav-inner .navbar-nav{max-height:68px;overflow:auto;justify-content:flex-start}}'''

def parse_doc(file):
    txt=file.read_text(encoding='utf-8')
    # Metadata remains deliberately simple: pages have quoted YAML strings.
    front,body=re.match(r'\A---\n(.*?)\n---\n(.*)\Z',txt,re.S).groups()
    title=re.search(r'^title:\s*"(.*?)"\s*$',front,re.M)
    descr=re.search(r'^description:\s*"(.*?)"\s*$',front,re.M)
    body=re.sub(r'^```\{=html\}\s*\n|\n```\s*$', '', body.strip())
    body=body.replace('{{< include _includes/publication_cards.html >}}',(root/'_includes/publication_cards.html').read_text(encoding='utf-8'))
    return title.group(1) if title else file.stem, descr.group(1) if descr else '', body

for qmd in sorted(root.glob('*.qmd')):
    title,descr,body=parse_doc(qmd)
    page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+html.escape(title)+'''</title><meta name="description" content="'''+html.escape(descr,quote=True)+'''"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><style>'''+nav_style+'''</style></head><body><header class="nav-header navbar"><div class="site-wrap nav-inner"><a class="navbar-brand" href="index.html">FALLAH NYUMAH</a><nav class="navbar-nav" aria-label="Site navigation">'''+navbar+'''</nav></div></header><main id="main-content">'''+body+'''</main><footer class="nav-footer"><span>© 2026 Fallah Nyumah · Independent academic profile</span><span>Made with <a href="https://quarto.org/">Quarto</a> · GitHub Pages-ready source</span></footer><script src="assets/js/site.js" defer></script></body></html>'''
    (out/(qmd.stem+'.html')).write_text(page,encoding='utf-8')
for f in ['styles.css','robots.txt']:
    shutil.copy2(root/f,out/f)
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)
(out/'PREVIEW_README.txt').write_text('Fallah Nyumah | Browser-ready static preview\n\nOpen index.html in a web browser. Every linked page and the sanitized CV PDF are included. This is a static preview. To publish the real Quarto website, use the Quarto source ZIP with GitHub Pages and GitHub Actions.\n',encoding='utf-8')
print(f'Wrote {len(list(root.glob("*.qmd")))} HTML preview pages to {out}')
