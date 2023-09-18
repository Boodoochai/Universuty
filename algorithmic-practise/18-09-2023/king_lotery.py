import copy


def check_position(x, y, ticket, key_word, visited, ind):
    if visited[x][y] == 1:
        return False

    if ticket[x][y] != key_word[ind]:
        visited[x][y] = 0
        return False

    if ind == len(key_word) - 1:
        return True

    s = 0

    visited[x][y] = 1
    s += check_position(x + 1, y, ticket, key_word, visited, ind + 1)
    s += check_position(x - 1, y, ticket, key_word, visited, ind + 1)
    s += check_position(x, y + 1, ticket, key_word, visited, ind + 1)
    s += check_position(x, y - 1, ticket, key_word, visited, ind + 1)

    if s != 0:
        visited[x][y] = 0
        return True

    return False


def main():
    key_word = list(input())

    ticket = [[0] * 7 for i in range(7)]
    for i in range(1, 6):
        ticket[i] = ['0'] + list(input()) + ['0']

    visited = [[0] * 7 for i in range(7)]

    for i in range(1, 6):
        for j in range(1, 6):
            if ticket[i][j] == key_word[0]:
                if check_position(i, j, ticket, key_word, copy.deepcopy(visited), 0):
                    print("YES")
                    return
    print("NO")


main()
