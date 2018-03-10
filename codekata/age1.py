#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      RGCET
#
# Created:     10/03/2018
# Copyright:   (c) RGCET 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def age():
    age = int(input("Enter your age:"))
    if(age < 20):
        print("You are a minor and not eligible")
    elif(age >= 20):
        print("you are eligible")

age()