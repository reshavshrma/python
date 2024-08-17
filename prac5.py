''' Prac 5

def change_case(text, style) => style is case in-sensitive (use of lower, upper, swapping is prohibited)
user can enter the style as capital or small

1. convert to capital
2. convert to small 
3. convert to reverse 
4. convert to ZigZag 

'''

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

# convert_to_small_case

def convert_to_small_case(text):
	result = ""
	for char in text:
		if('A' <= char <= 'Z'):
			result = result + chr(ord(char)+32)
		else:
			result = result + char 
	return result

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

#change_case

def change_case(text, style):
	if style == "c" or style == "C":
		return convert_to_capital_case(text)
	elif style == "s" or style == "S":
		return convert_to_small_case(text)
	elif style == "r" or style == "R":
		return convert_to_reverse_case(text)
	elif style == "z" or style == "Z":
		return convert_to_zigzag_case(text)
	else:
		return "Inavlid Style. Please enter a valid style."
	
	
#Test cases
print(change_case("SGGSNed", "c"))
print(change_case("SGGSNed", "C"))
print(change_case("SGGSNed", "s"))
print(change_case("SGGSNed", "S"))
print(change_case("SGGSNed", "r"))
print(change_case("SGGSNed", "R"))
print(change_case("SGGSNed", "z"))
print(change_case("SGGSNed", "Z"))
