def solve():
    n = int(input())
    l = list(map(int, input().split()))

    nums = dict()

    for x in l:
        if x in nums.keys():
            nums[x] += 1
        else:
            nums[x] = 1

    fl = 0
    mi = 999999999999999999999999999
    for j in nums.keys():
        if nums[j] == 1 and j < mi:
            fl = 1
            mi = j

    if fl == 0:
        print(-1)
    else:
        print(l.index(mi)+1)


t = int(input())

for i in range(t):
    solve()