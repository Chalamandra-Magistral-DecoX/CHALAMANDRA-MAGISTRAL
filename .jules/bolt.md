## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-06-15 - [Preventing Layout Thrashing in Scroll Event Listeners]
**Learning:** Using `getBoundingClientRect()` inside a synchronous `window.addEventListener('scroll')` causes severe layout thrashing and blocks the main thread, leading to jittery scrolling on lower-end devices. This is a common anti-pattern in vanilla JS reveal animations.
**Action:** Avoid synchronous DOM measurements in scroll events. Use `IntersectionObserver` for element visibility checks and decouple UI updates (like scroll progress bars) using `requestAnimationFrame` inside passive event listeners (`{ passive: true }`).
