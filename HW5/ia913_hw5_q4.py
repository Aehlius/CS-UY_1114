word = input('Enter a word: ')

vowel = 0
consonant = 0

for i in range(0, +1):  #find string length
    let = word[i]
    if let == 'a' or let == 'e' or let == 'o' or let == 'i':
        vowel += 1
    else:
        consonant += 1

print(word, 'has', vowel, 'vowels and', consonant, 'consonants')