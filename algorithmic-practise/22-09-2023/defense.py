def isEnough(m):
    pass


l = 1
r = 0

while r - l > 1:
    m = (r+l) // 2
    if isEnough(m):
        l = m
    else:
        r = m
