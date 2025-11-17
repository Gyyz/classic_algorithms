# Structure Tensor (Strukturtensor)

Computes per-pixel measures indicating whether a pixel lies in a homogeneous region, along an edge, or at a corner/vertex, based on gradient second-moment matrices.

Key ideas:

- Local gradients (Ix, Iy) and their products.
- Eigenvalues of the 2×2 structure tensor indicate edge/corner strength.

Overview

- Structure tensor `J = [[Ix^2, Ix Iy],[Ix Iy, Iy^2]]` summarizes local gradient distribution.
- Eigenvalues: large anisotropy indicates edges; both large indicates corners.

Algorithm Steps

1. Compute gradients `(Ix, Iy)`; optionally smooth.
2. Form second-moment matrix via local averaging.
3. Analyze eigenvalues or Harris/shi-tomasi measures.

Usage Example

```python
from algorithm import structure_tensor
J = structure_tensor(image, window=3)
```