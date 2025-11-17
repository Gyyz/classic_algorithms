def gradient_descent(f, df, x0, lr=0.1, iters=1000, tol=1e-8):
    x = x0
    for _ in range(iters):
        grad = df(x)
        x_new = x - lr*grad
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

if __name__ == "__main__":
    f = lambda x: (x-3)**2 + 1
    df = lambda x: 2*(x-3)
    xmin = gradient_descent(f, df, x0=10.0, lr=0.2)
    print("Minimum near x=3 ->", xmin, "f(x)=", f(xmin))