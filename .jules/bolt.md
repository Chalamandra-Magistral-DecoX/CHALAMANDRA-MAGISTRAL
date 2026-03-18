## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Skipping Idle 3D Buffer Geometry Updates]
**Learning:** Continuous particle animation loops consume significant CPU/GPU resources needlessly executing massive `for` loops even when visual transitions finish. Identifying "idle states" in these loops provides a significant optimization point.
**Action:** When working with Three.js loops where values interpolate toward a target, introduce a `settledFrames` counter to pause heavy array computations and buffer `needsUpdate` flags once the values converge, while retaining lighter animation routines like camera updates and rotations.
