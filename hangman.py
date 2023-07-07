#!/usr/bin/python3
import random, numpy as np
wordlist = ["Yourmom","Computer","banana"]

    
wrongchoices = 0
userguesses = []

class play():
    
    
    
    game = False
    word = random.choice(wordlist) #picking a random word from the list of words for the user to guess.
    def printcheck(wrongchoices):
        if wrongchoices == 0:
            print("+-----+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
        if wrongchoices ==1:
            print("+-----+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
        if wrongchoices ==2:
            print("+-----+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
        if wrongchoices ==3:
            print("+-----+\n  |   |\n  O   |\n / \  |\n      |\n      |\n=========")
        if wrongchoices ==4:
            print("+-----+\n  |   |\n  O   |\n /    |\n      |\n      |\n=========")
        if wrongchoices ==5:
            print("+-----+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
        if wrongchoices ==6:
            print("+-----+\n  |   |\n      |\n      |\n      |\n      |\n=========")
            game = True
            print("You lost. Game Over.")
    
    printcheck(wrongchoices)
    print()

    prev= ""
    for letter in word:
            print('_', end = "")
    while game == False:
        print()
        printcheck(wrongchoices)
        userguess = input("Enter a letter and guess the word: ")
        userguesses.append(userguess)
        temp = ""
        for letter in word:
            if userguess == letter in word:
                # print(userguess, end = '')
                temp += userguess 
            elif letter not in userguesses:
                # print("_",end='')
                temp += "_" 
            elif (letter in userguesses):
                # print(letter)
                temp += letter 
                # prev = letter
                # print(f"Prev: {prev}")
            
        print(temp)

        if userguess not in word:
            wrongchoices += 1
            
        if word in temp:
            print("You win")
            game = True
    


play()