## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Scroll Animations and Avoid Layout Thrashing]
**Learning:** Using `getBoundingClientRect()` synchronously inside a `scroll` event listener causes severe layout thrashing (forced synchronous layout), significantly dropping framerate on long scrolling pages. The main thread gets blocked continuously computing layout on every pixel scrolled.
**Action:** Decouple continuous layout calculations using `IntersectionObserver` for visibility checks and `requestAnimationFrame` for decoupled scroll updates (like progress bars) along with `{ passive: true }` event listeners.
