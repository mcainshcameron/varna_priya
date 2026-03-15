# Bot Automation Guide for Varna Priya

This guide helps OpenClaw (or any bot) automatically manage website content through Telegram.

## 🤖 Supported Commands

### 1. Add Blog Post
**User says:** "Create blog post about [topic]"

**Bot actions:**
1. Generate blog post content based on topic
2. Create filename: `blog/posts/YYYY-MM-DD-[topic-slug].html`
3. Copy from `blog/posts/post-template.html`
4. Fill in: title, date, content, category
5. If user uploads image:
   - Save to `assets/images/blog/featured/blog-YYYY-MM-DD-[topic-slug].jpg`
   - Update post with image path
6. Update `blog.html` - add new blog card
7. Git commit: "Add blog post: [title]"
8. Git push

**Example:**
```
User: "Create blog post about glass painting techniques"
Bot: Creates blog/posts/2024-03-15-glass-painting-techniques.html
Bot: Prompts for featured image
User: [uploads image]
Bot: Saves to assets/images/blog/featured/
Bot: Updates blog.html
Bot: "✅ Blog post published!"
```

---

### 2. Add Portfolio Mandala
**User says:** "Add new mandala" or "Upload mandala design"

**Bot actions:**
1. Prompt for mandala name/title
2. Receive uploaded image (should be high-res PNG)
3. Save original: `assets/images/portfolio/digital-mandalas/originals/mandala-[name].png`
4. Auto-compress and save: `assets/images/portfolio/digital-mandalas/display/mandala-[name].jpg`
   - Resize to 800x800px
   - JPEG quality 75%
5. Update `portfolio.html` - add portfolio item with:
   - Display image in gallery
   - Link to original for download
   - Title and description
6. Git commit: "Add portfolio mandala: [name]"
7. Git push

**Example:**
```
User: "Add new mandala"
Bot: "What's the name of this mandala?"
User: "Lunar Symmetry"
User: [uploads high-res PNG]
Bot: Saving originals/mandala-lunar-symmetry.png
Bot: Creating compressed display version
Bot: Updating portfolio.html
Bot: "✅ Mandala added to portfolio!"
```

---

### 3. Add Physical Craft
**User says:** "Add physical craft" or "Upload craft photo"

**Bot actions:**
1. Prompt for craft name and type (glass painting/crochet/jewelry)
2. Receive uploaded photo
3. Save original: `assets/images/portfolio/physical-crafts/originals/craft-[type]-[name].png`
4. Auto-compress: `assets/images/portfolio/physical-crafts/display/craft-[type]-[name].jpg`
5. Update `portfolio.html` - add with "DM to Purchase" button
6. Git commit and push

---

### 4. Add Free Resource (Wallpaper)
**User says:** "Add free wallpaper"

**Bot actions:**
1. Prompt for wallpaper name
2. Receive uploaded image (should be high-res)
3. Save to: `downloads/free-resources/wallpapers/wallpaper-[name].png`
4. Auto-create preview (400x300px): `downloads/preview/preview-wallpaper-[name].jpg`
5. Update `resources.html` - add resource card with:
   - Preview image
   - Download button
   - Title and description
6. Git commit and push

**Example:**
```
User: "Add free wallpaper"
Bot: "What should we call this wallpaper?"
User: "Starlight Dreams"
User: [uploads 4K wallpaper PNG]
Bot: Saving to downloads/free-resources/wallpapers/
Bot: Creating preview thumbnail
Bot: Updating resources.html
Bot: "✅ Free wallpaper added! Users can now download it."
```

---

### 5. Add Free PDF (Mandala/Template)
**User says:** "Add free PDF" or "Add coloring mandala"

**Bot actions:**
1. Prompt for PDF name and category
2. Receive uploaded PDF
3. Save to: `downloads/free-resources/[category]/[name].pdf`
4. Prompt for preview image OR auto-generate from PDF cover
5. Save preview: `downloads/preview/preview-[name].jpg`
6. Update `resources.html`
7. Git commit and push

---

### 6. Change Hero Image
**User says:** "Change hero image" or "Update homepage banner"

**Bot actions:**
1. Receive uploaded image
2. Validate size (should be square, ideally 1200x1200px)
3. Save to: `assets/images/hero/peacock-feather.jpg` (or versioned name)
4. Update `index.html` line ~38 with image path
5. Git commit and push

---

### 7. Update Social Links
**User says:** "Update Instagram link" or "Update Ko-fi link"

