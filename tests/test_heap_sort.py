import os
import sys
import random

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from heaps_heap_sort.algorithm import heap_sort


def run():
    for _ in range(5):
        arr = [random.randint(-100, 100) for __ in range(30)]
        assert heap_sort(arr[:]) == sorted(arr)
    print("test_heap_sort: OK")


if __name__ == "__main__":
    run()