

num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


#Using Recersive Function

def Series(i):
    if i <= 1:
      return i
    else:
       return (Series(i - 1) + Series(i - 2))

num=10
if num <=0:
   print(" Enter a Positive Number")
else:
   print("Fibonacci Series:", end=" ")
for i in range(num):
   print(Series(i), end=" ")
