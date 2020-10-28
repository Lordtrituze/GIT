def commonCharacterCount(s1, s2):
    count = 0
    common= []
    for i in s1:
        if i in s2 and i not in common:
            if s1.count(i) < s2.count(i):
                number = s1.count(i)
                count += number
            else:
                number = s2.count(i)
                count += number
            common.append(i)
    
    #return count
    print(count)

commonCharacterCount("aabbb", "abaaba")