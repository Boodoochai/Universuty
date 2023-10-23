n = int(input())

pref_sum = []

for i in range(n):
    s = input()
    if s[0] == '+':
        x = int(s[1:])
        pref_sum.append(x)
        if len(pref_sum) != 1:
            pref_sum[-1] += pref_sum[-2]
    elif s[0] == '?':
        x = int(s[1:])
        if x == len(pref_sum):
            print(pref_sum[-1])
        else:
            print(pref_sum[-1] - pref_sum[-(x+1)])
    else:
        if 1 == len(pref_sum):
            print(pref_sum[-1])
        else:
            print(pref_sum[-1] - pref_sum[-2])
        pref_sum = pref_sum[:-1]