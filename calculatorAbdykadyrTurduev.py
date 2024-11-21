import os
a = float(input("Enter number:"))
b = float(input("Enter number:"))

os.system("cls")
select_operation = int(input("1 - Multiplication, 2 - Division, 3 - Subtraction, 4 - Addition. Choose 1-4 :"))

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

if select_operation == 1:
    output = a * b
    operation = "*"
    print (f"{a}{operation}{b}={output}")
elif select_operation == 2:
    output = a / b
    operation = "/"
    print(f"{a}{operation}{b}={output}")
if select_operation == 3:
    output = a - b
    operation = "-"
    print(f"{a}{operation}{b}={output}")
if select_operation == 4:
    output = a + b
    operation = "+"
    print(f"{a}{operation}{b}={output}")
    

    