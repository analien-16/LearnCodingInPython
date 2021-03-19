random = int(input("Pick a number you would like to multiply up to: "))

def factorial(random):
  print(random)
  if random == 0:
    return 1
  elif random == 1:
    return 1
  else:
    return factorial(random - 1) * random

print(factorial(random))