'''
binary - binary = binary 
'''

#binary subtraction
def binary_subtraction(binary_num1, binary_num2):

	num1 = int(binary_num1, 2)
	num2 = int(binary_num2, 2)
	
	if num1 > num2:
		return bin(num1 - num2)[2:]
		
	elif num1 < num2:
		result = num2 - num1
		final_result = '-' + bin(result)[2:]
		return final_result
	
	else:
		return 0
		
print(binary_subtraction("0", "0"))
print(binary_subtraction("1", "0"))
print(binary_subtraction("0", "1"))
print(binary_subtraction("100", "1"))
print(binary_subtraction("101", "010"))
