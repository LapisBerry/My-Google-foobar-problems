def solution(x, y):
    x.sort()
    y.sort()
    iterator = 0
    len_x = len(x)
    len_y = len(y)

    while iterator != len_x and iterator != len_y:
        if x[iterator] == y[iterator]:
            iterator += 1
        elif x[iterator] < y[iterator]:
            return x[iterator]
        else:
            return y[iterator]
        
    if iterator != len_x:
        return x[-1]
    return y[-1]

'''
print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13])) # output: 6
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])) # output: -4
'''
