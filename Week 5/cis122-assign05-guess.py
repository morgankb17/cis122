'''
CIS 122 Summer 2020 Assignment 5
Author: Morgan Bartlett
Credit:
Description: Program that is a word guessing game
'''

fail_list = ''
guess_list = ''
guess_word = ''
guess_count = 0
# prompt user for guess word
word = input("Enter a guess word (blank to quit): ") 
# if no word is entered, quit the program

# keep prompting user for letters until all the letters are found
while True:
    
    # prompt user for guess letter
    guess = input("Enter a guess letter (blank to quit): ")
    # if no word is entered, quit the program
    if guess == '':
        break
        
    # check to see if guess letter has already been guessed    
    if guess in fail_list:
        print('\t','>',guess, 'already guessed and not found')
        print('\t','>','Guesses so far:', fail_list)

    # check to see if guess letter has already been guessed and found
    elif guess in guess_list:
        print('\t','>',guess,'already guessed and found')
        print('\t','>','Guesses so far:', fail_list)
        
    # check to see if guess is more than one letter
    elif len(guess) != 1:
        print('\t','>','Only enter a single letter')
        
    # check to see if guess does not match a letter in the word
    elif guess not in word:
        print('\t','>',guess, 'not found')
        fail_list += guess
        guess_count += 1
        print('\t','>','Guesses so far:', fail_list)
        
    # check to see if guess letter matches a letter in the word
    for i in word:
        if guess == i and guess not in guess_list:
            print('\t','>',guess,'found')
            guess_list += guess
            fail_list += guess
            guess_count += 1
            print('\t','>','Guesses so far:', fail_list)
        elif guess in guess_list:
            print('\t','>','All letters found')
            break
        
print('*** Results ***')
print('Word: \t', word)
print('Matched: \t', guess_list)
print('Unmatched: \t', fail_list)
print('Guesses: \t', guess_count)
