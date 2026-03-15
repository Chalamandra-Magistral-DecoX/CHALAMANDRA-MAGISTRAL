## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2025-02-12 - [Optimizing Three.js Geometry Updates for Settled Animations]
**Learning:** Recomputing large arrays of point positions and lines on every single frame, even after an animation has visually settled to its final target, causes unnecessary CPU overhead. When thousands of particles only need to rotate, the intensive `for` loop updating individual X, Y, Z coordinates per point shouldn't run.
**Action:** Implemented a `settledFrames` counter to track when `Math.abs(target - transitionFactor) < 0.001`. Once settled for enough frames (e.g., 60 frames), bypass the particle geometry updates and only apply the rotation to the overall container/objects, significantly saving CPU cycles and battery on mobile.
