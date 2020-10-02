def isSubstring(s, t):
	size_t = len(t)
	size_s = len(s)
	idx_t = 0

	if(size_s < size_t or size_t == 0 or size_s == 0):
		return False

	i = 0
	while i < size_s:
		if(s[i] == t[idx_t]):
			idx_t += 1
		else:
			idx_t = 0
			i -= 1

		i += 1

		if(idx_t >= size_t):
			return True

	return False

if __name__ == '__main__':
	s = "brybryannnnn"
	t = "bryan"
	print(isSubstring(s,t))