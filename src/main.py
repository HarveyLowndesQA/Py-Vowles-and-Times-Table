def isVowel(x):
    x = x.upper()
    if (x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        return True
    return False
def removeChars(s, removeVowels):
    z = "";
    if(removeVowels):
        for x in s:
            if not(isVowel(x)): z += x;
    else:
        for x in s:
            if isVowel(x):z += x;
    return z;
s1 = "QA Consulting"
s2 = "Office for National Statistics"
print(removeChars(s1, True))
print(removeChars(s2, False))