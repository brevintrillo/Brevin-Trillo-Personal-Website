# Brevin — Modern Personal Website

A modern responsive personal website built with Python and Flask.

## Features

- Responsive desktop/mobile layout
- Modern glassmorphism-inspired UI
- Dark/light mode
- Mobile navigation
- Hero section
- About section
- Skills
- Services
- Portfolio/project cards
- Photo gallery placeholders
- Timeline
- Contact form
- Flash messages
- Simple admin/project overview page
- Smooth scrolling and reveal animations
- SEO-friendly metadata
- Social links
- Easy customization

## Run locally

### 1. Create a virtual environment

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the site

```bash
python app.py
```

Then open:

http://127.0.0.1:5000

Admin/project preview:

http://127.0.0.1:5000/admin

## Customize

Edit `templates/index.html` for your name, bio and links.

Edit `app.py` to change project data.

Place your images in:
`static/images/`

Replace the gallery placeholders with your own image URLs or local files.

## Important before publishing

Change `SECRET_KEY` to a strong random value and run Flask behind a production WSGI server. The included `/admin` page is only a project preview and is not an authenticated administration system.
