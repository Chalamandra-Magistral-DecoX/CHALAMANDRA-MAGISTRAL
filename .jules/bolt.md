## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-23 - [Optimizing Three.js Loops with Idle State Detection]
**Learning:** Continuous 3D particle animations that perform O(N) geometry updates during transitions can waste massive CPU/GPU resources if the recalculation continues after the transition is visually complete.
**Action:** Always track an idle state (e.g., `settledFrames`) in `requestAnimationFrame` loops. When the target state is reached and stabilized, skip expensive geometry updates and only render necessary lightweight updates (like rotation or camera movement).
