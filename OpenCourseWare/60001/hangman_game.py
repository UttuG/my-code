# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:16:08 2020

@author: Stalik
"""


swlist=[]
swlist2=[]

check=int(0)
secret_word=input("secret word:")
guessnum=int(input("Number of guesses you want:"))
letters_guessed = []
l=len(secret_word)
print("the length of the serect word is",l)
swlist[:]=secret_word
swlist2[:]=swlist

for i in range(guessnum):
    guess=input("Guess the letter in the secret word:")
    guessnum -=1
    for word in swlist:
        if word==guess:
            letters_guessed.append(guess)
            print("Got",guess,"right!")
            l -= 1
            print("Remaining letters to guess:",l)
            print("Number of guesses remaining:",guessnum)
            check=1
            swlist.remove(guess)
            break
    
        print("Wrong choice!")
        print("Remaining letters to guess:",l)
        print("Number of guesses remaining:",guessnum)
       
    letters_guessed.sort()
    swlist2.sort()
    if letters_guessed==swlist2:
        print("You have Guessed the word!")
        break
    
if check==0:
    print("You have exceeded the no. of guesses!")

          
 
                
            
            
            
            
            
            
            