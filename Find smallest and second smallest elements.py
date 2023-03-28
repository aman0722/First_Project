import math

def small(arr):

	
	arr_size = len(arr)
	if arr_size < 2:
		print("Invalid Input")
		return

	first = second = math.inf
	for i in range(0, arr_size):

		
		if arr[i] < first:
			second = first
			first = arr[i]

		
		elif (arr[i] < second and arr[i] != first):
			second = arr[i]

	if (second == math.inf):
		print("No second smallest element")
	else:
		print('The smallest element is', first, 'and',
			' second smallest element is', second)



arr = [432, 4313, 3461, 1670, 734, 961]
small(arr)


