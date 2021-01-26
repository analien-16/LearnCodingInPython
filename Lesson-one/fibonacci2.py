# Write a program to generate the Fibonacci series, which has specified terms by user
x = int (input("What is the number of terms of the Fibonacci series you want to display? "))
a, b = 0, 1
print (0,1,end=' ')
for x in range(x-2):
  c = a + b
  a = b
  b = c
  print(c, end=' ') 

 