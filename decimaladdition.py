# string to int 
def str_to_int(string):
	
	result = 0
	negative = False
	
	if string[0] == '-':
		negative = True
		string = string[1:]
		
	for i in string:
		result = result * 10 + int(i)
	
	if negative:
		result = -result
		
	return result

# decimal addition
def decimal_addition(num1, num2):
	
	dec_num1 = str_to_int(num1)
	dec_num2 = str_to_int(num2)
	
	result = dec_num1 + dec_num2
	
	return str(result)
		
print(decimal_addition('25','19'))
print(decimal_addition('9','9'))
print(decimal_addition('0','0'))
print(decimal_addition('5','-10'))
print(decimal_addition('05','07'))
print(decimal_addition('999999999', '1'))
