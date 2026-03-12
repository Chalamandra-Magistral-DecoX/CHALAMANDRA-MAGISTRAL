## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Skipping Static Geometry Updates in Three.js]
**Learning:** Endlessly recalculating static geometry positions in Three.js animation loops consumes significant CPU/GPU resources, even when the visual state has reached its target.
**Action:** Detect when custom transition animations have settled and skip the expensive geometry update loops, while continuing to render the scene and perform cheap operations like rotation.
