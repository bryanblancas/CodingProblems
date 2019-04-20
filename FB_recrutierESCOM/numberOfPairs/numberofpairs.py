def numberOfPairs(array, k):
	if(len(array) <= 1):
		return 0;

	array.sort()
	solutions = {}
	index_i = 0
	index_f = len(array)-1

	while(index_i < index_f):
		a = array[index_i] + array[index_f]
		if a == k:
			solutions[str(array[index_i])+","+str(array[index_f])] = str(index_i)+","+str(index_f) 
			index_i += 1
			index_f -= 1
		if a < k:
			index_i += 1
		if a > k:
			index_f -= 1
	
	return len(solutions)
		
if __name__ == '__main__':
	array = []
	k = 0

	file = open("input.txt", "r")	
	line = file.readline()[:-1]
	array = [int(i) for i in line.split(',')]

	k = file.readline()

	print numberOfPairs(array, int(k))