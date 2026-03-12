## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Scroll Animations and Progress Bars]
**Learning:** Using `getBoundingClientRect()` inside a synchronous `scroll` event listener causes layout thrashing and severe main-thread blocking on scrolling. Replacing it with `IntersectionObserver` eliminates this overhead. Additionally, simple scroll updates like progress bars should be debounced with `requestAnimationFrame` and marked with `{ passive: true }` to avoid blocking scroll paints.
**Action:** Use `IntersectionObserver` for element reveal animations and `requestAnimationFrame` for continuous scroll-bound visual updates. Always set `{ passive: true }` on scroll event listeners when `preventDefault()` is not needed.
