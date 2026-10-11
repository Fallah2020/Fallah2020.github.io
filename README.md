# Fallah Nyumah — Academic Website

An original, responsive **Quarto** academic website designed for **GitHub Pages**. The site uses a minimal editorial layout inspired by the structure and readability of modern academic profiles, with original text, CSS, and design assets.

## Pages

- `index.qmd` — Home, research highlights, current work, collaboration
- `about.qmd` — Biography, four academic degrees, experience, scholarships
- `research.qmd` — Doctoral research, climate risk, study context
- `publications.qmd` — Three journal articles, 2023 MSc thesis, and searchable developing manuscripts
- `tools.qmd` — 3PG-RubPalm, LiRubPalm-GHG, Liberia Plantation DSS
- `teaching.qmd` — University of Toronto (FOR 201), AME University, and Tubman University
- `cv.qmd` — Resume-informed academic CV, awards, affiliations, skills, and public PDF download
- `contact.qmd` — Professional contact using the email supplied in the résumé

## Important: before public launch

Review the wording for accuracy. The supplied content reflects information available while preparing the draft. **Journal citations, thesis title, degrees, dates, jobs, skills, and awards come from the supplied résumé.** Two journal DOI values came from the résumé. A secondary scholarly index is linked for the 2022 teaching article because the original journal URL was not accessible during preparation. Current doctoral manuscripts remain clearly identified as in progress. The homepage uses the professional portrait you selected.

Personalize:
1. Your preferred professional portrait has been added as `assets/fallah-nyumah-portrait.webp` and referenced in `index.qmd`. Replace this file later if you want to switch to another portrait.
2. Check whether you want your personal Gmail address to appear publicly; it currently appears on `contact.qmd` and in the downloadable public CV. Add institutional email, Scholar, ORCID, and GitHub URLs if available.
3. Review `assets/Fallah_Nyumah_Public_CV.pdf` for accuracy before release. It omits residential address, telephone number, and professional membership identifiers.
4. Confirm and correct the listed academic degrees, completion dates, grades, role titles, and appointments.
5. Cross-check all résumé-sourced bibliography with final publisher records, especially the 2022 mathematics-education paper: external indexing differs from the résumé in author order/spelling. Preserve the correct published metadata.
6. If you have published Shiny apps, add verified deployment links to `tools.qmd`.
7. Set the public site URL in `_quarto.yml` after choosing your exact GitHub username. E.g., under `website:`, add `site-url: "https://YOUR-USERNAME.github.io"`.

## Preview locally (Quarto)

Install Quarto from https://quarto.org/docs/get-started/ (RStudio or VS Code are optional).

```bash
python3 scripts/build_publications.py
python3 scripts/check_site.py
quarto preview
```

The rendered website can be built with `quarto render`; the static output is written to `_site/`. For an additional standalone browser-ready preview, run `python3 scripts/build_static_preview.py`; the HTML preview goes in `_preview/`. No R installation is needed for this *website*: R/Shiny tools are described and can later be linked to an independent Shiny hosting service.

For a step-by-step guide, see **[PUBLISH_ON_GITHUB.md](PUBLISH_ON_GITHUB.md)**.

## Publish to GitHub Pages

1. Create a GitHub account if you do not already have one. Note the exact username.
2. Create a **public** repository named `USERNAME.github.io` (replace `USERNAME` with your username exactly).
3. Upload **all project files, including `.github/workflows/deploy.yml`**, to the repository root, and commit to the `main` branch. On GitHub's web uploader, check hidden directories are included; using Git on your computer is safer.
4. In repository **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**.
5. Open **Actions**. The workflow will generate publication cards, check the content, render Quarto, and deploy the `_site` directory. You can also run it manually with *Run workflow*.
6. The resulting URL is `https://USERNAME.github.io/` once deployment succeeds.

Workflow: `.github/workflows/deploy.yml`. It uses the official `quarto-dev/quarto-actions/setup` action plus GitHub Pages artifact/deploy actions. It does not require a personal access token.

**Avoid:** committing private data, unreviewed datasets, confidential contact details, unpublished source code, or working CV documents to the public repo.

## Add/update research outputs

Edit `publications.json`. Each item must have: `id`, `title`, `type`, `year` (or `null`), `status`, `summary`, `topics`, `url` (or `null`), `doi` (or `null`). Rebuild with:

```bash
python3 scripts/build_publications.py
quarto render
```

The GitHub workflow automatically regenerates `_includes/publication_cards.html` on every push. Search and stage filtering are implemented by `assets/js/site.js` and preserve a readable no-JavaScript listing.

## Replace contact placeholders

For a verified contact email, replace the explanatory paragraph in `contact.qmd` with, for example:

```html
<a class="text-link" href="mailto:you@university.edu">you@university.edu ↗</a>
```

The supplied résumé contains a Gmail contact already used in the updated website. Do not publish personal home addresses, telephone numbers, or confidential identifiers without an explicit decision to do so.

## Design files

- `styles.css` — color palette, fonts, spacing, layout, responsive behavior
- `assets/favicon.svg` — original monogram favicon
- `assets/fallah-nyumah-portrait.webp` — current professional portrait used on the homepage
- `assets/js/site.js` — publication search and status filtering

## References

- Quarto websites: https://quarto.org/docs/websites/
- Quarto GitHub Pages: https://quarto.org/docs/publishing/github-pages.html
- GitHub Pages: https://docs.github.com/en/pages

No copying of the reference site's proprietary content, photographs, CV, stylesheets, or images was used.

## Résumé integration (October 2026)

Added all four qualifications, six professional/academic appointments, FOR 201 and AME course experience, the UNFCCC remote internship, three published journal articles, the 2023 thesis, research methods, software skills, scholarships and awards, and professional affiliations. Current doctoral projects remain works in progress.

**Privacy safeguard:** The complete uploaded résumé is not included in the website repository. The downloadable CV is a new public edition with no home street address, telephone number, or professional membership/PMI identifiers. The personal Gmail contact is visible, since it was provided as the résumé contact; remove it if a public email address is not desired.

**Source priority:** Résumé entries are reproduced without inventing unprovided journal DOIs, publications, or positions. Before publishing, validate the 2022 education-paper citation against the authoritative article record.
