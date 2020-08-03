# Assuming that every element in a is in b too and both a and b have not repeated characteres
def matchingPairs(a, b):
	count = 0
	mps = 0

	for i in range(len(a)):
		if(a[i] == b[i]):
			count += 1
		elif(mps == 0):
			j = findPair(a, i, b[i])
			aux = a[i]
			a[i] = a[j]
			a[j] = aux
			count += 1
			mps = 1

	if(mps == 0):
		count -= 2

	return count

def findPair(a, i, c):
	for j in range(i, len(a)):
		if (a[j] == c):
			return j
	return -1


n_1, s_1, t_1 = 5, ['a','b','c','d','e'], ['a','d','c','b','e']
expected_1 = 5
print(matchingPairs(s_1, t_1))

s_2, t_2 = ['a','b','c','d'], ['a','b','c','d']
expected_2 = 2
print(matchingPairs(s_2, t_2))

s_2, t_2 = ['a','b','c','d'], ['d','a','b','c']
expected_2 = 2
print(matchingPairs(s_2, t_2))