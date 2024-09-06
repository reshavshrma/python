'''
decimal - decimal = decimal (cover all edge cases)
'''

# string to int 
def str_to_int(string):
	
	result = 0
	for i in string:
		result = result * 10 + int(i)
	return result

# decimal subtraction
def decimal_subtraction(num1, num2):
	
	dec_num1 = str_to_int(num1)
	dec_num2 = str_to_int(num2)
	
	if dec_num1 > dec_num2:
		return dec_num1 - dec_num2
	
	elif dec_num1 < dec_num2:
		result = dec_num2 - dec_num1
		return '-' + str(result)
		
	elif dec_num1 == dec_num2:
		return 0
		
	else:
		return "Invalid Input."
		
print(decimal_subtraction('25','19'))
print(decimal_subtraction('19','25'))
print(decimal_subtraction('9','9'))
print(decimal_subtraction('0','9'))
