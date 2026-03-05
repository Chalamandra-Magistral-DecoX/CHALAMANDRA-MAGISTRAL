## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Scroll Events and Layout Thrashing]
**Learning:** Unthrottled `scroll` event listeners that call `getBoundingClientRect()` on multiple DOM elements create a bottleneck by triggering layout recalculations (thrashing) on every frame. Replacing these with `IntersectionObserver` and wrapping passive scroll updates in `requestAnimationFrame` significantly reduces main thread blocking.
**Action:** Always use `IntersectionObserver` instead of `scroll` listeners for element visibility checks. When a `scroll` event must be used (e.g., progress bar), attach the listener with `{ passive: true }` and wrap the DOM manipulation inside `requestAnimationFrame`.
