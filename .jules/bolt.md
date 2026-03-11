## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Preventing Layout Thrashing in Scroll Handlers]
**Learning:** Using `getBoundingClientRect()` inside a `scroll` event listener causes synchronous layout calculations (layout thrashing) that block the main thread and destroy scrolling performance.
**Action:** Replace scroll-based element coordinate checks with `IntersectionObserver` whenever possible. For other scroll-dependent updates (like progress bars), always wrap the DOM update in `requestAnimationFrame` and add the `{ passive: true }` flag to the event listener to avoid blocking the main thread.
