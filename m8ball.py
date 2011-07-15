#!/usr/bin/env python3.2
"""
m8ball.py
name:Cythes
Problem:Get the system to print a fortune based on 1-6 number generation
Target Users: Myself and those poor souls who stumble upon
Target System: GNU/LINUX 
Functional Requirements:
    -User enters text to be decided
    -Program uses a dice roll to determine a number between 1-6
    -Program then tells a message based on the resulting number
    -User can then exit out of the program
Testing: A simple test run expecting an answer to a question.
Maintainer:Cythes
"""
#import random
import random
#User enters a statement.
tell = input("Your question? ")
#Beginning of the dice process
die = random.randint(1, 6)
if die == 1:
    print("Answer not presently availible: Ask later")
if die == 2:
    print("My reply is no")
if die == 3:
    print("Signs point to yes")
if die == 4:
    print("Outlook good")
if die == 5:
    print("Dont count on it.")
if die == 6:
    print("As I see it: yes")
exit = input("Press enter to exit the program. Dont forget your Cthulhu on the way out :)")
#this case is closed!


