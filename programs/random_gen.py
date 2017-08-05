import random

def gen_2():
	if not hasattr(gen_2, "prev"):
		setattr(gen_2, "prev", None)
	num=random.randint(0, 1)
	if gen_2.prev is None:
		gen_2.prev=num
	elif gen_2.prev == num:
		return gen_2()
	else:
		gen_2.prev=num
	return num+1

def gen_3():
	x=random.randint(0,1)
	y=random.randint(0,1)<<2
	return 0|x|y

def gen_5_2():
	x=random.randint(0, 1)
	y=random.randint(0, 1)<<1
	z=random.randint(0, 1)<<2
	num=0|x|y|z
	if num > 5:
		return gen_5()
	return num

def gen_5_3():
	x=gen_3()%2
	y=gen_3()%2<<1
	z=gen_3()%2<<2
	num=0|x|y|z
	if num > 4:
		return gen_5_3()
	return num+1

def gen_7_5():
	num=7*gen_5_3()+gen_5_3()-7
	if num > 21:
		return gen_7_5()
	return num%7+1