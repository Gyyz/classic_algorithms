# Structure Tensor (Strukturtensor)

Computes per-pixel measures indicating whether a pixel lies in a homogeneous region, along an edge, or at a corner/vertex, based on gradient second-moment matrices.

Key ideas:

- Local gradients (Ix, Iy) and their products.
- Eigenvalues of the 2×2 structure tensor indicate edge/corner strength.