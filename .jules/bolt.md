## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-03-22 - [Optimizing Heavy 3D Loops by Skipping Settled Geometry Updates]
**Learning:** Even when `IntersectionObserver` is used to pause Three.js animations off-screen, a continuous `requestAnimationFrame` loop on-screen can consume excessive CPU if it unconditionally recalculates geometry every frame. When transitions settle, recalculating `pos` and `lp` attributes for thousands of particles is wasteful.
**Action:** Implement a `settledFrames` counter to track when a transition target is reached (`Math.abs(target - transitionFactor) < 0.001`). Once settled for a few frames, skip the expensive O(N) array loops and only run lightweight updates (like ambient rotation or camera sway).
