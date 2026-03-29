## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Scroll Events and Layout Thrashing]
**Learning:** Using `getBoundingClientRect` inside a synchronous `scroll` event listener causes layout thrashing and severely degrades scrolling performance.
**Action:** Always replace synchronous `scroll` listeners used for element reveals with `IntersectionObserver`. For continuous updates like a scroll progress bar, debounce the scroll event with `requestAnimationFrame` and `isScrolling` flags, and mark the listener with `{ passive: true }`.