**Bot actions:**
1. Prompt for new URL
2. Find and replace all instances in HTML files
3. Git commit: "Update [platform] link"
4. Git push

---

## 📋 Content Type Mapping

The bot should recognize these keywords:

| User Intent | Keywords | Action |
|-------------|----------|--------|
| Blog post | "blog", "article", "post", "write about" | Create blog post |
| Portfolio mandala | "mandala", "portfolio", "design", "artwork" | Add to digital-mandalas |
| Physical craft | "craft", "physical", "glass", "crochet", "jewelry" | Add to physical-crafts |
| Free wallpaper | "wallpaper", "background", "freebie wallpaper" | Add to free-resources/wallpapers |
| Free PDF | "pdf", "printable", "coloring page", "template" | Add to free-resources |
| Hero image | "hero", "banner", "homepage image" | Update hero |
| Social link | "instagram", "ko-fi", "link" | Update links |

---

## 🔄 Auto-Processing Rules

### Image Compression
Bot should automatically create compressed versions:

**Portfolio Images:**
- Original: Keep as-is in `/originals/`
- Display: Resize to 800x800px, JPEG 75%, save to `/display/`

**Blog Images:**
- Featured: Resize to 1200x675px, JPEG 80%
- Content: Resize to max 1000px wide, JPEG 75%

**Download Previews:**
- Always 400x300px, JPEG 75%, max 50KB

### File Naming
Bot should auto-generate filenames:

**Pattern:**
- Blog: `YYYY-MM-DD-slug.html`
- Images: `type-name.ext` (lowercase, hyphens)
- Downloads: `category-name.ext`

**Examples:**
- ✅ `2024-03-15-glass-painting-guide.html`
- ✅ `mandala-lunar-symmetry.png`
- ✅ `wallpaper-starlight-dreams.png`
- ❌ `Blog Post 1.html`
- ❌ `My New Mandala.PNG`

---

## 🎯 Required Information

For each content type, bot should collect:

### Blog Post
- Title
- Topic/description (bot can write content)
- Category (Process/Tutorial/Inspiration/etc.)
- Featured image (optional - bot can use placeholder)

### Portfolio Item
- Name/title
- Type (mandala/craft/wallpaper)
- High-res image file
- Description (optional - bot can generate)

### Free Resource
- Name/title
- Category (wallpaper/mandala/pattern/template)
- File (image or PDF)
- Description (optional)

---

## ✅ Success Confirmation

After each action, bot should respond:

```
✅ [Action] completed!

📝 What was done:
- Created: [file path]
- Updated: [HTML file]
- Committed: [commit message]
- Pushed to GitHub

🌐 Live in 2-3 minutes at:
https://mcainshcameron.github.io/varna_priya/

Want to add anything else?
```

---

## 🚨 Error Handling

Bot should handle:

**Missing Information:**
```
❌ Missing image. Please upload the image file.
```

**Wrong File Type:**
```
❌ Expected PNG/JPEG, received PDF
Try uploading an image file instead.
```

**Large File:**
```
⚠️ Image is 15MB. This might take a moment to compress...
✅ Compressed to 2MB for optimal web performance.
```

---

## 🔧 Bot Configuration

Suggested config file for the bot:

```json
{
  "content_types": {
    "blog_post": {
      "folder": "blog/posts/",
      "template": "blog/posts/post-template.html",
      "naming": "YYYY-MM-DD-{slug}.html",
      "images": "assets/images/blog/featured/",
      "update_file": "blog.html"
    },
    "portfolio_mandala": {
      "display": "assets/images/portfolio/digital-mandalas/display/",
      "originals": "assets/images/portfolio/digital-mandalas/originals/",
      "naming": "mandala-{name}.{ext}",
      "update_file": "portfolio.html",
      "display_size": "800x800",
      "format": "jpg",
      "quality": 75
    },
    "free_wallpaper": {
      "folder": "downloads/free-resources/wallpapers/",
      "preview": "downloads/preview/",
      "naming": "wallpaper-{name}.png",
      "update_file": "resources.html",
      "preview_size": "400x300"
    }
  }
}
```

---

## 💡 Smart Features

**Auto-suggestions:**
- Suggest filename based on content
- Auto-categorize based on keywords
- Suggest related content to link

**Batch operations:**
- "Upload 5 new mandalas" → processes all at once
- "Add these 3 wallpapers as freebies" → batch upload

**Content generation:**
- Write blog post content from topic
- Generate image descriptions
- Create SEO-friendly titles

---

This structure makes bot management intuitive and automated!
