def partition(a, low, high):
    p = low
    for i in range(low, high):
        if a[i] < a[high]:
            a[i], a[p] = a[p], a[i]
            p += 1
    a[p], a[high] = a[high], a[p]
    return p


def select(a, low, high, k):
    pivot = partition(a, low, high)
    if k-1 < pivot:
        return select(a, low, pivot - 1, k)
    if k-1 > pivot:
        return select(a, pivot + 1, high, k)
    return a[k-1]


def kth(a, k):
    return select(a, 0, len(a) - 1, k)


print(kth([5, 4, 3, 2, 1], 2))
