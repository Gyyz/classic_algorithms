import cmath

def fft(x):
    n = len(x)
    if n == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    res = [0]*n
    for k in range(n//2):
        tw = cmath.exp(-2j*cmath.pi*k/n) * odd[k]
        res[k] = even[k] + tw
        res[k+n//2] = even[k] - tw
    return res

def ifft(X):
    n = len(X)
    conj = [x.conjugate() for x in X]
    inv = fft(conj)
    return [x.conjugate()/n for x in inv]

if __name__ == "__main__":
    x = [1,2,3,4,0,0,0,0]
    X = fft(list(map(complex, x)))
    xr = ifft(X)
    print("FFT:", X)
    print("IFFT:", xr)