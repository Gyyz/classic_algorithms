import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from dynamic_programming_edit_distance.algorithm import edit_distance


def run():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "") == 0
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("abc", "") == 3
    assert edit_distance("flaw", "lawn") == 2
    print("test_edit_distance: OK")


if __name__ == "__main__":
    run()