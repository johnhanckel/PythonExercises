# printCheck
"""
Created on Thu Jul  9 14:21:13 2020
this program will check to see if the user provided a word/phrase
@author: Jay
"""
def printCheck():
    word = input("Please provide a word or phrase: ")
    if word.isdigit():
        print("THAT'S NOT A WORD! LIAR!")
        printCheck()
    else:
        response = "You provided: "
        print(response + word)

