# Print List
"""
Created on Thu Jul  9 14:32:12 2020
this program gathers user input into a list and then displays it
@author: Jay
"""
print('If you wish to end the program, answer "no" when prompted')
keepGoing = True
listing = []
while keepGoing == True:        
    word = input("Please provide an item for the list: ")
    listing.append(word)
    contq = input("Would you like to keep going?: ")
    if contq=='no':
        keepGoing = False            
                
response = "You provided: "
print(response)
print(listing)
