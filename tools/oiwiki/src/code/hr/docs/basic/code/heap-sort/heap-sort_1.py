# --8<-- [start:sort]
def sift_down(arr, start, end):
    # Izračunaj indekse roditelja i djece
    parent = int(start)
    child = int(parent * 2 + 1)
    while child <= end:  # Usporedba samo dok je indeks djeteta unutar granica
        # Prvo usporedi dvoje djece i odaberi veće
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # Ako je roditelj veći od djeteta, popravak je gotov – izađi iz funkcije
        if arr[parent] >= arr[child]:
            return
        else:  # Inače zamijeni roditelja i dijete, pa dijete usporedi s unucima
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child = int(parent * 2 + 1)


def heap_sort(arr, len):
    # Kreni od roditelja posljednjeg čvora i radi sift down da izgradiš hrpu (heapify)
    i = (len - 2) // 2
    while i >= 0:
        sift_down(arr, i, len - 1)
        i -= 1
    # Zamijeni prvi element s elementom ispred već sortiranog dijela, pa ponovno popravi hrpu (elemente ispred upravo postavljenog), sve dok niz nije sortiran
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
