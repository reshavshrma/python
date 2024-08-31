'''
1. def slice(object, string_parameter):
2. Implement DFA which accepts all the string Z = {'a','b'} such that each string ends with 'b', def DFA_ends_with_b(text):
   should return "accepted" or "rejected"
3. def rom(text, text_base):
4. def base(text, text_base, output_base):
'''

# 1. user defined slice operator

def slice(get_slice, start, end):
	
	result = ""
	
	for i in range(start, end):
		result = result + get_slice[i]
	
	return result
	
string = "sggsNanded"
print(slice(string, 1, 5))

# 2. DFA accepts all strings ending with 'b'

def DFA_ends_with_b(text):

	state = 'q0'
	
	for char in text:
		if state == 'q0':
			if char == 'a':
				state = 'q0'
			elif char == 'b':
				state = 'q1'
			else: 
				return "Rejected"
		
		elif state == 'q1':
			if char == 'a':
				state = 'q0'
			elif char == 'b':
				state = 'q1'
			else:
				return "Rejected"
				
	if state == 'q1':
		return "Accepted"
	else:
		return "Rejected"

#Test cases
print(DFA_ends_with_b("b"))
print(DFA_ends_with_b("babb"))
print(DFA_ends_with_b("abab"))
print(DFA_ends_with_b("ababa"))
print(DFA_ends_with_b("aab"))
print(DFA_ends_with_b("aacbbb"))

# 3. number to roman number

def roman(text, text_base):
    def decimal_to_roman(number):
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_num = ''
        i = 0

        if number <= 0:
            return "Invalid"

        while number > 0:
            for _ in range(number//value[i]):
                roman_num = roman_num + symbol[i]
                number = number - value[i]
            i = i + 1

        return roman_num

    decimal_number = int(text, text_base)
    return decimal_to_roman(decimal_number)

print(roman("0", 10))
print(roman("11", 10))

# 4. base conversion 

def base(text, text_base, Output_Base):
	decimal = 0
	power = 0
	
	for digit in str(text)[::-1]:
		decimal = decimal + int(digit) * (text_base**power)
		power = power + 1
	result = ''
	
	while decimal > 0:
		result = str(decimal % Output_Base) + result
		decimal = decimal//Output_Base
	return result
    
print(base("11",2,2))
print(base("11",2,5))
print(base("100",2,10))
