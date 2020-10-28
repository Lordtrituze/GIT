def isLucky(n):
    string = str(n)
    length = len(string)
    half = int(length / 2)
    firstSum = 0
    secondSum = 0
    for i in range(half):
        number = int(string[i])
        firstSum += number
    for j in range(half + 1, len(n)):
        number = int(string[i])
        secondSum += number
    True if firstSum == secondSum else False
    
    