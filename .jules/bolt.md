## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2025-01-01 - [Optimizing Scroll Performance with IntersectionObserver and rAF]
**Learning:** Using `getBoundingClientRect` inside a synchronous scroll event listener causes severe layout thrashing because it forces the browser to recalculate layout on every scroll frame.
**Action:** Always replace synchronous scroll listeners that check element visibility with `IntersectionObserver`. For other scroll-dependent updates (like progress bars), decouple the update logic using `requestAnimationFrame` and `passive: true` to prevent blocking the main thread.
