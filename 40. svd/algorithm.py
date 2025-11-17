try:
    import numpy as np
except Exception:
    np = None

def svd(A):
    """Compute SVD of matrix A using NumPy if available."""
    if np is None:
        raise ImportError("NumPy is required for this SVD demo.")
    U, s, VT = np.linalg.svd(np.array(A), full_matrices=False)
    return U.tolist(), s.tolist(), VT.tolist()

def svd_demo(A):
    """Wrapper to match README usage; computes SVD and returns (U, s, VT)."""
    return svd(A)

if __name__ == "__main__":
    A = [[1, 0, 0], [0, 2, 0], [0, 0, 0.5]]
    try:
        U, s, VT = svd(A)
        print("Singular values:", s)
    except ImportError as e:
        print(e)