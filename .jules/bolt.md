## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2025-02-18 - [Optimizing Settled Three.js Animations]
**Learning:** Constantly updating thousands of particle positions and flagging `needsUpdate = true` in an animation loop drastically hurts performance (blocking main thread, dropping FPS), even when the transition factor has settled.
**Action:** Track when continuous animation transitions finish (e.g., target reached). Use a `settledFrames` counter to bypass expensive geometry updates, allowing base visual effects (like rotation) to continue while saving significant processing power.
