"""
PANCHO, Mary Jasmin S.
19877-ITELECPYTH

A program that would accept one(1) integer value not greater than 20, compute the factorial of the value

iterative solution

example:
input(1..20): 5
120

"""

from os import system
system("cls")

try: 
    n:int = int(input("Input value (1...20): "))
    if n>0 and n<=20:
        fact = 1
    else:
        print("Accept only 1 to 20")

    while n>0:
        fact = fact * n
        n-=1
    print(fact)

except:
    print("Invalid input")