from itertools import combinations


def apriori(transactions, min_support=0.5):
    n = len(transactions)
    min_count = int(min_support * n + 1e-9)
    # L1
    item_counts = {}
    for t in transactions:
        for item in t:
            item_counts[item] = item_counts.get(item, 0) + 1
    L = [{(i,): c for i, c in item_counts.items() if c >= min_count}]
    k = 2
    while L[-1]:
        prev = list(L[-1].keys())
        candidates = set()
        for a, b in combinations(prev, 2):
            union = tuple(sorted(set(a) | set(b)))
            if len(union) == k:
                # prune: all subsets must be frequent
                all_subsets_frequent = all(
                    tuple(sorted(sub)) in L[-1]
                    for sub in combinations(union, k - 1)
                )
                if all_subsets_frequent:
                    candidates.add(union)
        counts = {c: 0 for c in candidates}
        for t in transactions:
            st = set(t)
            for c in candidates:
                if set(c).issubset(st):
                    counts[c] += 1
        Lk = {c: cnt for c, cnt in counts.items() if cnt >= min_count}
        if not Lk:
            break
        L.append(Lk)
        k += 1
    # Flatten frequent itemsets
    frequent_itemsets = {}
    for Lk in L:
        for items, cnt in Lk.items():
            frequent_itemsets[items] = cnt / n
    return frequent_itemsets


def generate_rules(frequent_itemsets, min_confidence=0.7):
    rules = []
    for items, supp in frequent_itemsets.items():
        if len(items) < 2:
            continue
        items_set = set(items)
        for r in range(1, len(items)):
            for antecedent in map(tuple, combinations(items, r)):
                consequent = tuple(sorted(items_set - set(antecedent)))
                if antecedent in frequent_itemsets:
                    conf = supp / frequent_itemsets[antecedent]
                    if conf >= min_confidence:
                        rules.append((antecedent, consequent, supp, conf))
    return rules


if __name__ == "__main__":
    transactions = [
        ["milk", "bread"],
        ["milk", "diaper", "beer"],
        ["bread", "diaper"],
        ["milk", "bread", "diaper"],
    ]
    fi = apriori(transactions, min_support=0.5)
    rules = generate_rules(fi, min_confidence=0.7)
    print("Frequent itemsets:", fi)
    print("Rules:", rules)