def moves_to_open(icon):
    dist = num_by_icon[icon]
    moves = int((dist-1) / screen_capacity) + 1

    cur_icon_num = num_by_icon[icon]
    if cur_icon_num != 1:
        cur_icon = icon
        new_icon = icon_by_num[cur_icon_num - 1]
        new_icon_num = num_by_icon[new_icon]

        icon_by_num[cur_icon_num] = new_icon
        icon_by_num[new_icon_num] = cur_icon
        num_by_icon[cur_icon] = new_icon_num
        num_by_icon[new_icon] = cur_icon_num

    return moves


n, m, screen_capacity = map(int, input().split())

l = list(map(int, input().split()))

launch_order = list(map(int, input().split()))

icon_by_num = dict()
num_by_icon = dict()

for i in range(len(l)):
    icon_by_num[i+1] = l[i]
    num_by_icon[l[i]] = i+1

t = 0

for i in range(len(launch_order)):
    t += moves_to_open(launch_order[i])

print(t)
