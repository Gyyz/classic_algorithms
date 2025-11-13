def poly_hash(s: str, base=911382323, mod=972663749):
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h

if __name__ == "__main__":
    print(poly_hash("hello"))
    print(poly_hash("world"))