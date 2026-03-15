# Varna Priya - Folder Structure Guide

This guide explains the complete folder structure for easy content management through Telegram/OpenClaw.

## 📁 Complete Folder Tree

```
varna_priya/
│
├── assets/
│   └── images/
│       ├── hero/                    # Main hero/banner images
│       │   └── peacock-feather.jpg  # Current hero image
│       │
│       ├── portfolio/               # Portfolio showcase images
│       │   ├── digital-mandalas/
│       │   │   ├── display/         # Compressed for website (JPEG, ~200KB)
│       │   │   └── originals/       # High-res for downloads (PNG, full quality)
│       │   │
│       │   ├── physical-crafts/
│       │   │   ├── display/         # Compressed for website
│       │   │   └── originals/       # High-res for downloads
│       │   │
│       │   └── celestial-wallpapers/
│       │       ├── display/         # Compressed for website
│       │       └── originals/       # High-res for downloads
│       │
│       └── blog/                    # Blog post images
│           ├── featured/            # Featured/header images for posts
│           └── content/             # Images used within blog posts
│
├── blog/
│   └── posts/                       # Blog post HTML/Markdown files
│       ├── 2024-03-15-creating-mandalas.html
│       ├── 2024-03-08-cosmic-crafts.html
│       └── post-template.html       # Template for new posts
│
├── downloads/
│   ├── free-resources/              # Free downloadable content
│   │   ├── wallpapers/              # Desktop/mobile wallpapers
│   │   ├── mandalas/                # Printable mandalas (PDF/PNG)
│   │   ├── patterns/                # Seamless patterns
│   │   └── templates/               # Design templates
│   │
│   └── preview/                     # Preview images for download page
│       └── (thumbnails of downloadable items)
│
├── css/
│   └── style.css
│
├── js/
│   └── main.js
│
├── index.html
├── portfolio.html
├── blog.html
├── resources.html
├── about.html
└── blog-post-1.html
```

---

## 📋 Folder Purposes

### 1. `/assets/images/hero/`
**What goes here:** Main hero/banner images for the homepage

**File naming:**
- `peacock-feather.jpg` (current hero)
- `seasonal-hero-winter.jpg` (optional seasonal variants)

**Specifications:**
- Format: JPEG
- Size: 1200x1200px (square)
- Quality: 85%
- Max file size: ~300KB

**When to update:**
- New hero artwork
- Seasonal changes
- Rebranding

---

### 2. `/assets/images/portfolio/digital-mandalas/`

#### `/display/` subfolder
**What goes here:** Compressed versions for website gallery display

**File naming convention:**
- `mandala-001.jpg`
- `mandala-002.jpg`
- `mandala-lunar-symmetry.jpg`

**Specifications:**
- Format: JPEG
- Size: 800x800px
- Quality: 75-80%
- Max file size: ~150KB

#### `/originals/` subfolder
**What goes here:** High-resolution originals for user downloads

**File naming:** (same name as display version)
- `mandala-001.png`
- `mandala-lunar-symmetry.png`

**Specifications:**
- Format: PNG
- Size: 4000x4000px or higher
- Quality: Maximum (lossless)
- File size: 5-15MB

**How it works:**
1. Upload your original high-res PNG to `/originals/`
2. Create compressed JPEG for `/display/`
3. Website shows compressed version
4. Users can download original from link

---

### 3. `/assets/images/portfolio/physical-crafts/`

**What goes here:** Photos of physical items (glass paintings, crochet, jewelry)

**Same structure as digital-mandalas:**
- `/display/` - Compressed for web (JPEG, 800x600px)
- `/originals/` - High-res photos (PNG, full size)

**File naming:**
- `craft-glass-painting-01.jpg`
- `craft-crochet-moon-blanket.jpg`
- `craft-jewelry-celestial-necklace.jpg`

**Special note:** Add "DM to Purchase" button on portfolio page for these

---

### 4. `/assets/images/portfolio/celestial-wallpapers/`

**What goes here:** Wallpaper artwork

**Structure:**
- `/display/` - Preview thumbnails (800x450px)
- `/originals/` - Full desktop wallpapers (3840x2160px)

**File naming:**
- `wallpaper-starlight-dreams.jpg`
- `wallpaper-nebula-nights.jpg`

---

### 5. `/assets/images/blog/`

#### `/featured/` subfolder
**What goes here:** Featured images for blog posts (shown on blog listing)

**File naming:**
- `blog-2024-03-15-creating-mandalas.jpg`
- `blog-2024-03-08-cosmic-crafts.jpg`

**Specifications:**
- Format: JPEG
- Size: 1200x675px (16:9)
- Quality: 80%
- Max file size: ~200KB

#### `/content/` subfolder
**What goes here:** Images used within blog post content

**File naming:**
- `post-creating-mandalas-process-1.jpg`
- `post-creating-mandalas-tools.jpg`

**Specifications:**
- Format: JPEG
- Size: 1000px wide
- Quality: 75-80%

---

### 6. `/blog/posts/`

**What goes here:** Individual blog post files

