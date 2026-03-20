## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-03-20 - [Optimizing Scroll Performance with IntersectionObserver and requestAnimationFrame]
**Learning:** The synchronous `scroll` event listener looping through `.querySelectorAll('.reveal')` with `getBoundingClientRect()` to trigger animations forces synchronous layout calculation and layout thrashing. This is a common performance bottleneck on Single Page Applications (SPAs) with heavily visual/animated elements.
**Action:** Replace unthrottled manual checks that calculate geometric layouts during scroll with `IntersectionObserver`. Debounce visual styling updates driven by scrolling using `window.requestAnimationFrame()`.
