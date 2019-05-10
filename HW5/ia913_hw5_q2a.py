char = input('Please enter a character: ')

#if char == char.lower():
#    print(char, 'is a lower case letter.')  #turns nonalpha into lower too
#elif char == char.upper():
#    print(char, 'is an upper case letter.')
if char == int(char):
    print(char, 'is a digit.')
else:
    print(char, 'is a non-alphanumeric character.')