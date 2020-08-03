def isSubstring(s, t):
	size_t = len(t)
	size_s = len(s)
	idx_t = 0

	if(size_s < size_t):
		return False

	for i in s:
		if(i == t[idx_t]):
			idx_t += 1
		else:
			idx_t = 0
		if(idx_t >= size_t):
			return True
	return False

if __name__ == '__main__':
	s = "bryan"
	t = "t"
	print(isSubstring(s,t))