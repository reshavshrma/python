"""
third practical - make a function without using the print statement in it.
input from the user. if enetered user no < 1, show enter a greater no than 1,
else, show valid number. function name should be like printPattern.

=> check for 1.25, 1.27, 2.50, 3.0007 and if user entered this, show error

=> if enteredNumber = 1,2,3. show patterns (shown on board). 

	*
      * 1 *
    * * * * *
  
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
