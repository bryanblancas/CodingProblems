def balancedSplit(arr):
	arr.sort()

	totalSum = 0
	for i in arr:
		totalSum += i

	i = len(arr)-1
	rightSum = 0
	for i in range(i, -1, -1):
		rightSum += arr[i]
		if(rightSum == totalSum - rightSum):
			if(arr[i] == arr[i-1]):
				return False
			return True
		if(rightSum < totalSum):
			return False

def check(a, b):
	if(a == b):
		return "Correct!!"
	return "Incorrect :("

arr_1 = [2, 1, 2, 5]
expected_1 = True
output_1 = balancedSplit(arr_1)
print(check(expected_1, output_1))

arr_2 = [3, 6, 3, 4, 4]
expected_2 = False
output_2 = balancedSplit(arr_2)
print(check(expected_2, output_2))