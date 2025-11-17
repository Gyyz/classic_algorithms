import math

def dot(u, v):
    return sum(ui*vi for ui, vi in zip(u, v))

def proj(u, v):
    # project u onto v
    denom = dot(v, v)
    if denom == 0:
        return [0]*len(u)
    scale = dot(u, v)/denom
    return [scale*vi for vi in v]

def gram_schmidt(B):
    U = []
    mu = [[0]*len(B) for _ in range(len(B))]
    for i, b in enumerate(B):
        u = b[:]
        for j in range(i):
            mu[i][j] = dot(b, U[j]) / dot(U[j], U[j])
            u = [ui - mu[i][j]*uj for ui, uj in zip(u, U[j])]
        U.append(u)
    return U, mu

def lll_reduce(B, delta=0.75):
    # B: list of integer vectors
    n = len(B)
    k = 1
    U, mu = gram_schmidt(B)
    while k < n:
        # size reduction
        for j in range(k-1, -1, -1):
            if abs(mu[k][j]) > 0.5:
                r = int(round(mu[k][j]))
                B[k] = [bk - r*bj for bk, bj in zip(B[k], B[j])]
                U, mu = gram_schmidt(B)
        # Lovász condition
        uk_norm2 = dot(U[k], U[k])
        ukm_norm2 = dot(U[k-1], U[k-1])
        if uk_norm2 >= (delta - mu[k][k-1]**2) * ukm_norm2:
            k += 1
        else:
            # swap
            B[k], B[k-1] = B[k-1], B[k]
            U, mu = gram_schmidt(B)
            k = max(k-1, 1)
    return B

if __name__ == "__main__":
    B = [[1,1,1],[1,0,2],[0,2,1]]
    print("Original basis:", B)
    R = lll_reduce(B)
    print("Reduced basis:", R)