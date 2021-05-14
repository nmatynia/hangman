import random
import string

def underscored_word(word):
    guess_word = []
    for letter in word:
        guess_word.append("_")
    return guess_word

def checker(user_choice,word,guess_word_arg = []):
    if(user_choice in word):
        while user_choice in word:
            guess_word_arg[word.index(user_choice)] = user_choice
            word[word.index(user_choice)] = '1'
        return guess_word_arg
    else:
        return None

def play_again():
    play_again_question = input("Would you like to play another game? Yes or No?")
    if(play_again_question.capitalize() == "No"):
        return 0
    elif play_again_question.capitalize() == "Yes":
        return 1
    else: 
        print("Yes or No? :D") 
        play_again()

def alphabet_func(alphabet_arg,user_choice = ''):
    alphabet_arg.remove(user_choice)
    return alphabet_arg


words = ["jeremy","szklanica","bartosh","polska","zajebistyjestes","slowo","range","merc","schemat"]
while True:
    lives = 9
    word = []
    word[:0] = random.choice(words)
    alphabet = [] 
    alphabet[:0] = string.ascii_lowercase
    holder = -1
    wincheck = []

    guess_word = underscored_word(word)
    print(guess_word)

    for i in range(len(word)):
        wincheck.append('1')

    while lives != 0:
        print(f"Choices you have:{alphabet}")
        user_choice = input('Enter letter:').lower()

        while user_choice not in alphabet:
            print("You already used this letter! Try another one")
            user_choice = input('Enter letter:').lower()

        alphabet = alphabet_func(alphabet,user_choice)
        holder = checker(user_choice,word,guess_word)

        if(holder == None):
            lives -= 1
            print(f"You have {lives} lives left!")
        else:
            print(holder)

        if(word == wincheck):
            print("You won!")
            break
        print("-----------------------------------------------------------------")
    if(play_again()==0):
        print("Thank you for playing!")
        break
    else:
        pass
