#Solution: 
def capital_indexes(word):
    result = []
    i = 0
    while i < len(word): 
        if word[i].upper() == word[i]:
            result.append(i)
        i += 1
    return result
    
print(capital_indexes("HeLlo"))

#Better solution given 
from string import uppercase

def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]
