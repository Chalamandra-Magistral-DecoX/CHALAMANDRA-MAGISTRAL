## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Skipping BufferGeometry Updates on Settled Animations]
**Learning:** Three.js loops often update array attributes and set `needsUpdate = true` every frame, even after transitions have completed. Continuously updating up to 3000 particle positions unnecessarily burns CPU/GPU.
**Action:** Always track animation state (e.g., using `settledFrames`) and skip expensive array iterations and geometry `needsUpdate` flags when visual changes drop below a perceptible threshold.
