def countPairs(array, k):
	numMap = {}
	count = 0

	for i in array:
		numMap[i] = numMap.get(i, 0) + 1

	for key in numMap:
		if k-key in numMap:
			if k-key == key:
				# count += (numMap[key]-1)*numMap[key]/2
				count += (numMap[key]-1)*(numMap[key])/2
				numMap[key] = 0
			else:
				count += numMap[key]*numMap[k-key]
				numMap[key] = 0
				numMap[k-key] = 0

	return count

# array = [1,1,1,3,-1,5]
# array = [1,1,1,3,-1,5]
# array = [1,1,1,3,-1,5]
# array = [1,1,1,3,-1,5]
# array = [1,3,3,3,3,3,10,-6,5,-1,1]
# k = 4
array_1 = [1,2,3,4,3]
k_1 = 6
array_2 = [1,5,3,3,3]
k_2 = 6

print(countPairs(array_1, k_1))
print(countPairs(array_2, k_2))