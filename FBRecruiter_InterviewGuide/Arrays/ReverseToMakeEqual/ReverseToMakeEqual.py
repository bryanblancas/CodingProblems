def reverseToMakeEqual(a, b):
	if len(a) != len(b):
		return False

	a.sort() #O(nlogn)
	b.sort()

	for i in range(len(a)): #O(n)
		if a[i] != b[i]:
			return False

	return True


a_1 = [1, 2, 3, 4]
b_1 = [1, 4, 3, 2]

print(reverseToMakeEqual(a_1, b_1))

a_2 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 5] 

print(reverseToMakeEqual(a_2, b_2))