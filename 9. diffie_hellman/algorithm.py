def modexp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

if __name__ == "__main__":
    p = 23  # small prime for demo
    g = 5   # primitive root mod 23
    a = 6   # Alice's secret
    b = 15  # Bob's secret
    A = modexp(g, a, p)
    B = modexp(g, b, p)
    s_alice = modexp(B, a, p)
    s_bob = modexp(A, b, p)
    print("Public A:", A, "Public B:", B)
    print("Shared secrets equal:", s_alice == s_bob, "=", s_alice)