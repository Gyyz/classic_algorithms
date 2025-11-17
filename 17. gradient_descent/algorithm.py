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

    # More complex demo: f(x) = (x+2)^5 + (x-1)^3 + (x+5)^2
    # Note: This function is unbounded below due to the x^5 term,
    # so gradient descent will keep pushing x toward -infinity.
    # We use a tiny learning rate and limited iterations to illustrate
    # behavior without causing numeric overflow.
    f2 = lambda x: (x+2)**5 + (x-1)**3 + (x+5)**2
    df2 = lambda x: 5*(x+2)**4 + 3*(x-1)**2 + 2*(x+5)
    x0 = 0.0
    xmin2 = gradient_descent(f2, df2, x0=x0, lr=1e-6, iters=20000)
    print("Complex polynomial demo -> x=", xmin2, "f(x)=", f2(xmin2))