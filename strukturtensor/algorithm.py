def central_diff(image, r, c):
    rows, cols = len(image), len(image[0])
    # clamp neighbors
    left = image[r][max(0, c - 1)]
    right = image[r][min(cols - 1, c + 1)]
    up = image[max(0, r - 1)][c]
    down = image[min(rows - 1, r + 1)][c]
    ix = 0.5 * (right - left)
    iy = 0.5 * (down - up)
    return ix, iy

def structure_tensor(image, window=1):
    rows, cols = len(image), len(image[0])
    result = [[None for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            J11 = J22 = J12 = 0.0
            for dr in range(-window, window + 1):
                for dc in range(-window, window + 1):
                    rr = min(rows - 1, max(0, r + dr))
                    cc = min(cols - 1, max(0, c + dc))
                    ix, iy = central_diff(image, rr, cc)
                    J11 += ix * ix
                    J22 += iy * iy
                    J12 += ix * iy
            # eigenvalues of 2x2 matrix [[J11, J12],[J12, J22]]
            trace = J11 + J22
            det = J11 * J22 - J12 * J12
            disc = max(0.0, trace * trace - 4 * det)
            lambda1 = 0.5 * (trace + disc ** 0.5)
            lambda2 = 0.5 * (trace - disc ** 0.5)
            # classification
            if lambda1 < 1e-3 and lambda2 < 1e-3:
                cls = 'flat'
            elif lambda1 > 1e-3 and lambda2 < 1e-3:
                cls = 'edge'
            else:
                cls = 'corner'
            result[r][c] = (lambda1, lambda2, cls)
    return result

if __name__ == "__main__":
    img = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    st = structure_tensor(img, window=1)
    print("Center pixel classification:", st[1][1][2])