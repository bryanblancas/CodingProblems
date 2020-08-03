def findSignatureCounts(arr, n):
	arr2 = [0] * n
	for i in range(n):
		# print("at index "+str(i))
		j = i
		while i+1 != arr[j]:
			# print("\tat curr "+str(j)+" : "+str(arr[j]))
			arr2[j] += 1
			j = arr[j]-1
			# print("\t\t "+str(j))
		arr2[j]+=1
	return arr2


n_1 = 2
arr_1 = [2,1]

print(findSignatureCounts(arr_1, n_1))


n_2 = 4
arr_2 = [2,3,1,4]

print(findSignatureCounts(arr_2, n_2))


n_3 = 3
arr_3 = [2,3,1]

print(findSignatureCounts(arr_3, n_3))


n_4 = 2
arr_4 = [1,2]

print(findSignatureCounts(arr_4, n_4))
