def product(xs):
    if xs:
        output = 1
        for x in xs:
            output *= x
        return output
    else:
        return 0

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    
    i = 0
    countNegative = 0
    mostNegativeNumber = -1000
    indexOfMostNegativeNumber = 0
    while i != len(xs):
        if xs[i] > 0:
            i += 1
        elif xs[i] < 0:
            countNegative += 1
            if mostNegativeNumber < xs[i]:
                mostNegativeNumber = xs[i]
                indexOfMostNegativeNumber = i
            i += 1
        else:
            xs.pop(i)
            indexOfMostNegativeNumber -= 1

    
    if countNegative % 2 == 1:
        xs.pop(indexOfMostNegativeNumber)
    
    return str(product(xs))

'''
print(solution([2, 0, 2, 2, 0])) # output: 8
print(solution([-2, -3, 4, -5])) # output: 60
print(solution([0])) # output: 0
print(solution([3])) # output: 3
print(solution([-3])) # output: -3
print(solution([-4, 0])) # output: 0
print(solution([-4, 4])) # output: 4
print(solution([0, 5, -5])) # output: 5
print(solution([0, -5, -5])) # output: 25
'''
