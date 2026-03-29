## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-24 - [Scroll Event Layout Thrashing]
**Learning:** Using `getBoundingClientRect()` inside a synchronous scroll listener causes severe layout thrashing by forcing the browser to synchronously recalculate layout.
**Action:** Use `IntersectionObserver` to trigger reveal animations or visibility checks, and decouple continuous scroll logic (like a progress bar) using `requestAnimationFrame` with `{ passive: true }` scroll event listeners to prevent blocking the main thread.
