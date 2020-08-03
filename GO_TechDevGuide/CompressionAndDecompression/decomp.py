# Get as many repetitions of string as numberstr given
def getRep(numberstr, string):
	if(len(numberstr) == 0 or len(string) == 0):
		return ""

	rtn_string = ""
	number = int(numberstr)
	for i in range(number):
		rtn_string += string

	return rtn_string			

# Read the expression looking for numbers until any different character
def readNumber(i, exp_len, expression):
	rtnstr = ""
	while (i < exp_len and expression[i] != '['):
		rtnstr += expression[i]
		i += 1
	return rtnstr, i

# Read the expression looking for lettter until any different character
def readLetters(i, exp_len, expression):
	rtnstr = ""
	while (i < exp_len and expression[i] != '[' and expression[i] >= 'a' and expression[i] <= 'z'):
		rtnstr += expression[i]
		i += 1
	return rtnstr, i

# Main decompress function
def decomp(expression):

	# Validate the lenght of the expression, if that's 0 
	# it means I have reached the end of the recursion tree
	exp_len = len(expression)
	if(exp_len == 0):
		return ""

	# This is for traverse all the current expression
	i = 0
	decomstr = ""
	while(i < exp_len):

		# Possible formats of the expression
		# 1.	EXPRESSION = NUMBER[EXPRESSION]
		# 	An common expression starts with a number which means the
		# 	number of times the expression inside brackets will be repeated
		# 2.	EXPRESION = LETTERS-NUMBERS[EXPRESION]
		# 	Also an expression can start with letters which means that
		# 	is a fixed text in the result decompress string
		# 3. 	EXPRESION = EXPRESSION-EXPRESSION
		# 	An expression can be followed by another expression

		# If the expression starts with a number, that means 
		# I have to read until '[' to get the number of times
		# I'll repeat the string inside '[]'
		# 
		# If not start with a number, that means I have fixed text 
		# in the compressed expression
		numberstr = ""
		number = 0
		if(expression[i] >= '0' and expression[i] <= '9'):
			numberstr, i = readNumber(i, exp_len, expression)
		else:
			aux, i = readLetters(i, exp_len, expression)
			decomstr += aux
			numberstr, i = readNumber(i, exp_len, expression)

		# Avoid '[' character 
		i += 1

		# Now I'll read the text inside '[]'
		# Aux is just to be sure when ends the text inside brackets
		# This is not a compiler of balanced brackets
		args = ""
		aux = 0
		while (i < exp_len):
			if(expression[i] == ']' and aux == 0):
				break
			elif(expression[i] == ']'):
				aux -= 1
			elif(expression[i] == '['):
				aux += 1	
			args += expression[i]
			i += 1

		# At this point I have the number of times I'll repeat the 
		# expression inside the brackets. If that's the case, the fixed text
		# and the expression inside brackets. So, use recursion to move ahead
		decomstr += getRep(numberstr, decomp(args))

		# Avoid ']' character 
		i += 1

	return decomstr

if __name__ == '__main__':
	# string = "bryanisraelblancaspereztengo2[dos]aniosymegusta3[4[a]bry]adios"
	# string = "2[3[a]b]"
	# string = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
	string = "2[2[abbb]c]"
	print(decomp(string))