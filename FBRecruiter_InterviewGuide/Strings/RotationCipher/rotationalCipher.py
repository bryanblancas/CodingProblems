def rotationalCipher(arr, rf):
	rtnstr = ""
	aux = 0
	aux2 = 0

	for i in arr:
		i = ord(i)
		if (i >= 97 and i <= 122):
			aux = 26
			aux2 = 97
		elif (i >= 65 and i <= 90):
			aux = 26
			aux2 = 65
		elif (i >= 48 and i <= 57):
			aux = 10
			aux2 = 48
		else:
			rtnstr += chr(i)
			continue

		if(i+rf >= aux):
			rtnstr += chr((i-aux2+rf)%aux + aux2)
		else:
			rtnstr += chr(i+rf)

	return rtnstr

def check(ex, out):
	print("-------------------------------")
	print(ex)
	print(out)
	if(ex == out):
		return True
	return False

# a = "Za-4"
# rf = 3

# print(rotationalCipher(a, rf))

input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4
expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
output_1 = rotationalCipher(input_1, rotation_factor_1)
print(check(expected_1, output_1))

input_2 = "abcdZXYzxy-999.@"
rotation_factor_2 = 200
expected_2 = "stuvRPQrpq-999.@"
output_2 = rotationalCipher(input_2, rotation_factor_2)
print(check(expected_2, output_2))