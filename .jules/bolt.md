## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-22 - [Refactoring Scroll Layout Thrashing]
**Learning:** Synchronous layout calculations like `getBoundingClientRect()` inside high-frequency scroll event listeners cause main thread blocking and layout thrashing. Relying on `IntersectionObserver` for element visibility logic, and throttling visual updates (like progress bars) with `requestAnimationFrame` and passive listeners (`{ passive: true }`), significantly improves scroll performance.
**Action:** Replace direct scroll layout querying logic with `IntersectionObserver` and throttle visual scroll updates with `requestAnimationFrame`.
