import random

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m

def is_probable_prime(n, k=8):
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    # Miller-Rabin
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=256):
    while True:
        candidate = random.getrandbits(bits) | 1 | (1 << (bits - 1))
        if is_probable_prime(candidate):
            return candidate

def generate_keypair(bits=256):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if phi % e == 0:
        # fallback
        e = 3
    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt_bytes(data: bytes, pubkey):
    e, n = pubkey
    m = int.from_bytes(data, 'big')
    c = pow(m, e, n)
    return c

def decrypt_bytes(cipher_int: int, privkey):
    d, n = privkey
    m = pow(cipher_int, d, n)
    # decode back to bytes with length guess
    blen = (m.bit_length() + 7) // 8
    return m.to_bytes(blen, 'big')

if __name__ == "__main__":
    pub, priv = generate_keypair(bits=128)
    msg = b"hello rsa"
    c = encrypt_bytes(msg, pub)
    dec = decrypt_bytes(c, priv)
    print("Cipher:", c)
    print("Decrypted:", dec)