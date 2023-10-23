def count_smaller(x, arr):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (r + l) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    return l + 1


def count_inversions(l):
    if len(l) <= 1:
        return 0
    inv = 0
    LeftHalf = l[0:len(l) // 2]
    RightHalf = l[len(l) // 2:len(l)]
    inv += count_inversions(LeftHalf)
    inv += count_inversions(RightHalf)
    q = sorted(RightHalf)
    for x in LeftHalf:
        inv += count_smaller(x, q)
    return inv


n = int(input())

l = list(map(int, input().split()))

print(count_inversions(l))
