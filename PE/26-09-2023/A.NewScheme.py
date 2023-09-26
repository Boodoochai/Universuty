l = list(map(int, input().split()))

for i in range(1, len(l)):
    if l[i-1] > l[i]:
        print("No")
        exit()

for x in l:
    if x % 25 != 0 or not (100 <= x <= 675):
        print("No")
        exit()

print("Yes")