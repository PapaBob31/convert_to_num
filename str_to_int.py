from decimal import Decimal

def convert_to_num(string):
	""" Function that converts string parameter representing a number in base 10 
		to an integer or floating point number 
	"""
	if type(string) == int or type(string) == float:
		return string
	if type(string) != str:
		raise ValueError(f"'{string}' can only be an int, string or float type")
	if len(String) == 0:
		raise ValueError("Empty string cannot be converted!")

	str_to_int_mappings = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	found_decimal_point = False
	whole_part = 0       # The part of the string before the decimal point if any
	fractional_part = 0     # The part of the string after the decimal point if any
	place_value_determinant = 10       # Variable for determining the place values of the fractional_part characters
	negative_num = False   # Used for flagging the string parameter as a negative number

	for i in range(len(string)):
		if i == 0:
			if string[i] ==  '+':
				continue
			elif string[i] == '-':
				negative_num = True
				continue

		if string[i] == '.':
			if found_decimal_point:
				raise ValueError(f"String '{string}' can only have one decimal point!")
			found_decimal_point = True
			continue

		next_no = str_to_int_mappings.get(string[i])
		if next_no != None:
			if not found_decimal_point:
				# Multiply the previous digit stored in whole_part variable by 10..
				# ..before adding the next number to get the place value of the digit
				whole_part = whole_part * 10 + next_no
			else:
				# Decimal Class was used here to get accurate floating point numbers calculations
				# Divide each digit in the fractional part with a multiple of 10 to get the place value
				fractional_part += Decimal(str(next_no))/Decimal(str(place_value_determinant))
				place_value_determinant *= 10
		else:
			raise ValueError(f"String '{string}' contains one or more characters that aren't possible parts of a number!")

	if fractional_part:
		# if the number has a fractional part
		# Convert the fractional_part variable from a decimal object to a float object
		if negative_num:
			return -(whole_part + float(fractional_part))
		return whole_part + float(fractional_part)

	if negative_num:
		return -(whole_part + fractional_part)
	return whole_part + fractional_part


