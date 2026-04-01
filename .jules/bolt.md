## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-04-01 - [Synchronous Scroll Events and getBoundingClientRect]
**Learning:** Attaching synchronous `getBoundingClientRect()` calls to scroll event listeners triggers severe layout thrashing, as the browser is forced to continuously recalculate styles and layout on every scroll tick.
**Action:** Decouple DOM measurements from the scroll event using `IntersectionObserver` for visibility checks, and use `requestAnimationFrame` with `{ passive: true }` for necessary high-frequency scroll updates like progress bars to avoid blocking the main thread.
