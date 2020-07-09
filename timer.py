# timer
"""
Created on Thu Jul  9 14:03:17 2020
Print out a timer between a start and end time
@author: Jay
"""
import time 
# # time it takes to run the program
# techAnswer = time.thread_time() 
# print(techAnswer)

#stopwatch with user interface
startT = time.monotonic()
input("Press Enter to continue:")
endT = time.monotonic()

finaltime = endT - startT
print(finaltime)