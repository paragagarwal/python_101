import random

def swap(array, x, y):
	temp=array[x]
	array[x]=array[y]
	array[y]=temp

def random_partition(array=[]):
	index=random.randint(0, len(array)-1)
	swap(array, index, len(array)-1)
	return partition(array)

def partition(array=[]):
	if array is None or len(array) == 1:
		pass
	pivot=array[len(array)-1]
	x=0
	y=len(array)-2
	while(x<y):
		if array[x] > pivot and pivot >= array[y]:
			swap(array, x, y)
			x+=1
			y-=1
		else:
			if array[x] < pivot:
				x+=1
			if array[y] >= pivot:
				y-=1
			
	if(pivot < array[x]):
		swap(array, x, len(array)-1)
	return array	