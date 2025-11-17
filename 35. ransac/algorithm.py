import random

def ransac_line(points, threshold=0.5, iterations=200):
    """Fit y = a x + b to points using RANSAC. Returns (a, b), inliers."""
    best_model = None
    best_inliers = []
    if len(points) < 2:
        return None, []
    for _ in range(iterations):
        p1, p2 = random.sample(points, 2)
        if p2[0] == p1[0]:
            continue  # skip vertical to keep model simple
        a = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - a * p1[0]
        inliers = [p for p in points if abs(p[1] - (a * p[0] + b)) < threshold]
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_model = (a, b)
    if best_inliers:
        # refine via least squares on inliers
        xs = [p[0] for p in best_inliers]
        ys = [p[1] for p in best_inliers]
        n = len(xs)
        xmean = sum(xs) / n
        ymean = sum(ys) / n
        sxx = sum((x - xmean) ** 2 for x in xs)
        sxy = sum((xs[i] - xmean) * (ys[i] - ymean) for i in range(n))
        a = sxy / sxx if sxx != 0 else 0.0
        b = ymean - a * xmean
        best_model = (a, b)
    return best_model, best_inliers

if __name__ == "__main__":
    pts = [(x, 2.0 * x + 1.0 + random.uniform(-0.3, 0.3)) for x in range(-10, 11)]
    # add outliers
    pts += [(5, -20), (-7, 20)]
    model, inliers = ransac_line(pts, threshold=0.5)
    print("Model:", model)
    print("Inliers:", len(inliers))