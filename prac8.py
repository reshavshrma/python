'''
Create a count function which will return total no of palindrome sequences 
in a list object, there could be any no of list tuple string integer element
or reference of these elements in that list
'''
 
def is_palindrome(item):
	str_item = str(item)
	return str_item == str_item[::-1]
	
def count_palindrome(my_list):
	count = 0
	regNo = 11
	
	for item in my_list:
		if isinstance(item, (list, tuple)):
			for sub_item in item:
				if len(str(sub_item)) % regNo == 7:
					count += is_palindrome(sub_item)
		else:
			if len(str(item)) % regNo == 7 and is_palindrome(item):
				count += 1
	return count 
	
test_list_1 = [121, "abcba", 23432, [11, 22, 33, 44, 45654], ("madam", "testtset", 1234321)]
test_list_2 = [123, "hello", 34543, [10101, "radar"], ("wow", "noon")]
test_list_3 = []

print(count_palindrome(test_list_1))
print(count_palindrome(test_list_2))
print(count_palindrome(test_list_3))
