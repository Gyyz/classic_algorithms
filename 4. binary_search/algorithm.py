def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    nums = [1,3,4,7,9,12,15]
    for t in [4, 5, 15, 0]:
        print(f"search {t} ->", binary_search(nums, t))