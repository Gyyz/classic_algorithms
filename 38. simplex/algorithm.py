def simplex_maximize(c, A, b):
    """
    Solve max c^T x subject to A x <= b, x >= 0 via simplex tableau (small problems).
    Returns (opt_value, x) or raises ValueError for unbounded/infeasible in simple checks.
    """
    # Build initial tableau with slack variables: [A | I | b] and objective [-c | 0 | 0]
    m = len(A)
    n = len(A[0])
    # tableau rows: m constraints + 1 objective
    tableau = []
    for i in range(m):
        row = A[i][:] + [0]*m + [b[i]]
        row[n + i] = 1
        tableau.append(row)
    obj = [-ci for ci in c] + [0]*m + [0]
    tableau.append(obj)

    basis = list(range(n, n + m))

    while True:
        # Entering variable: most negative coefficient in objective
        last = tableau[-1]
        entering = max(range(n + m), key=lambda j: -last[j])
        if last[entering] >= 0:
            break  # optimal
        # Leaving variable: minimum ratio test
        ratios = []
        for i in range(m):
            col = tableau[i][entering]
            if col > 1e-12:
                ratios.append((tableau[i][-1] / col, i))
        if not ratios:
            raise ValueError("Unbounded LP (no positive entries in entering column)")
        _, leaving_row = min(ratios)
        pivot = tableau[leaving_row][entering]
        # Normalize pivot row
        tableau[leaving_row] = [x / pivot for x in tableau[leaving_row]]
        # Eliminate column
        for i in range(m + 1):
            if i == leaving_row:
                continue
            factor = tableau[i][entering]
            tableau[i] = [tableau[i][k] - factor * tableau[leaving_row][k] for k in range(n + m + 1)]
        basis[leaving_row] = entering

    # Extract solution
    x = [0.0] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = tableau[i][-1]
    opt = tableau[-1][-1]
    return opt, x

def simplex(c, A, b):
    """Wrapper to match README usage; maximizes c^T x subject to A x <= b."""
    return simplex_maximize(c, A, b)

if __name__ == "__main__":
    # Maximize 3x + 2y subject to: x + y <= 4, x <= 2, y <= 3, x,y >= 0
    c = [3, 2]
    A = [
        [1, 1],
        [1, 0],
        [0, 1]
    ]
    b = [4, 2, 3]
    opt, x = simplex_maximize(c, A, b)
    print("Optimal value:", opt)
    print("Solution x:", x)