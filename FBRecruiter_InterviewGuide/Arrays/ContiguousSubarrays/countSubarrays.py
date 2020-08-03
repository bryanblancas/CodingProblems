# Time complexity O(n)
# Space complexity O(n)
def countSubarrays(arr):
	size = len(arr)
	currBigNum = 0
	idxCurrBigNum = 0
	arr1 = [0] * size
	arr1[0] = 1
	
	# O(n)
	for i in range(size):
		if(arr[i] > currBigNum):			
			arr1[i] = arr1[idxCurrBigNum]-1
			currBigNum = arr[i]
			idxCurrBigNum = i		

		if(i != 0):
			if arr[i] > arr[i-1]:
				arr1[i] += 1		

		if(i != size-1):			
			if(arr[i] > arr[i+1]):
				arr1[i] += 1		

		arr1[i] += 1		
		
		if(arr[i] < currBigNum):
			arr1[idxCurrBigNum] += arr1[i]-1		

	return arr1

test_1 = [3, 4, 1, 6, 2]
print(countSubarrays(test_1))

test_2 = [2, 4, 7, 1, 5, 3]
print(countSubarrays(test_2))