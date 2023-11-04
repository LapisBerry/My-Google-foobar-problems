def solution(l):
    l = [[int(number) for number in stringInList.split('.') ] for stringInList in l] # turn to list of lists of numbers
    l.sort() # it's integer now, so it can be sorted
    l = [[str(number) for number in listOfNumber] for listOfNumber in l] # turn to list of lists of strings
    l = ['.'.join(listOfNumber) for listOfNumber in l] # turn to list of strings
    return l    

'''
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
'''
