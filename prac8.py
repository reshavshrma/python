''' 
04-10-2024 => def get_even_odd_count(list) - list is the list of integers objects
'''

import time

def get_even_odd_count_approach1(int_list):

	even_count = 0
	odd_count = 0
	
	for i in int_list:
		if i % 2 == 0:
			even_count += 1
		else:
			odd_count += 1	
	return even_count, odd_count
	
def get_even_odd_count_approach2(int_list):
        
        even_count = 0
        odd_count = 0
        
        for i in int_list:
        	t = i % 2
        	if t == 1:
        		odd_count += 1
        	else:
        		even_count += 1
        return even_count, odd_count
        
def get_even_odd_count_approach3(int_list):
	
	even_count = 0
	odd_count = 0
	
	for i in int_list:
		if i & 1 == 0:
			even_count += 1
		else:
			odd_count += 1

def check_performance(approaches):

	time_taken = []
	test_data = list(range(1, 1000000))
	
	for approach in approaches:
		start_time = time.time()
		approach(test_data)
		end_time = time.time()
		time_taken.append(end_time - start_time)
	return time_taken

print(check_performance([get_even_odd_count_approach1, get_even_odd_count_approach2, get_even_odd_count_approach3]))

'''
return the second largest and second smallest, def get_secondLargest_secondSmallest(my_list) 
where my_list is the list of objects (int, list, tuple or dict) and use of built-ins functions is prohibited. 
'''

def get_num_list(lst):
	ans = []
	
	for item in lst:
		if isinstance(item, int):
			ans.append(item)
		elif isinstance(item, (list, tuple, set)):
			ans += get_num_list(list(item))
		elif isinstance(item, dict):
			item = list(item.keys()) + list(item.values())
			ans += get_num_list(item)
	return ans

def get_secondLargest_secondSmallest(my_list):
	
	nums_list = get_num_list(my_list)
	if len(nums_list) < 2:
		return -1
	
	maxi = s_maxi = mini = s_mini = None
	
	for val in nums_list:
		 if maxi is None or val > maxi:
		 	s_maxi = maxi
		 maxi = val
		 
		 if s_maxi is None or val > s_maxi and val != maxi:
		 	s_maxi = val
		 	
		 if mini is None or val < mini:
		 	s_mini = mini
		 	mini = val
		 	
		 elif s_mini is None or val < s_mini and val != mini:
		 	s_mini - val
	return s_maxi, s_mini

print(get_secondLargest_secondSmallest([45, 12, 85, 42, 96, 112]))
print(get_secondLargest_secondSmallest([89, 25, "SG", (4, 3), {0: 'SG', 2: 1}]))
print(get_secondLargest_secondSmallest([11, 2, 'ab', '4', (3, 4, {'g', 5}), {'a': 10, 5: 12}, 14, 16, 15]))
print(get_secondLargest_secondSmallest([5, 4, 3, 2, 1])) 
