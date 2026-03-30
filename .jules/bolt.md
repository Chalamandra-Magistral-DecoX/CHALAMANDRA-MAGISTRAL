## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.
## 2025-02-12 - [Refactoring Scroll Handlers for Performance]
**Learning:** Using `getBoundingClientRect()` inside a synchronous scroll event listener causes severe layout thrashing and blocks the main thread.
**Action:** Decouple scroll events using `requestAnimationFrame` and replace visibility checks with `IntersectionObserver` configured with `{ passive: true }` to ensure smooth scroll performance and prevent layout thrashing.
