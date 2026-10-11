"""Turn verified publication/manuscript metadata into accessible HTML cards."""
import html
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / "publications.json").read_text(encoding="utf-8"))
required = {"id", "title", "type", "year", "status", "summary", "topics", "url", "doi"}
seen = set()
parts = []
for item in items:
    if not required.issubset(item):
        raise ValueError(f"Missing fields for {item.get('id', '<unknown>')}: {required-set(item)}")
    if item["id"] in seen:
        raise ValueError(f"Duplicate publication id: {item['id']}")
    seen.add(item["id"])
    if item["url"] and urlparse(item["url"]).scheme != "https":
        raise ValueError(f"Use an https:// URL: {item['id']}")
    if item["doi"] and not item["doi"].startswith("10."):
        raise ValueError(f"DOIs should begin 10.: {item['id']}")
    esc = lambda value: html.escape(str(value), quote=True)
    topic_html = "".join(f'<span class="topic-tag">{esc(topic)}</span>' for topic in item["topics"])
    year = str(item["year"]) if item["year"] is not None else "Undated"
    search_text = " ".join([item["title"], item["type"], item["status"], item["summary"], str(item.get("authors") or ""), str(item.get("venue") or ""), " ".join(item["topics"]), year]).lower()
    link = ""
    if item["doi"]:
        doi_url = "https://doi.org/" + item["doi"]
        link = f'<a class="text-link" href="{esc(doi_url)}" rel="noopener" target="_blank">Read via DOI <span aria-hidden="true">↗</span></a>'
    elif item["url"]:
        link = f'<a class="text-link" href="{esc(item["url"])}" rel="noopener" target="_blank">View resource <span aria-hidden="true">↗</span></a>'
    citation_bits = []
    if item.get("authors"):
        citation_bits.append(esc(item["authors"]))
    if item["year"] is not None:
        citation_bits.append(f'({esc(item["year"])}).')
    if item.get("venue"):
        citation_bits.append(f'<em>{esc(item["venue"])}</em>')
    citation = (f'<p class="publication-citation">{" ".join(citation_bits)}</p>' if citation_bits else "")
    parts.append(f'''<article class="publication-card" data-search="{esc(search_text)}" data-kind="{esc(item['type'])}" data-status="{esc(item['status'])}">
      <div class="publication-topline"><span class="tiny-label">{esc(item['type'])}</span><span class="status-pill">{esc(item['status'])}</span></div>
      <h3>{esc(item['title'])}</h3>{citation}<p class="publication-summary">{esc(item['summary'])}</p>
      <div class="tagline">{topic_html}</div>{link}
    </article>''')
out = ROOT / "_includes" / "publication_cards.html"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(f"Generated {len(items)} cards in {out.relative_to(ROOT)}")
