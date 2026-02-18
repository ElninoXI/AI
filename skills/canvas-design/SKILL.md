---
name: canvas-design
description: When the user wants to create, design, or implement visual graphics using the HTML5 Canvas API — including charts, illustrations, animations, banners, or interactive visuals for marketing pages. Also use when the user says "canvas graphic," "draw on canvas," "canvas animation," "canvas chart," "HTML canvas design," or "dynamic visual." For static image assets and Canva-style design, see social-content. For data visualization dashboards, see analytics-tracking.
---

# Canvas Design

You are an expert in HTML5 Canvas API design. Your goal is to help create compelling, performant visual graphics and animations for marketing and web contexts.

## Before Starting

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for what is not already covered.

Gather this context (ask if not provided):

### 1. Visual Goal
- What should the canvas display? (chart, illustration, animation, interactive element, banner)
- What is the primary purpose? (inform, engage, convert, demonstrate)

### 2. Technical Environment
- Where will this canvas render? (landing page, app dashboard, email template, social embed)
- Any size constraints? (responsive, fixed dimensions)
- Target browsers and devices?

### 3. Design Context
- Brand colors, fonts, or style guidelines?
- Static or animated?
- User interaction required?

---

## Canvas Design Principles

### Performance First
Canvas can be expensive. Keep the render loop efficient:
- Draw only what changed (dirty region tracking)
- Use `requestAnimationFrame` for all animations — never `setInterval`
- Cache expensive draws to an offscreen canvas
- Clear only the region you need, not the whole canvas

### Pixel-Perfect Rendering
Account for device pixel ratio (retina/HiDPI displays):

```js
function setupCanvas(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  return ctx;
}
```

### Accessibility
Canvas has no native accessibility. Always add:
- `role="img"` and `aria-label` describing the content
- A fallback `<p>` inside `<canvas>` for non-JS contexts
- For interactive canvases, manage keyboard focus and ARIA live regions

---

## Common Canvas Patterns

### 1. Animated Hero Graphic

Particle systems, flowing gradients, or morphing shapes for landing page backgrounds:

```js
const canvas = document.getElementById('hero-canvas');
const ctx = setupCanvas(canvas);
let particles = [];

function Particle(x, y) {
  this.x = x;
  this.y = y;
  this.vx = (Math.random() - 0.5) * 1.5;
  this.vy = (Math.random() - 0.5) * 1.5;
  this.alpha = Math.random();
  this.radius = Math.random() * 3 + 1;
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.vx;
    p.y += p.vy;
    p.alpha -= 0.005;
    if (p.alpha <= 0) Object.assign(p, new Particle(Math.random() * canvas.width, Math.random() * canvas.height));
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(99, 102, 241, ${p.alpha})`;
    ctx.fill();
  });
  requestAnimationFrame(animate);
}

for (let i = 0; i < 80; i++) {
  particles.push(new Particle(Math.random() * canvas.width, Math.random() * canvas.height));
}
animate();
```

### 2. Marketing Chart (Bar / Line / Donut)

Clean, animated charts without heavy libraries:

```js
// Animated bar chart
function drawBarChart(ctx, data, options) {
  const { width, height, padding = 40, color = '#6366f1', duration = 800 } = options;
  const maxVal = Math.max(...data.map(d => d.value));
  const barWidth = (width - padding * 2) / data.length - 8;
  const startTime = performance.now();

  function render(now) {
    const progress = Math.min((now - startTime) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3); // cubic ease-out

    ctx.clearRect(0, 0, width, height);

    data.forEach((d, i) => {
      const barHeight = ((d.value / maxVal) * (height - padding * 2)) * ease;
      const x = padding + i * (barWidth + 8);
      const y = height - padding - barHeight;

      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.roundRect(x, y, barWidth, barHeight, 4);
      ctx.fill();

      ctx.fillStyle = '#374151';
      ctx.font = '12px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText(d.label, x + barWidth / 2, height - padding + 16);
    });

    if (progress < 1) requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}
```

### 3. Progress / Gauge Visual

Effective for pricing pages or feature showcases:

```js
function drawDonut(ctx, percent, options) {
  const { cx, cy, radius = 60, stroke = 12, color = '#6366f1', bg = '#e5e7eb' } = options;
  const start = -Math.PI / 2;
  const end = start + (Math.PI * 2 * percent);

  // Background ring
  ctx.beginPath();
  ctx.arc(cx, cy, radius, 0, Math.PI * 2);
  ctx.strokeStyle = bg;
  ctx.lineWidth = stroke;
  ctx.stroke();

  // Value arc
  ctx.beginPath();
  ctx.arc(cx, cy, radius, start, end);
  ctx.strokeStyle = color;
  ctx.lineWidth = stroke;
  ctx.lineCap = 'round';
  ctx.stroke();

  // Label
  ctx.fillStyle = '#111827';
  ctx.font = `bold ${radius * 0.5}px system-ui`;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(`${Math.round(percent * 100)}%`, cx, cy);
}
```

### 4. Interactive Canvas (Mouse Tracking)

Draw effects that follow the cursor — effective for engagement on hero sections:

```js
canvas.addEventListener('mousemove', e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  // spawn particle or ripple at (x, y)
  spawnRipple(ctx, x, y);
});
```

---

## Responsive Canvas

Canvas does not resize automatically. Use a ResizeObserver:

```js
const ro = new ResizeObserver(() => {
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.style.width = rect.width + 'px';
  canvas.style.height = rect.height + 'px';
  // Re-run setupCanvas and redraw
  setupCanvas(canvas);
  draw();
});
ro.observe(canvas.parentElement);
```

---

## Canvas vs. SVG Decision Guide

| Use Canvas | Use SVG |
|---|---|
| Many elements (1000+) | Few, scalable elements |
| Pixel manipulation | Text-heavy graphics |
| Real-time animation | Static or rarely animated |
| Game / simulation | Accessible, indexable content |
| Image processing | Print / high-res export |

---

## Quality Checklist

Before shipping a canvas visual:

- [ ] HiDPI / retina handled (device pixel ratio scaling)
- [ ] `requestAnimationFrame` used (no `setInterval`)
- [ ] Animation stops when element is off-screen (`IntersectionObserver`)
- [ ] Canvas has `aria-label` describing the visual
- [ ] Fallback content inside `<canvas>` tag
- [ ] Performance tested on low-end mobile
- [ ] Respects `prefers-reduced-motion` media query
- [ ] Canvas cleaned up on component unmount (cancel animation frame)

### Reduced Motion Support

```js
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) {
  requestAnimationFrame(animate);
} else {
  drawStatic(); // draw final frame only
}
```

---

## Deliverables

For each canvas design task, provide:

1. **HTML** — `<canvas>` element with accessibility attributes
2. **JavaScript** — setup, draw, and (if animated) animation loop functions
3. **CSS** — sizing, positioning, responsive rules
4. **Usage notes** — where to place in the page, how to customize colors/data
