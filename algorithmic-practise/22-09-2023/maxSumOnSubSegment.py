n = int(input())
l = list(map(int, input().split()))

ma = - 999999999999999999999
su = 0
ma_st = 0
ma_end = 0
cur_st = 0
cur_end = 0

for i in range(n):
    su += l[i]
    if su > ma:
        ma = su
        ma_st = cur_st
        ma_end = cur_end
    cur_end += 1
    if su < 0:
        su = 0
        cur_st = i+1
        cur_end = i+1

print(ma_st+1, ma_end+1, ma)