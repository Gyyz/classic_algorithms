import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fft.algorithm import fft, ifft


def run():
    x = [1, 2, 3, 4, 0, 0, 0, 0]
    X = fft(list(map(complex, x)))
    xr = ifft(X)
    for a, b in zip(x, xr):
        assert abs(a - b.real) < 1e-9
    print("test_fft: OK")


if __name__ == "__main__":
    run()