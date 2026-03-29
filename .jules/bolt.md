## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Scroll Handlers for Performance]
**Learning:** Continuous synchronous execution inside scroll event listeners (`window.addEventListener('scroll')`) causes main thread blocking and jank, especially when performing DOM operations.
**Action:** Throttle high-frequency events using `requestAnimationFrame` with `{ passive: true }` flags. Replace scroll-based visibility checks entirely with `IntersectionObserver` to offload layout calculations to the browser engine.
