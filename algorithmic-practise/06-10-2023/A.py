def merge(arr1, arr2):
    l = [0] * (len(arr1) + len(arr2))
    p1 = 0
    p2 = 0
    while p1 + p2 < len(l):
        if p1 == len(arr1):
            l[p1 + p2] = arr2[p2]
            p2 += 1
        elif p2 == len(arr2):
            l[p1 + p2] = arr1[p1]
            p1 += 1
        elif arr1[p1] < arr2[p2]:
            l[p1 + p2] = arr1[p1]
            p1 += 1
        else:
            l[p1 + p2] = arr2[p2]
            p2 += 1
    return l


n, m = map(int, input().split())

l1 = list(map(int, input().split()))

l2 = list(map(int, input().split()))

print(*merge(l1, l2))
