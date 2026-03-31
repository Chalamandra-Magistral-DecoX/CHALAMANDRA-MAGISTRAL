## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Throttling High-Frequency Scroll Events]
**Learning:** Synchronous DOM reads (like `getBoundingClientRect`) and writes inside a `scroll` event listener can cause layout thrashing and significant main thread blocking, especially on high-refresh-rate displays.
**Action:** Consolidate scroll listeners and throttle them using `requestAnimationFrame` (ticking pattern). Use `{ passive: true }` to allow the compositor thread to scroll without waiting for JS.
