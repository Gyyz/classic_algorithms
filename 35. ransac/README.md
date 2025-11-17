# RANSAC (Random Sample Consensus)

Algorithm to robustly estimate model parameters from data with outliers by iteratively fitting to random minimal samples and validating with inlier counts.

Key ideas:

- Random minimal sample selection.
- Consensus via inlier thresholding.
- Model refinement on consensus set.

Overview

- Robust estimation under outliers; fits models using random minimal samples and validates by inlier thresholds.
- Common for line/plane fitting, homography/essential matrices in vision.

Algorithm Steps

1. Repeat for `N` iterations:
   - Randomly sample minimal set; fit provisional model.
   - Count inliers within tolerance; track best model and inliers.
2. Refit model using the consensus inliers.

Complexity

- Depends on required confidence and inlier ratio; iterations `N` derived from success probability.

Pros / Cons

- Pros: handles heavy outlier contamination.
- Cons: needs tolerance and iteration tuning; can miss optimal model.

Usage Example

```python
from algorithm import ransac_line
model, inliers = ransac_line(points, tol=0.01, max_iters=1000)
```