## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Heavy 3D Scene Geometry Updates]
**Learning:** Three.js loops can run lightweight transformations (rotation, camera movement) efficiently. But continuously calculating and updating large position arrays (like `needsUpdate = true` on buffer geometries) causes heavy CPU/GPU overhead. When an animation settles, these expensive calculations should be paused.
**Action:** Introduce a `settledFrames` counter in animation loops. Once a transition target is reached and the counter exceeds a threshold, skip the expensive array recalculations and buffer updates, keeping only the necessary lightweight operations running.
