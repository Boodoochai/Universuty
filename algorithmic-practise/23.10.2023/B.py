def f(fr, to, k, posl, ans, used):
    if len(posl) == k-1:
        for i in range(fr, to+1):
            new_ans = tuple(posl.copy() + [i])
            if new_ans not in used:
                used.add(new_ans)
                ans.append(new_ans)
        return
    for i in range(fr, to+1):
        if to-i+1 >= k - len(posl):
            posl.append(fr)
            f(i+1, to, k, posl, ans, used)
            posl.pop()


n, k = map(int, input().split())

ans = []
f(0, n, k+1, [], ans, set())

for x in ans:
    print(*x[1:])
