"""
third practical - make a function without using the print statement in it.
input from the user. if enetered user no < 1, show enter a greater no than 1,
else, show valid number. function name should be like printPattern.

=> check for 1.25, 1.27, 2.50, 3.0007 and if user entered this, show error
  
"""

def printPattern(enteredNumber): 

	if(enteredNumber.is_integer() < 1): 
		return "enter a number greater than 1"
	else: 
		return "valid number"

#test cases
print(printPattern(3.0))
print(printPattern(1.25))
print(printPattern(1.27))
print(printPattern(2.50))
print(printPattern(3.0007))

''' 1. Write the code for the patterns shown on the board - Star pattern having 1 2 3 in the middle '''

# Pattern 1 

def printPattern_1(): 
	for i in range(3):
		for j in range(5): 
			if ((i == 0 and j == 2) or (i == 1 and j in [1,3]) or (i == 2 and j < 5)):
				print("*", end=' ')
			elif (i == 1 and j == 2):
				print("1", end=' ')
			else: 
				print(" ", end=' ')
		print()

printPattern_1()

print()

# Pattern 2

def printPattern_2():
	for i in range(6):
		for j in range(7):
			if ((i == 0 and j == 3) or (i in [1,3] and j in [2,4]) or (i == 2 and j in [1,5]) or (i in [4,5] and j < 7)):
				print("*", end=' ')
			elif (i == 2 and j == 3):
				print("2", end=' ')
			else: 
				print(" ", end=' ')
				
		print()
		
printPattern_2()

print() 

# Pattern 3

def printPattern_3(): 
	for i in range(9):
		for j in range(9): 
			if((i == 0 and j == 4) or (i in [1,5] and j in [3,5]) or (i in [2,4] and j in [2,6]) or (i == 3 and j in [1,7]) or (i in [6,7,8] and j < 9)):
				print("*", end=' ')
			elif (i == 3 and j == 4):
				print("3", end=' ')
			else: 
				print(" ", end=' ')
				
		print()
		
printPattern_3()

print() 

''' 2. Print the patterns on the board '''

def pattern_1():

	for i in range(3):
		for j in range(3):
			if ((i == 0 and j == 1) or (i == 1 and j in [0,2])):
				print("+", end=' ')
			elif (i == 2 and j == 1):
				print("-", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern_1()

print()

def pattern_2():

	for i in range(5):
		for j in range(5):
			if ((i == 0 and j == 2) or (i in [1,3] and j in [1,3]) or (i == 2 and j in [0,4])):
				print("+", end=' ')
			elif (i == 4 and j == 2):
				print("-", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern_2()

print()

def pattern_3():

	for i in range(7):
		for j in range(7):
			if ((i == 0 and j == 3) or (i in [1,5] and j in [2,4]) or (i in [2,4] and j in [1,5]) or (i == 3 and j in [0,6])):
				print("+", end=' ')
			elif (i == 6 and j == 3):
				print("-", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern_3()

''' 3. Print the patterns on the board ''' 

def pattern1(): 
	for i in range(3):
		for j in range(3):
			if ((i == 0 and j == 1) or (i == 1 and j in [0,2])):
				print("+", end=' ')
			elif (i == 2 and j == 1):
				print("-", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern1()

print() 

def pattern2(): 
	for i in range(5):
		for j in range(5):
			if ((i == 0 and j == 2) or (i == 1 and j in [1,3]) or (i == 2 and j in [0,4])):
				print("+", end=' ')
			elif ((i == 3 and j in [1,3]) or (i == 4 and j == 2)):
				print("-", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern2()

print() 

def pattern3():

	for i in range(7):
		for j in range(7):
			if ((i == 0 and j == 3) or (i in [1,5] and j in [2,4]) or (i in [2,4] and j in [1,5]) or (i == 3 and j in [0,6]) or (i == 6 and j == 3)):
				print("+", end=' ')
			else:
				print(" ", end=' ')
		print()

pattern3()


''' 4. Create a modulo function which performs % operation of two numbers '''

def modulo(numerator, denominator):
	
	if denominator == 0:
		return "Error, 0 not expected. Please, enter value other than 0"
	else: 
		quotient = numerator//denominator
		rem = numerator-quotient*denominator
		return rem
		
''' Test cases 

print(modulo(5,0)) 
print(modulo(0,0))
print(modulo(0,5))
print(modulo(-5,1))
print(modulo(5,-1))
print(modulo(-5,-1))

'''
numerator = (int(input("Enter numerator: ")))
denominator = (int(input("Enter denominator: ")))
print(modulo(numerator, denominator)) 


''' 5. Count of substring '''

def count_subString(string, sub_string, flag):

	count = 0
	i = 0
	len_subString = len(sub_string)
	
	while (i <= len(string) - len_subString):
		if (string[i:i + len_subString] == sub_string):
			count += 1
			if flag:
				i += 1
			else:
				i += len_subString
		else:
			i += 1
	return count 
	
print(count_subString("sgggs", "gg", True))
print(count_subString("sgggs", "gg", False))
