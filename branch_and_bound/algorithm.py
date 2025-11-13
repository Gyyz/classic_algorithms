from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    weight: int
    value: int

def bound(items: List[Item], idx: int, cur_weight: int, cur_value: int, capacity: int):
    if cur_weight > capacity:
        return 0
    total_value = cur_value
    w = cur_weight
    # Greedy fill by value/weight ratio for fractional bound
    for i in range(idx, len(items)):
        if w + items[i].weight <= capacity:
            w += items[i].weight
            total_value += items[i].value
        else:
            remain = capacity - w
            total_value += items[i].value * (remain / items[i].weight)
            break
    return total_value

def knapsack_branch_and_bound(items: List[Item], capacity: int):
    items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)
    best_value = 0
    best_taken = []

    def dfs(idx, cur_weight, cur_value, taken):
        nonlocal best_value, best_taken
        b = bound(items, idx, cur_weight, cur_value, capacity)
        if b <= best_value:
            return
        if idx == len(items):
            if cur_weight <= capacity and cur_value > best_value:
                best_value = cur_value
                best_taken = taken[:]
            return
        # Try include
        dfs(idx+1, cur_weight + items[idx].weight, cur_value + items[idx].value, taken + [1])
        # Try exclude
        dfs(idx+1, cur_weight, cur_value, taken + [0])

    dfs(0, 0, 0, [])
    return best_value, best_taken

if __name__ == "__main__":
    items = [Item(2,3), Item(3,4), Item(4,5), Item(5,8), Item(9,10)]
    cap = 10
    val, take = knapsack_branch_and_bound(items, cap)
    print("Best value:", val)
    print("Items taken:", take)