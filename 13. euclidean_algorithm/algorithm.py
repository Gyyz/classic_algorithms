def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(gcd(48, 18))  # 6