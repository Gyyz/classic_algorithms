# Gradient Descent

Gradient descent iteratively updates parameters in the direction of the negative gradient to minimize a function.

This demo minimizes `f(x) = (x-3)^2 + 1`.

Key ideas:

- Step size (learning rate) controls progress.
- Stop when updates are small or max iterations reached.

## Complex Polynomial Demo

We also include a more complex example:

`f(x) = (x+2)^5 + (x-1)^3 + (x+5)^2`

Its derivative is:

`f'(x) = 5(x+2)^4 + 3(x-1)^2 + 2(x+5)`

Important: this function is unbounded below (the `x^5` term dominates), so gradient descent will keep pushing `x` toward negative infinity. The demo uses a tiny learning rate and limited iterations to illustrate behavior without numeric overflow:

```python
from algorithm import gradient_descent

f2 = lambda x: (x+2)**5 + (x-1)**3 + (x+5)**2
df2 = lambda x: 5*(x+2)**4 + 3*(x-1)**2 + 2*(x+5)

xmin2 = gradient_descent(f2, df2, x0=0.0, lr=1e-6, iters=20000)
print("Complex polynomial demo -> x=", xmin2, "f(x)=", f2(xmin2))
```

If you want a finite minimizer, choose a function that is bounded below (e.g., add a strong quadratic term or constrain the domain).

Overview

- First-order optimization; updates `x_{t+1} = x_t - η \nabla f(x_t)`.
- Converges for convex, smooth functions with suitable step size.

Variants

- Stochastic/mini-batch GD, momentum, Nesterov, Adam.

Step Size and Convergence

- Choose `η` small enough; for quadratic forms, set by Lipschitz constant.
- Use line search or schedules (e.g., decay) to improve stability.

Notes

- For non-convex functions, GD may converge to local minima or diverge.