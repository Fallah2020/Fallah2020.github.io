# Fallah2020 — academic website publishing checklist

1. Sign in at https://github.com/ (username: `Fallah2020`).
2. Create a **public** repository named exactly `Fallah2020.github.io`: https://github.com/new.
3. Download this ZIP and **extract** it. Upload the *contents* of the extracted folder, not the ZIP itself. Ensure `_quarto.yml`, `index.qmd`, `assets/`, and `.github/workflows/deploy.yml` appear at the top level of the repository.
4. Commit files to the `main` branch.
5. On GitHub open **Settings → Pages → Build and deployment → Source → GitHub Actions**. Do not create an additional workflow.
6. Open **Actions** and find **Build and deploy academic website**. Confirm both build and deploy jobs succeed.
7. Visit https://fallah2020.github.io/ . The site may take a few minutes to appear after successful deployment.

If the hidden `.github` folder doesn't upload through the browser, use GitHub Desktop (https://desktop.github.com/) or manually create `.github/workflows/deploy.yml` using the supplied file.

Review personal details before uploading: a public GitHub Pages site and repository make your content accessible online.
