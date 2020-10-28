def reverseInParenthesis(inputString):
    if '(' not in inputString:
        return inputString
    
    openIndex = -1
    i = 0
    n = len(inputString)

    while i < n and inputString[i] != ')':
        c = inputString[i]
        if c == '(':
            openIndex = i
        i += 1

    beforeOpen = inputString[:openIndex]
    withinParen = inputString[openIndex + 1:i]
    afterClose = inputString[i + 1:]
    
    withinParenReversed = withinParen[::-1]
    inputString = f'{beforeOpen}{withinParenReversed}{afterClose}'
    return reverseInParenthesis(inputString)

a = reverseInParenthesis("(a(bc)d)(a(bc)d)")
print(a)