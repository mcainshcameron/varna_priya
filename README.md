# Varna Priya

**Where the cosmos meets the craft table**

A static website showcasing intricate mandalas, celestial art, ethereal wallpapers, and handcrafted cosmic creations.

## About

Varna Priya is a digital sanctuary for cosmic art that bridges the digital and physical worlds. This website serves as:

- A professional portfolio for digital and physical crafts
- A free resource library for celestial wallpapers and mandalas
- A blog for creative insights and process articles
- A funnel to Ko-fi for premium content and support

## Quick Start

**To preview the website locally:**

1. Open `index.html` in your web browser
2. Try the language toggle (EN/RU) in the navigation
3. View your peacock feather hero image
4. Test the responsive design by resizing your browser

**To make it live:**

See the [Setup for GitHub Pages](#setup-for-github-pages) section below.

## Features

- **Peacock Feather Design**: Custom color palette inspired by your sacred geometry artwork
- **Bilingual Support**: English/Russian language toggle with localStorage persistence
- **Hero Image Integration**: Your peacock feather mandala as the welcoming centerpiece
- **Responsive Design**: Fully mobile-friendly with cosmic theme
- **Portfolio Gallery**: Filterable showcase of digital art and physical crafts
- **Blog System**: Article cards with categorization
- **Free Resources**: Download library with Ko-fi upsell
- **Animated UI**: Smooth scrolling, parallax effects, and cosmic starfield background
- **SEO Optimized**: Meta tags and semantic HTML
- **Fast & Lightweight**: Pure HTML/CSS/JS, no dependencies

## Project Structure

```
VarnaPriya/
│
├── Visuals.jpg            # Hero image - peacock feather mandala
├── index.html             # Homepage with hero image & translations
├── portfolio.html         # Portfolio gallery
├── blog.html              # Blog articles
├── blog-post-1.html       # Sample blog post
├── resources.html         # Free downloads
├── about.html             # About page
│
├── css/
│   └── style.css          # Peacock feather color palette
│
├── js/
│   └── main.js            # Interactivity + language toggle
│
├── README.md              # Setup guide
├── UPDATE-NOTES.md        # Recent changes documentation
└── .gitignore             # Git ignore file
```

## Setup for GitHub Pages

### 1. Initialize Git Repository

```bash
cd VarnaPriya
git init
git add .
git commit -m "Initial commit: Varna Priya cosmic website"
```

### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `varnapriya` (or your preferred name)
3. Do NOT initialize with README (we already have one)

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR-USERNAME/varnapriya.git
git branch -M main
git push -u origin main
```

### 4. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch
4. Click **Save**
5. Your site will be published at: `https://YOUR-USERNAME.github.io/varnapriya/`

### 5. Custom Domain (Optional)

To use a custom domain like `varnapriya.com`:

1. Add a `CNAME` file to the root directory with your domain
2. Configure DNS settings at your domain registrar:
   - Add a CNAME record pointing to `YOUR-USERNAME.github.io`
3. Update GitHub Pages settings with your custom domain

## Customization Guide

### Update Instagram & Ko-fi Links

Replace placeholder links throughout the HTML files:

- Instagram: `https://instagram.com/varnapriya`
- Ko-fi: `https://ko-fi.com/varnapriya`

Search and replace these URLs with your actual social media handles.

### Add Your Images

Replace the `.image-placeholder` divs with actual images:

```html
<!-- Before -->
<div class="image-placeholder">Image Title</div>

<!-- After -->
<img src="images/your-image.jpg" alt="Description">
```

Create an `images/` folder to store your artwork.

### Language Toggle

The website supports English and Russian out of the box. To add more content translations:

1. Find elements you want to translate
2. Add `data-en` and `data-ru` attributes:

```html
<h2 data-en="Welcome" data-ru="Добро пожаловать">Welcome</h2>
```

The language toggle automatically switches all elements with these attributes.

**To add another language** (e.g., Spanish):
1. Add `data-es` attributes to elements
2. Add a new button in the language toggle:
```html
<button class="lang-btn" data-lang="es">ES</button>
```
3. The JavaScript will handle the rest automatically

### Customize Colors

Edit the CSS variables in `css/style.css`. Current peacock feather palette:

```css
:root {
    --primary-color: #0d9488;    /* Teal */
    --secondary-color: #c87137;   /* Bronze */
    --accent-color: #c9a961;      /* Gold */
    --dark-bg: #1a2e2e;          /* Deep teal background */
    --teal-bright: #00a3a3;      /* Bright teal */
    --bronze: #d4823b;           /* Warm bronze */
    /* Adjust to match your artwork */
}
```

### Add Blog Posts

1. Create individual blog post HTML files (e.g., `blog-post-1.html`)
2. Use the same structure as other pages
3. Link from `blog.html` cards

### Add Download Files

1. Create a `downloads/` folder
2. Add your free resources (wallpapers, PDFs, etc.)
3. Update download button links in `resources.html`:

```javascript
button.addEventListener('click', function() {
    window.location.href = '/downloads/your-file.zip';
});
```

## Newsletter Integration

To add email collection, integrate with services like:

- [Mailchimp](https://mailchimp.com)
- [ConvertKit](https://convertkit.com)
- [Buttondown](https://buttondown.email)

Replace the newsletter form action in `blog.html`.

## Analytics (Optional)

Add Google Analytics or similar:

```html
<!-- Add before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Android)

## Performance

- No external dependencies (except Google Fonts)
- Optimized CSS animations
- Lazy loading ready for images
- Minimal JavaScript

## License

© 2024 Varna Priya. All rights reserved.

## Support

For questions or issues:
- Instagram: [@varnapriya](https://instagram.com/varnapriya)
- Ko-fi: [varnapriya](https://ko-fi.com/varnapriya)

---

**Built with cosmic energy ✨**
