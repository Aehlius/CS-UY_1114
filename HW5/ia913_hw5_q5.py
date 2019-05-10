ps = input('Please enter a password')

upper = 0
lower = 0
digit = 0
special = 0

for i in range (0, strlen+1):





if upper > 1 and lower > 0 and digit > 1 and special > 0:
    print(ps, 'is a valid password.')
else:
    print(ps, 'is not a valid password.')