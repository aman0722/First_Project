
def BS(arr):
    n = len(arr)
    
    swapped = False
   
    for i in range(n-1):
        
        for j in range(0, n-i-1):
 
            
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
           
            return
 
    def display(arr):
        print("Bubble Sort")

arr = [2624, 33244, 2544, 351562, 4324342, 31531, 690]
 
BS(arr)
 
print("Sorted array is:")
display(arr)
BS(arr)
print("after Bubble Sort")
display(arr)