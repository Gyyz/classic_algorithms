import math

def central_diff(f, x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

if __name__ == "__main__":
    x = 1.234
    approx = central_diff(math.sin, x)
    print("d/dx sin(x) at x=", x, "≈", approx)
    print("true cos(x)=", math.cos(x))