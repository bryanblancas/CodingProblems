import math 

def findEncryptedWords(s):

	length = len(s)
	if(length <= 1):
		return s

	middleIdx = int(math.ceil((length-1)/2))

	return s[middleIdx] + findEncryptedWords(s[:middleIdx]) + findEncryptedWords(s[middleIdx+1:])

def check(s, t):
	if(s == t):
		return True
	return False

s = "BRYANI"
expected = "YBRNAI"
print(check(findEncryptedWords(s), expected))

s1 = "abc"
expected_1 = "bac"
print(check(findEncryptedWords(s1), expected_1))

s2 = "abcd"
expected_2 = "bacd"
print(check(findEncryptedWords(s2), expected_2))