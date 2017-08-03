Move to Inbox
 
More 
2 of 50
 
radix sort based solution
Parag <agarwal.parag@gmail.com>
	
AttachmentsJul 31 (2 days ago)
	
to Mohit
Attachments area
	
Click here to Reply or Forward
13.79 GB (13%) of 100 GB used
Manage
Terms - Privacy
Last account activity: 8 minutes ago
Details
	
	
Mohit Goyal's profile photo
	Mohit Goyal
Birla Institute of Technology & Science, Pilani - Goa
Show details

op_list=['/', '*', '-', '+']

def check_operation(v):
	if v not in op_list:
		raise Exception(" Invalid operation : {0}".format(v))
	return True

def do_ops(op, x1, x2):
	if op == '+':
		return x1+x2
	elif op == '-':
		return x1-x2
	elif op == "*":
		return x1*x2
	else:
		return x1/x2

def parse_and_get_operations(input=[]):
	sort_list={x:[] for x in op_list}
	for x in range(len(input)):
		if x%2 == 0:
			if not input[x].isdigit():
				raise Exception(" Invalid number :: {0}".format(input[x]))
		elif check_operation(input[x]):
			sort_list[input[x]].append(x)
	new_list=[]
	for x in op_list:
		new_list+=[[x, index] for index in sort_list[x]]
	return new_list

def calculate(input=[]):
	ops=[]
	# 1st Pass
	ops=parse_and_get_operations(input)
	# 2nd Pass
	total=0
	for x in ops:
		index=x[1]
		operation=x[0]
		num=do_ops(operation, int(input[index-1]), int(input[index+1]))
		input[index]=num
		input[index+1]=num
		input[index-1]=num
	return num

print calculate(['1', '+', '2']), 1+2
print calculate(['1', '+', '2', '/', '2']), 1+2/2
print calculate(['10', '*', '2', '/', '2']), 10*2/2
print calculate(['10', '+', '2', '-', '2']), 10+2-2
print calculate(['10', '-', '2', '*', '2']), 10-2*2
