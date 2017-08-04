

def max_subset_increasing_numbers(array=[]):
	temp=None
	max_sum=None
	for num in array:
		if max_sum is None:
			temp=num
			max_sum=num
		elif temp+num > num:
			temp=temp+num
		else:
			temp=num
		if temp > max_sum:
			max_sum=temp
	return max_sum

print max_subset_increasing_numbers([-2, 4, 1, -1]), 5
print max_subset_increasing_numbers([-2, 4, -1]), 4
print max_subset_increasing_numbers([0, 4, 0]), 4
print max_subset_increasing_numbers([0, 4, 4, 0]), 8
print max_subset_increasing_numbers([10, -1, 4, 100]), 113
print max_subset_increasing_numbers([-1, -1, 4, 100]), 104