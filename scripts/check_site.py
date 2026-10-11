"""Basic checks: required pages/resources exist, publications are not invented."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
expected = ["_quarto.yml", "index.qmd", "about.qmd", "research.qmd", "publications.qmd", "tools.qmd", "teaching.qmd", "cv.qmd", "contact.qmd", "404.qmd", "styles.css", "assets/js/site.js", "assets/fallah-nyumah-portrait.webp", "assets/Fallah_Nyumah_Public_CV.pdf", "_includes/publication_cards.html"]
missing = [p for p in expected if not (ROOT / p).exists()]
if missing:
    raise SystemExit("Missing website files: " + ", ".join(missing))
entries = json.loads((ROOT / "publications.json").read_text(encoding="utf-8"))
for p in entries:
    if not p.get("title") or not p.get("status"):
        raise SystemExit("Incomplete publication record")
    if p.get("type") == "Published journal article" and not (p.get("doi") or p.get("url")):
        raise SystemExit("Published works need a verifiable DOI or source URL")
print(f"Website checks passed: {len(expected)} required files, {len(entries)} publication records.")
