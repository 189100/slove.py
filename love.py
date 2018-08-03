#love calculator
#input your name in first line and  lover's name in second
import os
import random

love = random.randint(40, 100)

name1 = input()#enter your name
name2 = input()#enter your partner's name'

print(love)
print("percentage")

if love <= 50:
    print("Still there is chances")
    
if love > 50 and love <= 60:
    print("Made for each other")
    
if love > 60 and love <= 75:
    print("perfect couples")
    
if love > 75:
    print("even  death can't seperate your relation'")
