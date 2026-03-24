## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-03-24 - [Skipping O(N) Array Updates for Settled Geometries]
**Learning:** Continuously updating large array buffers (like particle positions) and setting `needsUpdate = true` inside a Three.js animation loop, even when the values have barely changed, incurs significant CPU overhead. Tracking when interpolations have "settled" allows bypassing O(N) array calculations and GPU uploads, massively improving frame times, while cheap global transformations (like rotation and camera movement) keep the scene alive.
**Action:** When animating buffer geometries between states, track settling (e.g., `Math.abs(target - value) < threshold`) and skip geometry recalculations and `needsUpdate` flags when settled.
