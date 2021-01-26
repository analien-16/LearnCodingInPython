# Improve the previous work to allow user to set the range of number, start number and end number
min =int (input("Pick your minimum number value: "))
max =int (input("Put your maximum number value: "))
i = min
sum = 0
while i <= max:
 sum = sum + i
 i += 2
print(sum)
print("Have a good day!")