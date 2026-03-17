## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Heavy 3D Geometries with Settled Frames]
**Learning:** In Three.js, constantly updating `geometry.attributes.position.array` and setting `needsUpdate = true` in an animation loop is very expensive. When the particle transition has reached its target (e.g., transition difference < 0.001), these updates are redundant but still consume resources.
**Action:** Track a `settledFrames` counter and skip the inner geometry modification loops and `needsUpdate` flags once the animation has settled for a threshold number of frames, continuing to render only global scene/camera changes.
