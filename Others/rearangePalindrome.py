# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.


# __________________________
# string = "a" -> TRUE
# string = "aab" -> TRUE : "aba"

# anitala v alatina
# poop 

# if(len(string) % 2 == 0): I don't have a pivot
# else: i have a pivot 

# aaabbc
# len("aabbbcc") = 7

# a
# b
# c

# TRUE: abccba
# __________________________

def palindromeRearranging(inputString):
	hs = set()

	for letter in inputString:
		if letter in hs:
			hs[letter].pop()
		else:
			hs[letter]

	if (len(hs) > 1):
		return False
	return True