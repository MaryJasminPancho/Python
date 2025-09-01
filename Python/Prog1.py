"""
PANCHO, Mary Jasmin S.
19877-ITELECPYTH

    base and exponential program
    ----------------------------
    A program that would compute the exponential,the program accepts two(2) positive integer value not greater 
    than 20, first value would the base and followed by the exponential value,respectively, compute and dispplay 
    the result

example:
base     (1..20): 2
exponent (1..20): 10

2 raise to the power of 10 is 1024
"""

from os import system
system("cls")

try:
    result:int = 1
    
    base:int = int(input("Enter the base number: "))
    if base>0 and base<=20:
        expo:int = int(input("Enter the exponential value: "))
        if expo>0 and expo<=20:
            i = 1
            while i <= expo:
                result = result * base
                i+=1
            print(f"{base} raised to the power of {expo} is {result}")
        else:
            print("exponent should be from 1 to 20")
    else:
        print("Base should be from 1 to 20")

except: print("Invalid input")