# Mesfin Genie Quarto Website

This is a Quarto academic personal website template prepared for Mesfin Genie.

## Local preview

1. Install Quarto: https://quarto.org/docs/get-started/
2. Open this folder in RStudio, VS Code, or Terminal.
3. Run:

```bash
quarto preview
```

## Render site

```bash
quarto render
```

The rendered website will be created in `_site/`.

## Publish options

### Option A: GitHub Pages

1. Create a GitHub repository, e.g. `mesfin-genie-website`.
2. Upload all files in this folder.
3. In GitHub, go to Settings → Pages.
4. Select GitHub Actions or deploy from the rendered `_site` branch/folder.
5. Add a custom domain such as `mesfingenie.com`.

### Option B: Netlify

1. Create a Netlify account.
2. Connect the GitHub repository.
3. Build command: `quarto render`
4. Publish directory: `_site`
5. Add your custom domain in Netlify Domain settings.

## Custom domain

Buy a domain from Namecheap, GoDaddy, Google Domains/Squarespace Domains, Cloudflare Registrar, or another registrar. Then point DNS records to the host:

- For GitHub Pages, use GitHub's recommended A records and CNAME.
- For Netlify, use Netlify DNS or add the CNAME/A records Netlify provides.

Replace `profile.jpg` with your official headshot. If no image is added, remove the `image: profile.jpg` line from `index.qmd`.
