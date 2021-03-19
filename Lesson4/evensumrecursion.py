# get user's input
num = int(input("Pick a number to add up all the even numbers less than it: "))
def addup(num):
  if num == 2:
    return 2
  elif num % 2 == 0:
    return num + addup(num - 2)
  else:
      return addup(num - 1)
print(addup(num))
