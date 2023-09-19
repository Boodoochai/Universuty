import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
equals_bef = [0] * n

cur = a[0]
cur_num = 1

for i in range(1, n):
    if cur == a[i]:
        equals_bef[i] = cur_num
        cur_num += 1
    else:
        equals_bef.append(0)
        cur = a[i]
        cur_num = 1

for i in range(m):
    l, r, x = map(int, input().split())
    if a[r-1] != x:
        sys.stdout.write(str(r)+'\n')
    elif r-l+1 <= equals_bef[r-1]+1:
        sys.stdout.write('-1\n')
    else:
        sys.stdout.write(str(r-equals_bef[r-1]-1) + '\n')