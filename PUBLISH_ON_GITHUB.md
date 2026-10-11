# Publish this academic website using GitHub Pages

Your selected blue-shirt professional portrait is already included in `assets/fallah-nyumah-portrait.webp` and displayed on the homepage.

## Preparation

1. Your GitHub account is `Fallah2020`. The website will be available at `https://fallah2020.github.io/` after a successful deployment.
2. Review the site's contact email, PDF CV, publications, and research entries before making them public. GitHub Pages websites are public.
3. Download/unzip the **source project ZIP**. The project files should be at the ZIP's top level: `_quarto.yml`, `index.qmd`, `.github/`, `assets/`, and other pages. Do **not** upload the preview ZIP as the Quarto source.

## Recommended method: GitHub Desktop (Windows or macOS)

1. On github.com, create a **public repository** named exactly `Fallah2020.github.io` (replace with your actual GitHub username). Choose **Add a README file** when creating it.
2. Install and sign into GitHub Desktop: https://desktop.github.com/. Use **File → Clone repository** to clone `Fallah2020.github.io` to your computer.
3. Extract the source ZIP, then copy **all the contents** (not an extra enclosing folder) into the cloned repository folder. Preserve the hidden `.github/workflows/deploy.yml` directory and the `assets/` folder.
4. In GitHub Desktop, check changed files, enter commit summary `Add academic website`, select **Commit to main**, then **Push origin**.
5. On github.com, open repository **Settings → Pages**, and under **Build and deployment**, set **Source** to **GitHub Actions**. You do not need to create another workflow; `.github/workflows/deploy.yml` is already included.
6. Open the repository's **Actions** tab, select **Build and deploy academic website**, and watch for both **build** and **deploy** jobs to succeed. If it does not start, use **Run workflow** (select the `main` branch).
7. Visit `https://Fallah2020.github.io/` after successful deployment.

## Alternative: upload from the GitHub website

Create the same repository. Select **Add file → Upload files**, upload all extracted files and directories to the **repository root**, and commit to `main`. Make sure the hidden `.github/workflows/deploy.yml` file is actually present on GitHub. If your browser does not upload hidden directories, use GitHub Desktop above or create that workflow file manually via **Add file → Create new file** with the filename `.github/workflows/deploy.yml`, copying it from the extracted project.

## Common problems

- **Site shows a README or a 404 error:** ensure **Settings → Pages → Source** is **GitHub Actions**, and confirm a successful deploy job.
- **No build runs:** verify `.github/workflows/deploy.yml` exists in the root and that your branch is called `main`.
- **Build fails:** open **Actions**, click the failed run and the failed step, and share the error message.
- **Missing photo:** the site must include `assets/fallah-nyumah-portrait.webp`; `index.qmd` already references this file.
- **Wrong website address:** for a personal site, the repo name must match the account exactly: `Fallah2020.github.io`.
- **Accidentally uploaded a `work_website/` folder:** move its contents to the repository **root**, so `_quarto.yml` and `.github/` are at the top level.

## Updating the website later

Edit your `.qmd` pages or `publications.json`, commit and push to `main`. The included GitHub Actions workflow regenerates publication cards, builds the Quarto website, and republishes the site. You do not need a separate hosting account or personal access token.

## Official references

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/quickstart
- https://quarto.org/docs/publishing/github-pages.html

## Personalized project settings

- GitHub user: `Fallah2020`
- GitHub repository: `Fallah2020.github.io`
- Published site: `https://fallah2020.github.io/`
- Quarto site-url: configured to match the public website
- Homepage portrait: `assets/fallah-nyumah-portrait.webp` (preferred second photo)

**Reminder:** Upload the extracted *contents*, not the ZIP itself. If the first deployment fails, open the repository's Actions tab, select the failed run, and inspect the failed step.
