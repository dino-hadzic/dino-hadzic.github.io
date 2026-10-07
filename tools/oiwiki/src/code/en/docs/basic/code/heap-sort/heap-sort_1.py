# --8<-- [start:sort]
def sift_down(arr, start, end):
    # Compute the indices of the parent and the children
    parent = int(start)
    child = int(parent * 2 + 1)
    while child <= end:  # Compare only while the child index is within range
        # First compare the two children and pick the larger one
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # If the parent is larger than the child the adjustment is done – leave the function
        if arr[parent] >= arr[child]:
            return
        else:  # Otherwise swap parent and child, then compare the child with the grandchildren
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child = int(parent * 2 + 1)


def heap_sort(arr, len):
    # Starting from the parent of the last node, sift down to build the heap (heapify)
    i = (len - 2) // 2
    while i >= 0:
        sift_down(arr, i, len - 1)
        i -= 1
    # Swap the first element with the one just before the already sorted part, then re-adjust the heap (the elements before the one just placed), until the array is sorted
    i = len - 1
    while i > 0:
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i - 1)
        i -= 1


# --8<-- [end:sort]

if __name__ == "__main__":
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    a = data[1 : data[0] + 1]
    heap_sort(a, len(a))
    print(*a)
