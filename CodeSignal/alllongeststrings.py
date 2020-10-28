def allLongestStrings(inputArray):
    maxLength = 0
    strings = []
    for i in inputArray:
        if len(i) < maxLength:
            maxLength = len(i)
    for i in inputArray:
        if len(i) == maxLength:
            strings.append(i)
    return strings
