def minLengthString(s, t):
	map = {}
	count = 0
	countCoincidences = len(t)

	for i in t:
		map[i] = map.get(i, 0) + 1

	for i in s:
		if i in map:
			if(map[i] != 0):
				map[i] -= 1
				countCoincidences -= 1
		count += 1
		if(countCoincidences == 0):
			return count

	return -1

s1 = "dcbefebce"
t1 = "fd"
print(minLengthString(s1,t1))

s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
t2 = "cbccfafebccdccebdd"
print(minLengthString(s2,t2))

s2 = "bryan israel bryan perez"
t2 = "bryann"
print(minLengthString(s2,t2))