## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Preventing Layout Thrashing in Scroll Listeners]
**Learning:** Synchronous `window.addEventListener('scroll')` that reads DOM properties (like `getBoundingClientRect().top`) and writes DOM changes (like `classList.add`) causes significant layout thrashing and blocks the main thread, especially when combined with a continuous 3D WebGL loop.
**Action:** Always use `IntersectionObserver` for scroll-based element reveals and `requestAnimationFrame` with `{ passive: true }` for scroll progress bars to prevent main thread blocking and layout thrashing.
