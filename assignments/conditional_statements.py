#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      RGCET
#
# Created:     10/03/2018
# Copyright:   (c) RGCET 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    total=80
    if(total<100 and total >75):
        print(" distinction")
    elif(total<75 and total>50):
        print(" first class")
    else:
        print("failed")

if __name__ == '__main__':
    main()
