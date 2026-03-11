## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2026-03-11 - [Bypassing Unnecessary Geometry Updates in Settled Three.js Animations]
**Learning:** Three.js geometry updates that continually mutate position buffers inside a `requestAnimationFrame` loop consume massive CPU resources and cause needless GPU uploads (e.g., iterating through thousands of vertices for minor interpolation math), even when the animation's target transition factor has practically been reached. When an animation relies primarily on global rotation but no longer requires internal vertex positional changes, these buffer updates become a major hidden bottleneck.
**Action:** Always track the delta of the transition logic. Once the delta falls below a negligible threshold (e.g., `Math.abs(target - transitionFactor) < 0.001`) for a certain number of frames, bypass the internal geometry `for` loop and stop setting `needsUpdate = true`. Let the global transformations (e.g., `particles.rotation.y`) handle continuous motion.
