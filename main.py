import random
a = int(input("The range is from: "))
b = int(input("To: "))
r = random.randint(a, b)
c = int(input("Guess a number"))
while True:
  if c == r:
    print("Correct!")
    break
  elif c > r:
    c = int(input("Too high. Guess again: "))
  else:
    c = int(input("Too low. Guess again: "))
