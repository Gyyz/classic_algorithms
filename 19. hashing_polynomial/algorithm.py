def poly_hash(s: str, base=911382323, mod=972663749):
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h

def build_prefix(s: str, base=911382323, mod=972663749):
    """
    Build prefix hashes and base powers for fast substring hashing.
    Returns (prefix, power) where:
      - prefix[i] = hash of s[:i]
      - power[i] = base^i mod mod
    """
    n = len(s)
    prefix = [0] * (n + 1)
    power = [1] * (n + 1)
    for i, ch in enumerate(s, start=1):
        prefix[i] = (prefix[i - 1] * base + ord(ch)) % mod
        power[i] = (power[i - 1] * base) % mod
    return prefix, power

if __name__ == "__main__":
    print(poly_hash("hello"))
    print(poly_hash("world"))