**File naming convention:**
- `YYYY-MM-DD-post-title.html`
- Example: `2024-03-15-creating-mandalas.html`

**Template provided:** `post-template.html`

**How to add a new post:**
1. Copy `post-template.html`
2. Rename to `YYYY-MM-DD-your-title.html`
3. Edit content
4. Add featured image to `/assets/images/blog/featured/`
5. Update `blog.html` to link to new post

---

### 7. `/downloads/free-resources/`

#### `/wallpapers/`
**What goes here:** Free downloadable wallpapers

**File naming:**
- `wallpaper-desktop-starlight-dreams.png` (3840x2160)
- `wallpaper-mobile-starlight-dreams.png` (1080x2400)

**Formats:** PNG or JPEG
**Users download:** Full quality versions

#### `/mandalas/`
**What goes here:** Printable mandalas (coloring pages, meditation guides)

**File naming:**
- `mandala-coloring-01.pdf`
- `mandala-mini-pack.pdf`

**Format:** PDF (print-ready, 300 DPI)

#### `/patterns/`
**What goes here:** Seamless patterns for design projects

**File naming:**
- `pattern-cosmic-stars.png`
- `pattern-celestial-set.zip` (bundle)

**Format:** PNG (tileable/seamless)

#### `/templates/`
**What goes here:** Design templates (Instagram stories, social media)

**File naming:**
- `template-instagram-story-cosmic.psd`
- `template-social-media-bundle.zip`

**Format:** PSD, PNG, or ZIP

---

### 8. `/downloads/preview/`

**What goes here:** Preview/thumbnail images for the resources page

**File naming:** (matches the download filename)
- `preview-wallpaper-starlight-dreams.jpg`
- `preview-mandala-coloring-01.jpg`

**Specifications:**
- Format: JPEG
- Size: 400x300px
- Quality: 75%
- Max file size: ~50KB

**Purpose:** Shows users what they're downloading before clicking

---

## 🔄 Typical Workflow

### Adding a New Portfolio Item (Digital Mandala)

1. **Create the artwork** (high-resolution PNG)
2. **Save original:** `/assets/images/portfolio/digital-mandalas/originals/mandala-new-work.png`
3. **Create compressed version:** Resize to 800x800px, save as JPEG
4. **Save display:** `/assets/images/portfolio/digital-mandalas/display/mandala-new-work.jpg`
5. **Update portfolio.html:** Add new portfolio item with image paths
6. **Commit and push** to GitHub

### Adding a Free Resource

1. **Create the resource** (wallpaper, PDF, etc.)
2. **Save resource:** `/downloads/free-resources/wallpapers/new-wallpaper.png`
3. **Create preview:** Thumbnail version, 400x300px
4. **Save preview:** `/downloads/preview/preview-new-wallpaper.jpg`
5. **Update resources.html:** Add new resource card with download link
6. **Commit and push**

### Writing a Blog Post

1. **Copy template:** `blog/posts/post-template.html`
2. **Rename:** `blog/posts/2024-XX-XX-post-title.html`
3. **Add featured image:** `/assets/images/blog/featured/blog-2024-XX-XX-post-title.jpg`
4. **Add content images:** `/assets/images/blog/content/post-title-image-1.jpg`
5. **Edit post content** with your text and images
6. **Update blog.html:** Add new blog card linking to your post
7. **Commit and push**

---

## 📝 Quick Reference Commands

### Via Telegram with OpenClaw

**Upload new hero image:**
```
Upload to: assets/images/hero/
Filename: peacock-feather-new.jpg
Then update: index.html (line 38)
```

**Add portfolio image:**
```
Upload original to: assets/images/portfolio/digital-mandalas/originals/
Upload display to: assets/images/portfolio/digital-mandalas/display/
Update: portfolio.html
```

**Add free resource:**
```
Upload file to: downloads/free-resources/[category]/
Upload preview to: downloads/preview/
Update: resources.html
```

---

## ✅ Best Practices

1. **Always use descriptive filenames** (no spaces, use hyphens)
2. **Maintain original + display pairs** for portfolio items
3. **Compress images before upload** (use TinyPNG, ImageOptim, etc.)
4. **Keep previews small** (<50KB) for fast page loading
5. **Organize by date** for blog posts (YYYY-MM-DD prefix)
6. **Test locally** before pushing to GitHub
7. **Update HTML** when adding new images/resources

---

## 🎯 Image Size Guidelines

| Content Type | Display Size | Original Size |
|--------------|--------------|---------------|
| Hero Image | 1200x1200px | Same |
| Portfolio Digital | 800x800px | 4000x4000px+ |
| Portfolio Physical | 800x600px | 2000x1500px+ |
| Wallpapers | 800x450px | 3840x2160px |
| Blog Featured | 1200x675px | Same |
| Blog Content | 1000px wide | Same |
| Download Previews | 400x300px | N/A |

---

**This structure makes it easy to:**
- Find any content quickly
- Manage uploads via Telegram/OpenClaw
- Separate web-optimized from high-quality versions
- Keep organized as your content grows
- Know exactly where to put new files

📧 Questions? Check the file or ask for clarification!
