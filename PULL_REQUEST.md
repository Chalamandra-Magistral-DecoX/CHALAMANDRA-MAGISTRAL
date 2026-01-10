# Pull Request: Refactor & Cleanup Chalamandra Magistral

## Summary of Changes

This PR streamlines the repository structure and aligns the documentation with the "Chalamandra Magistral" brand identity.

### 1. File Reorganization
- **Moved Documentation**: `brand-kit/archetype.md` -> `docs/archetype.md`.
- **Flattened Methodologies**: `metodologias/index.html` -> `metodologias.html` (moved to root).
- **Cleanup**: Removed empty `brand-kit/` and `metodologias/` directories.

### 2. Documentation Update
- **README.md**: Completely rewritten to reflect the conceptual, non-technical tone of the project. Removed technical instructions and replaced them with the "Bunker of Cognitive Sovereignty" narrative.

### 3. Navigation Fixes
- **index.html**: Updated the "Lanzar Dado" link to point to the new location `metodologias.html`.
- **metodologias.html**: Verified that the move to root did not break internal logic (the file is self-contained or uses absolute/CDN paths).

## Verification

### Manual Checks
- **Links**: Confirmed `index.html` links correctly to `metodologias.html`.
- **Assets**: Confirmed `metodologias.html` loads correctly without broken relative paths.

### Automated Checks
- **Frontend Verification**: Ran Playwright scripts to capture screenshots of `metodologias.html` and `index.html`.
    - Verified page titles.
    - Verified CSS loading.
    - Verified JS execution.

## Next Steps
- Deploy to Vercel/Netlify (configuration required if not static).
- Continue building out the "Chola", "Fresa", etc. modules as planned.
