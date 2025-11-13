def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        dfx = df(x)
        if dfx == 0:
            break
        x_new = x - f(x) / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    f = lambda x: x*x - 2
    df = lambda x: 2*x
    root = newton(f, df, x0=1.0)
    print("Root of x^2-2:", root)