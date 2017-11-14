#SAC Rate Calculator
#This program will calculate your air consumption rate for scuba diving
#Made by Tom Knudsen - post@tknudsen.com
#License is open source

import os
import time

os.system('cls')
print('***********************************')
print('***********************************')
print('**********SAC Calculator***********')
print('****************by*****************')
print('************Tom Knudsen************')
print('***********************************')
print('***********************************')
time.sleep(3)
os.system('cls')
print('Welcome to the SAC calculator')
time.sleep(3)

# This code is to first determain the air consumption in bar)
print('First we need to calculate your air consumption in bar')
time.sleep(2)
os.system('cls')
tankVolum = int(input('How large is your tank in litres? :'))
startBar = int(input('Please enter your start pressure in BAR: ')) #starting pressure with full cooled tank
endBar = int(input('Please enter your end pressure in BAR: ')) #ending pressure with cooled tank
totalBar = startBar - endBar 
time.sleep(2)
os.system('cls')
print('Thank you, your total pressure used is: ') #feedback to the user
print(totalBar)
time.sleep(4)
os.system('cls')
# Input to calculate air consumption in litres
print("Let's now see how much air concumption in litre you have used!")
time.sleep(3)
os.system('cls')
print('First we need to know a little bit about your dive :')
time.sleep(2)
depth = int(input('How deep was your dive in meter? :'))
time.sleep(2)
diveTime = int(input('How long was your dive in minutes? :'))
time.sleep(2)
os.system('cls')
print('Let me calculate, please wait...')
time.sleep(3)

#This checks input from the user and assign a atmosphearic pressure value to the answer

depth_total = None
if depth <10 :
    depth_total = 2
elif depth <=20:
        depth_total = 3
elif depth <=30:
    depth_total = 4
else:
    print('You need to enter a depth between 0 and 40 meter')

# This will calculate the total air consumption in litres. 
sacTotal = tankVolum * totalBar / diveTime / depth_total
print('Your air consumption in litre per minute is :')
time.sleep(3)
print(round(sacTotal, 2))
