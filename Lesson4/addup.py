num = int(input("Pick a number to add up all the even numbers less than it: "))
def addup(num):
  if num == 1:
    return 1
  else:
    return num + addup(num - 1)


print(addup(num))
