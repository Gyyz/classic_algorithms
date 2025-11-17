from typing import Dict, Tuple, List

Monomial = Tuple[int, int]  # exponents (x^a y^b)
Poly = Dict[Monomial, float]

def add_poly(p: Poly, q: Poly) -> Poly:
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, 0.0) + c
        if abs(r[m]) < 1e-12:
            r.pop(m)
    return r

def neg_poly(p: Poly) -> Poly:
    return {m: -c for m, c in p.items()}

def mul_monomial(p: Poly, m: Monomial, k: float) -> Poly:
    a, b = m
    return {(ma+a, mb+b): c*k for (ma, mb), c in p.items()}

def leading_term(p: Poly) -> Tuple[Monomial, float]:
    if not p:
        return ((0,0), 0.0)
    m = max(p.keys(), key=lambda e: (e[0], e[1]))  # lex x > y
    return m, p[m]

def reduce_poly(f: Poly, G: List[Poly]) -> Poly:
    r = dict(f)
    changed = True
    while changed:
        changed = False
        for g in G:
            if not g:
                continue
            (ma, mb), lc = leading_term(g)
            (ra, rb), rc = leading_term(r)
            if ra >= ma and rb >= mb and lc != 0:
                # cancel leading term
                factor_m = (ra - ma, rb - mb)
                factor_k = rc / lc
                r = add_poly(r, neg_poly(mul_monomial(g, factor_m, factor_k)))
                changed = True
                if not r:
                    return {}
    return r

def lcm_monomial(a: Monomial, b: Monomial) -> Monomial:
    return (max(a[0], b[0]), max(a[1], b[1]))

def s_polynomial(f: Poly, g: Poly) -> Poly:
    (fa, fb), fc = leading_term(f)
    (ga, gb), gc = leading_term(g)
    l = lcm_monomial((fa, fb), (ga, gb))
    mf = (l[0]-fa, l[1]-fb)
    mg = (l[0]-ga, l[1]-gb)
    return add_poly(mul_monomial(f, mf, 1.0/fc), neg_poly(mul_monomial(g, mg, 1.0/gc)))

def buchberger(F: List[Poly]) -> List[Poly]:
    G = [reduce_poly(f, []) for f in F]
    changed = True
    while changed:
        changed = False
        for i in range(len(G)):
            for j in range(i+1, len(G)):
                S = s_polynomial(G[i], G[j])
                R = reduce_poly(S, G)
                if R:
                    G.append(R)
                    changed = True
    # normalize leading coefficients to 1
    NG = []
    for g in G:
        if not g:
            continue
        m, c = leading_term(g)
        NG.append({k: v/c for k, v in g.items()})
    return NG

def poly_str(p: Poly) -> str:
    if not p:
        return "0"
    terms = []
    for (a,b), c in sorted(p.items(), key=lambda e: (e[0][0], e[0][1]), reverse=True):
        term = f"{c:.2f}"
        if a: term += f"*x^{a}"
        if b: term += f"*y^{b}"
        terms.append(term)
    return " + ".join(terms)

if __name__ == "__main__":
    # Example: F = {x^2 + xy + 1, xy + y^2 + 1}
    f1 = {(2,0):1.0, (1,1):1.0, (0,0):1.0}
    f2 = {(1,1):1.0, (0,2):1.0, (0,0):1.0}
    G = buchberger([f1, f2])
    print("Groebner basis (toy):")
    for g in G:
        print(" ", poly_str(g))