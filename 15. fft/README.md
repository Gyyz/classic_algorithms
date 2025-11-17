# Fast Fourier Transform (FFT)

Cooley–Tukey FFT computes the discrete Fourier transform efficiently by recursively splitting even and odd indices and combining with twiddle factors.

Key ideas:

- Divide-and-conquer on length `n` (power of 2).
- Use complex roots of unity.
- Inverse via conjugation and scaling.