n = int(input())

a = list(map(int, input().split()))

used = set()
used.add(1)
s = 1
ans = []
st = 0
while True:
    ans.append(s)
    s = a[s-1]
    if s in used:
        st = s
        break
    used.add(s)

ans = ans[ans.index(s):]
print(len(ans))
print(*ans)