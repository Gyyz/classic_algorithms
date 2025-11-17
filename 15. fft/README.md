# Fast Fourier Transform (FFT)

Cooley–Tukey FFT computes the discrete Fourier transform efficiently by recursively splitting even and odd indices and combining with twiddle factors.

Key ideas:

- Divide-and-conquer on length `n` (power of 2).
- Use complex roots of unity.
- Inverse via conjugation and scaling.

Overview

- Computes DFT in `O(n log n)` vs naive `O(n^2)`.
- Used in signal processing, convolution (via FFT), spectral analysis.

Algorithm Steps (Cooley–Tukey radix-2)

1. Recursively compute DFT of even and odd-indexed elements.
2. Combine using twiddle factors `W_n^k = e^{-2πik/n}`.

Complexity

- Time `O(n log n)`; memory depends on implementation (in-place vs out-of-place).

Usage Example

```python
from algorithm import fft, ifft
X = fft(signal)
x = ifft(X)
```

Notes

- Length not power of 2: use mixed-radix or pad.
- Numerical errors accumulate; consider double precision.