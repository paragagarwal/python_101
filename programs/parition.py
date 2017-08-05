def partition(array=[]):
	l_index=0
	pivot=array[len(array)-1]
	x=0
	y=len(array)-2
	while(x<y):
		if array[x] > pivot and array[y] <= pivot:
			temp=array[x]
			array[x]=array[y]
			array[y]=temp
			x+=1
			y-=1
		else:
			if array[x] < pivot:
				x+=1
			if array[y] >= pivot:
				y-=1
	if(pivot < array[x]):
		temp=array[x]
		array[x]=pivot
		array[len(array)-1]=temp
	return array