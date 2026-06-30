# Mesfin Genie premium Quarto website

Upload all files in this folder to the GitHub repository `DrGenie/DrGenie.github.io`.

## How to update

- Replace the MG placeholder with a professional photo by adding `assets/profile.jpg` and editing `index.qmd`.
- Add the current CV as `assets/Mesfin_Genie_CV.pdf` and link it in `cv.qmd`.
- Export your full Google Scholar BibTeX and replace `assets/publications.bib`.
- Use `assets/publications_by_field.csv` to classify publications by field.

## GitHub Pages

The workflow in `.github/workflows/publish.yml` renders and publishes the Quarto site automatically.
