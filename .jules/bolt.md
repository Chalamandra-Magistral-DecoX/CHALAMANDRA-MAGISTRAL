## 2024-05-22 - [Optimizing Heavy 3D Scenes with IntersectionObserver]
**Learning:** Three.js animation loops running constantly consume significant CPU/GPU resources even when off-screen. Pausing the loop using `IntersectionObserver` is a high-impact optimization for single-page scroll experiences.
**Action:** Always wrap `requestAnimationFrame` loops in an `IntersectionObserver` visibility check for non-critical visual elements.

## 2024-05-24 - [Idle-state Detection in 3D Transition Animations]
**Learning:** Continuously recalculating particle geometry positions for microscopic changes (as they asymptotically approach a target) creates an unnecessary CPU bottleneck `O(n)`. Once visually settled, recalculating the `O(n)` geometry loop every frame is wasted processing power.
**Action:** Implement an idle-state detection mechanism (e.g., `settledFrames`) in animation loops to skip expensive geometry updates when the visual transition is complete, while still allowing lightweight rendering operations like overall camera/scene rotation to continue smoothly.
