def prefix_sum(l, r, pref_arr):
    if l == 1:
        return pref_arr[r-1]
    return pref_arr[r - 1] - pref_arr[l - 2]


n, q = map(int, input().split())

song = list(input())

for i in range(n):
    song[i] = ord(song[i]) - ord('a') + 1

prefix_arr = [0] * n

prefix_arr[0] = song[0]
for i in range(1, n):
    prefix_arr[i] = prefix_arr[i - 1] + song[i]

for i in range(q):
    l, r = map(int, input().split())
    print(prefix_sum(l, r, prefix_arr))
