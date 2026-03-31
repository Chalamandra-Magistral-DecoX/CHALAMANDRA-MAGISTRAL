## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Preventing Layout Thrashing in Scroll Events]
**Learning:** Using `getBoundingClientRect()` inside synchronous scroll event listeners causes severe layout thrashing and performance bottlenecks.
**Action:** Decouple scroll-based animations and layout queries. Use `IntersectionObserver` for element visibility checks and `requestAnimationFrame` with `{ passive: true }` for continuous scroll-based updates like progress bars.
