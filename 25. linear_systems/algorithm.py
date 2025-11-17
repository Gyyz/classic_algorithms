def gauss_jordan_solve(A, b):
    """
    Solve A x = b via Gauss–Jordan elimination. A is n×n, b is length n.
    Returns solution vector x.
    """
    n = len(A)
    # build augmented matrix
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        # find pivot
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < 1e-12:
            raise ValueError("Singular matrix")
        M[col], M[pivot_row] = M[pivot_row], M[col]
        # normalize pivot row
        pivot = M[col][col]
        M[col] = [x / pivot for x in M[col]]
        # eliminate other rows
        for r in range(n):
            if r == col:
                continue
            factor = M[r][col]
            M[r] = [M[r][c] - factor * M[col][c] for c in range(n + 1)]
    return [M[i][-1] for i in range(n)]

def gauss_jordan(A, b):
    """Alias to match README usage; solves A x = b via Gauss-Jordan."""
    return gauss_jordan_solve(A, b)

if __name__ == "__main__":
    A = [[2, 1], [5, 7]]
    b = [11, 13]
    x = gauss_jordan_solve(A, b)
    print("Solution:", x)