


def roman_to_decimal(s):
	roman_to_decimal_map = {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000
	}

	result = 0

	prev_value = 0

	for i in range(len(s)-1,-1,-1):
		curr_value = roman_to_decimal_map[s[i]]

		if curr_value < prev_value:
			result -= curr_value
		else:
			result += curr_value

		prev_value = curr_value

	return result

'''
The for loop iterates over each character in the s string, starting from the end and going backwards.
The roman_to_decimal_map is a dictionary that maps each Roman numeral character to its corresponding decimal value.
s[i] is the current character being looked at in the loop, and roman_to_decimal_map[s[i]] gets the corresponding decimal value for that character.
The decimal value for each character is stored in the curr_value variable.


(len(s)-1, -1, -1) is a tuple that specifies the range over which the for loop will iterate. The first value in the tuple, len(s)-1, is the starting point of the loop. It is set to len(s)-1 because Python indexes start at 0, so the last character in the string s has an index of len(s)-1.

The second value in the tuple, -1, is the stopping point of the loop. Since we want to iterate from the end of the string to the beginning, we set the stopping point to -1.

The third value in the tuple, -1, is the step size for the loop. It specifies that the loop should iterate backwards, from the end of the string to the beginning, one character at a time.


1.First, we create a mapping of Roman numerals to their decimal equivalents using a dictionary.
2.We initialize a variable result to 0, which will hold the decimal equivalent of the Roman numeral string.
3.We also initialize a variable prev_value to 0, which will hold the decimal value of the previous Roman numeral character encountered during the loop. This will be used to determine whether to add or subtract the current Roman numeral character from result.
4.We loop through the Roman numeral string from right to left using range(len(s)-1, -1, -1). This allows us to start with the rightmost character, which will always be added to result, and work our way to the left.
5.For each character, we look up its decimal value from the roman_to_decimal_map dictionary and store it in curr_value.
6.We compare curr_value to prev_value to determine whether to add or subtract curr_value from result.
7.If curr_value is less than prev_value, we subtract it from result (because it represents a smaller value that comes before a larger value in the Roman numeral system).
8.If curr_value is greater than or equal to prev_value, we add it to result.
9.We update prev_value to curr_value so that we can use it to compare against the next character in the loop.
10.Once the loop has finished, we return the final value of result, which represents the decimal equivalent of the input Roman numeral string.'''



print(roman_to_decimal('LLLI'))
