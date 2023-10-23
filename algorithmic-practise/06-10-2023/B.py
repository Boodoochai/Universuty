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


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left_arr = merge_sort(arr[0:len(arr) // 2])
    right_arr = merge_sort(arr[len(arr) // 2:len(arr)])
    return merge(left_arr, right_arr)


n = int(input())

l1 = list(map(int, input().split()))

print(*merge_sort(l1))
