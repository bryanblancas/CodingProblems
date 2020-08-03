def canGetExactChange(tm, denom):
	if(tm == 0):
		return True

	for i in range(len(denom)):
		if(denom[i] > tm):
			i -= 1
			break

	if(i < 0):
		return False

	x = int(tm/denom[i])
	y = tm - denom[i]*x
	
	return canGetExactChange(y, denom)

def check(a, b):
	if(a == b):
		return "Correct"
	return "Incorrect"

target_1 = 94
arr_1 = [5, 10, 25, 100, 200]
expected_1 = False
output_1 = canGetExactChange(target_1, arr_1)
print(check(expected_1, output_1))

target_2 = 75
arr_2 = [4, 17, 29]
expected_2 = True
output_2 = canGetExactChange(target_2, arr_2)
print(check(expected_2, output_2))