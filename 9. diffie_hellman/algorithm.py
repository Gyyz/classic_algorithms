def modexp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def diffie_hellman_demo(p, g, a, b):
    """Return public values and shared secret for a simple DH exchange.

    Parameters:
    - p: prime modulus
    - g: generator modulo p
    - a: Alice's private exponent
    - b: Bob's private exponent

    Returns: (A, B, s) where A=g^a mod p, B=g^b mod p, s=shared secret.
    """
    A = modexp(g, a, p)
    B = modexp(g, b, p)
    s_alice = modexp(B, a, p)
    s_bob = modexp(A, b, p)
    assert s_alice == s_bob
    return A, B, s_alice

if __name__ == "__main__":
    p = 23  # small prime for demo
    g = 5   # primitive root mod 23
    a = 6   # Alice's secret
    b = 15  # Bob's secret
    A, B, s = diffie_hellman_demo(p, g, a, b)
    print("Public A:", A, "Public B:", B)
    print("Shared secret:", s)