# d = {1: {2}, 2: {1, 3}, 3: {2}, 4: {1, 5, 7}, 5: {2, 4, 6, 8}, 6 : {3, 5, 9}, 7: {4, 8}, 8: {7, 5, 9}, 9:{6, 8}}
d = {1: {2}, 2: {1, 3}, 3: {2}, 4: {5}, 5: {4, 6}, 6: {5}, 7: {8}, 8: {7, 9}, 9: {8}}

a, b = map(int, input().split())

if b in d[a]:
    print("Yes")
else:
    print("No")