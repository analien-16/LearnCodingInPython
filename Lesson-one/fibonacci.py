# Write a program to generate the Fibonacci series up to a number
a, b = 0, 1
x = int (input("What is the last term you would like to display up to? " ))
print (0,1,end=' ')
while True:
  c = a + b
  a = b
  b = c
  if  c > x: break
  print(c, end=' ') 

