## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.
