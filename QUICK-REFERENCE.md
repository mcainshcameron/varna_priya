# Quick Reference - Where to Put Files

## 🖼️ Images

### Hero Image (Homepage Banner)
```
📁 assets/images/hero/
   └── peacock-feather.jpg (1200x1200px, JPEG)
```

### Portfolio Images
```
📁 assets/images/portfolio/
   ├── digital-mandalas/
   │   ├── display/           → Website gallery (800x800px JPEG, ~150KB)
   │   └── originals/         → Download versions (4000x4000px PNG)
   │
   ├── physical-crafts/
   │   ├── display/           → Website gallery (800x600px JPEG)
   │   └── originals/         → High-res photos (PNG)
   │
   └── celestial-wallpapers/
       ├── display/           → Preview (800x450px JPEG)
       └── originals/         → Full wallpapers (3840x2160px PNG)
```

### Blog Images
```
📁 assets/images/blog/
   ├── featured/              → Blog post headers (1200x675px JPEG)
   └── content/               → Images within posts (1000px wide JPEG)
```

---

## 📝 Blog Posts

```
📁 blog/posts/
   ├── post-template.html              → Copy this for new posts
   ├── 2024-03-15-post-title.html     → Your blog posts
   └── 2024-04-01-another-post.html   → (Format: YYYY-MM-DD-title.html)
```

**Steps to add blog post:**
1. Copy `post-template.html`
2. Rename: `YYYY-MM-DD-title.html`
3. Add featured image to `assets/images/blog/featured/`
4. Edit content
5. Update `blog.html` main page

---

## 📦 Free Downloads

```
📁 downloads/
   ├── free-resources/
   │   ├── wallpapers/        → Desktop/mobile wallpapers (PNG)
   │   ├── mandalas/          → Printable PDFs
   │   ├── patterns/          → Seamless patterns (PNG)
   │   └── templates/         → Design templates (PSD/PNG)
   │
   └── preview/               → Preview thumbnails (400x300px JPEG)
```

**Steps to add free resource:**
1. Save file to appropriate `/free-resources/[category]/`
2. Create preview (400x300px) → save to `/preview/`
3. Update `resources.html`

---

## 🎯 Most Common Tasks

### Add New Portfolio Mandala
1. **Original:** `assets/images/portfolio/digital-mandalas/originals/mandala-name.png`
2. **Display:** `assets/images/portfolio/digital-mandalas/display/mandala-name.jpg`
3. **Update:** `portfolio.html`

### Add Free Wallpaper
1. **File:** `downloads/free-resources/wallpapers/wallpaper-name.png`
2. **Preview:** `downloads/preview/preview-wallpaper-name.jpg`
3. **Update:** `resources.html`

### Write Blog Post
1. **Copy:** `blog/posts/post-template.html`
2. **Rename:** `blog/posts/2024-XX-XX-title.html`
3. **Featured Image:** `assets/images/blog/featured/blog-2024-XX-XX-title.jpg`
4. **Update:** `blog.html`

### Change Hero Image
1. **Upload:** `assets/images/hero/new-hero.jpg`
2. **Update:** `index.html` (line ~38)

---

## 📏 Image Size Cheat Sheet

| Type | Display Size | Original Size |
|------|-------------|---------------|
| Hero | 1200x1200px | Same |
| Portfolio Mandala | 800x800px | 4000x4000px |
| Physical Craft | 800x600px | 2000x1500px |
| Wallpaper | 800x450px | 3840x2160px |
| Blog Featured | 1200x675px | Same |
| Blog Content | 1000px wide | Same |
| Download Preview | 400x300px | N/A |

---

## ✅ Checklist Before Pushing to GitHub

- [ ] Images compressed and optimized
- [ ] File names use lowercase and hyphens (no spaces)
- [ ] Display + Original versions for portfolio items
- [ ] Preview images created for downloads
- [ ] HTML updated with new content
- [ ] Tested locally in browser
- [ ] Ready to `git add . && git commit && git push`

---

## 🚀 Quick Git Commands

```bash
# Check status
git status

# Add all changes
git add .

# Commit
git commit -m "Add new portfolio items and blog post"

# Push to GitHub
git push

# All in one
git add . && git commit -m "Update content" && git push
```

---

**Need full details?** See `FOLDER-STRUCTURE.md`
