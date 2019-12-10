def rotate(string, i):
	return string[i:]+string[:i]

def is_rotation(str_r, string):
	l_str = len(string)
	l_str_r = len(str_r)

	if(l_str != l_str_r):
		return False
	if(str_r in string):
		return True

	for i in range(1, l_str):
		aux = rotate(str_r, i)
		if(aux in string):
			return True

	return False


print(is_rotation("lyon", "only"))
print(is_rotation("lnyo", "only"))
print(is_rotation("lyoni", "onlyi"))
print(is_rotation("an israelbry", "bryan israel"))
