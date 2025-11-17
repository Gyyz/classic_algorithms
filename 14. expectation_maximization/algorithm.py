import math
import random

def normal_pdf(x, mu, var):
    return (1/math.sqrt(2*math.pi*var)) * math.exp(- (x-mu)**2 / (2*var))

def em_gaussian_mixture_1d(data, k=2, iters=20):
    # initialize
    mus = [min(data) + (i+1)*(max(data)-min(data))/(k+1) for i in range(k)]
    vars_ = [1.0 for _ in range(k)]
    pis = [1.0/k for _ in range(k)]

    for _ in range(iters):
        # E-step: responsibilities
        resp = []
        for x in data:
            numerators = [pis[j]*normal_pdf(x, mus[j], vars_[j]) for j in range(k)]
            denom = sum(numerators) + 1e-12
            resp.append([n/denom for n in numerators])

        # M-step
        Nk = [sum(r[j] for r in resp) for j in range(k)]
        for j in range(k):
            mus[j] = sum(r[j]*x for r, x in zip(resp, data)) / (Nk[j] + 1e-12)
            vars_[j] = sum(r[j]*(x - mus[j])**2 for r, x in zip(resp, data)) / (Nk[j] + 1e-12)
            pis[j] = Nk[j] / len(data)

    return mus, vars_, pis

def em_gaussian_mixture(data, k=2, iters=20):
    """Alias to match README usage; runs 1D Gaussian mixture EM and returns (means, variances, weights)."""
    return em_gaussian_mixture_1d(data, k=k, iters=iters)

if __name__ == "__main__":
    random.seed(0)
    data = [random.gauss(-2, 0.5) for _ in range(100)] + [random.gauss(3, 1.0) for _ in range(100)]
    mus, vars_, pis = em_gaussian_mixture_1d(data, k=2, iters=30)
    print("means:", mus)
    print("vars:", vars_)
    print("weights:", pis)