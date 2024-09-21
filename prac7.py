'''
check string validity i.e. check_validity(text):
where text is made up of string of brackets like ('{', '}', '(', ')', '[', ']', '<', '>')
return valid or invalid => provide reason for the invalid cases e.g. invalid symbol or closing bracket without having open bracket
valid text => '', '{}', '[{]', etc. 
'''

def check_validity(text):

	symbols = {'{', '}', '(', ')', '<', '>', '[', ']'}
	pairs = {'{': '}', '(': ')', '[': ']', '<': '>'} 
	
	stack = []
	
	for symbol in text:
		if symbol in symbols:
			if symbol in pairs:
				stack.append(symbol)
			else:
				if not stack:
					return "Invalid"
				if symbol == pairs[stack[-1]]:
					stack.pop()
				else:
					return "Invalid"

	return "Valid"
	
	
print(check_validity("[{}]"))
print(check_validity("[{]"))
print(check_validity(""))
print(check_validity("<([{)}>]"))


'''
def get_valid_invalid_text(list):
list contains any object i.e. can be int, list, tuple, set, complex, float. function parameters 
should be list is the only restriction. returns valid and invalid count as tuple. 
sample input ['({(', [45, ("()"), ]] or '({(', [45, ("()"), ], ""]
'''

def get_valid_invalid_text(my_list):
	valid_count = 0
	invalid_count = 0
	
	for item in my_list:
		if isinstance(item, str) and item.strip():
			valid_count += 1
		else:
			invalid_count += 1

	return valid_count, invalid_count

print(get_valid_invalid_text(['({(', [45, ("()")], ""]))
