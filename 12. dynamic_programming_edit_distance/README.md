# Dynamic Programming: Edit Distance

Edit distance (Levenshtein) computes the minimum number of edits to transform one string into another using DP.

Key ideas:

- DP table of size `m×n` with insert/delete/replace transitions.
- Optimal substructure and overlapping subproblems.

Overview

- Levenshtein distance allows insertions, deletions, and substitutions with unit cost.
- Variants: Damerau–Levenshtein (transpositions), weighted costs.

Algorithm Steps

1. Initialize DP table `dp[i][0]=i`, `dp[0][j]=j`.
2. Transition: `dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (s[i]!=t[j]))`.
3. Answer: `dp[m][n]`.

Complexity

- Time/space `O(mn)`; can reduce space to `O(min(m,n))` keeping two rows.

Usage Example

```python
from algorithm import edit_distance
print(edit_distance("kitten", "sitting"))  # 3
```