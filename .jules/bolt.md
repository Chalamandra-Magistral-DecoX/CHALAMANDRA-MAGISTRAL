## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-03-19 - [Optimizing Settled Particle Systems in Three.js]
**Learning:** Continuously updating particle geometry and marking `needsUpdate = true` when a particle system is no longer moving significantly wastes CPU and GPU overhead, especially when maintaining a constant rotation. Three.js position array updates scale O(N) relative to particle count and involve expensive buffer uploads.
**Action:** Add a settled state counter to animation loops managing transitions. Skip geometry buffer calculations and updates when settled, while preserving global rotation to maintain visual life without the overhead.
