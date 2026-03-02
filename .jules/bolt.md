## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Scroll Performance with requestAnimationFrame and IntersectionObserver]
**Learning:** Synchronous scroll event listeners for visual updates (like progress bars and reveal animations) cause severe layout thrashing by forcing synchronous reflows on the main thread.
**Action:** Always use `IntersectionObserver` for element visibility checks instead of scroll events. For scroll-bound continuous updates (like progress bars), debounce the updates using `requestAnimationFrame` and ensure the event listener is `{ passive: true }`.
