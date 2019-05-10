import random
def create_permutation(n):
    lst=[];
    for i in range(n+1):
        compare = random.randint(0,n)
        while compare in lst:
            compare = random.randint(0,n)
        lst.append(compare)
    return lst

def scramble_word(word):
    n = (len(word)-1)
    lst = create_permutation(n)
    scrambled = ''
    for i in lst:
        scrambled=scrambled+word[i]+' '
    return scrambled

def main():
    f = open('hw7 - work bank.txt', 'r')
    lines = f.readlines()
    for f in lines:
        lines = f.strip('\n')
    rand = random.randint(0, len(lines)+1)
    print(lines)
    original = lines[rand]
    scrambled = scramble_word(original)
    print("Unscramble the word: ", scrambled)
    word = input("Try #1: ")
    n=1
    while word != original and n != 3:
        print("Wrong!")
        n+=1
        print("Try #", n)
        word=input("")
    if word == original:
        print("Yay! You got it!")
    f.close()

main()