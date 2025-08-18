from os import system

system('cls')

try:
    value1:int = int(input("enter first value: "))
    value2:int = int(input("enter second value: "))

    sum:int = value1+value2
    difference:int = value1-value2
    product:int = value1*value2
    quotient:int = value1/value2

    print(f"the sum of {value1} and {value2} is {sum}")
    print(f"the difference of {value1} and {value2} is {difference}")
    print(f"the product of {value1} and {value2} is {product}")
    print(f"the quotient of {value1} and {value2} is {quotient}")
except:
    print("Invalid input")
