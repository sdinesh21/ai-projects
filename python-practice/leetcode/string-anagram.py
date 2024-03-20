def isAnagram(str1, str2):
    if len(str1) == len(str2):
        sorted_str1 = ''.join(sorted(str1))
        sorted_str2 = ''.join(sorted(str2))
        if sorted_str1 == sorted_str2:
            return True
    return False

def isAnagramList(str1, str2):
    strList1 = []
    strList2 = []
    if len(str1) == len(str2):
        for char in str1:
            strList1.append(char)
        strList1.sort()
        for char in str2:
            strList2.append(char)
        strList2.sort()
        if strList1 == strList2:
            return True
    return False


str1 = 'anagram'
str2 = 'gamnara'

print (sorted(str1))
print (sorted(str2))

print (isAnagram(str1, str2))

print (isAnagramList(str1, str2))