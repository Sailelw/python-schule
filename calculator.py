
print("calculator")

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
zeichen = input("zeichen: ")

if zeichen == "+":
    result = num1 + num2
if zeichen == "-":
    result = num1 - num2
if zeichen == "*":
    result = num1 * num2
if zeichen == "/":
    result = num1 / num2

print(result)