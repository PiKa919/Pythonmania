#Ankit Das
#SE4A
#Roll no: 10
#Write a python program that takes any word and changes all occurrences of vowels to the next vowel (cyclically) using function:
def next_vowel(word): #function definition
    vowels = 'aeiou'    #vowels
    new_word = ''
    for letter in word: #loop to check each letter
        if letter in vowels:    #if letter is vowel
            index = vowels.index(letter)    #index of vowel
            next_index = (index + 1) % len(vowels)  #next index of vowel
            new_letter = vowels[next_index] #next vowel
            new_word += new_letter  #new word
        else:   
            new_word += letter  #if letter is not vowel
    return new_word #return new word

word = input("Enter a word: ")
print("Next vowel word:", next_vowel(word))


