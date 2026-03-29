## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-24 - [Skipping Stable Geometry Updates]
**Learning:** In Three.js animations involving particle interpolation, expensive geometry updates can be skipped once the interpolation target is reached (stable state), significantly reducing CPU usage while maintaining rendering (rotation/camera).
**Action:** Implement a stability counter to detect when an animation has settled and bypass geometry calculations, only updating render-critical properties like rotation.
