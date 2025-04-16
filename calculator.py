first = input("Enter the first number: ")
oprator = input("Enter the oprator(+,-,*,/,%,**): ")
second = input("Enter the second number: ")

if oprator == "+":   
    sum = int(first) + int(second)
    print(sum)
elif oprator == "-":
    difference = int(first) - int(second)
    print(difference)
elif oprator == "*":
    product = int(first) * int(second)
    print(product)
elif oprator == "/": 
    division = int(first) / int(second)
    print(division)
elif oprator == "%":
    remainder = int(first) % int(second)
    print(remainder)
elif oprator == "**":
    power = int(first) ** int(second)
    print(power)
else:
    print("Invalid operator")
print("Thank you for using this calculator")
