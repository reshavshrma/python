''' Prac 5

def change_case(text, style) => style is case in-sensitive (use of lower, upper, swapping is prohibited)
user can enter the style as capital or small

1. convert to capital
2. convert to small 
3. convert to reverse 
4. convert to ZigZag 

'''
# def change_case(text, style):

# convert_to_capital_case

def convert_to_capital_case(text):
	result = ""
	#iterate through whole text
	for char in text:
		#SGGSNed - from small letter, see e is between a and z
		if('a' <= char <= 'z'):
			# since, ord('a') = 97 and ord('A') = 65, then to convert 'a' to 'A', simply 97-65 = 32, diff between two is 32 
			result = result + chr(ord(char)-32) 
		else:
			result = result + char #if no char is small, print same
	return result
	
print(convert_to_capital_case("SGGSNed"))

# convert_to_small_case

def convert_to_small_case(text):
	result = ""
	for char in text:
		if('A' <= char <= 'Z'):
			result = result + chr(ord(char)+32)
		else:
			result = result + char 
	return result
	
print(convert_to_small_case("SGGSNed"))

#convert_to_reverse_case

def convert_to_reverse_case(text):
	result =  ""
	for char in text:
		if('A' <= char <= 'Z'):
			result = result + chr(ord(char)+32)
		elif('a' <= char <= 'z'):
			result = result + chr(ord(char)-32)
		else:
			result = result + char
			
	return result
	
print(convert_to_reverse_case("SGGSNed"))

#convert_to_zigzag_case

def convert_to_zigzag_case(text):
	result = ""
	flag = True
	for char in text:
		if('a' <= char <= 'z'):
			if flag:
				result = result + chr(ord(char)-32)
			else:
				result = result + char
			flag = not flag
		elif('A' <= char <= 'Z'):
			if flag: 
				result = result + char
			else: 
				result = result + chr(ord(char)+32)
			flag = not flag
		else: 
			result = result + char
	
	return result

print(convert_to_zigzag_case("SGGSNed"))
