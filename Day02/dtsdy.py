#Ask the user to enter two numbers as input,
# convert them to int, and print their sum,
# difference, product, and division result

num1=input("Enter First Number:")
num2=input("Enter Second Number:")

n1=int(num1)
n2=int(num2)

print("Choose any one(+,-,*,/)")

op=input("Enter Operator:")

match op:
    case "+":
        print("Result:",n1+n2)

    case "-":
        print("Result:",n1-n2)

    case "*":
        print("Result:",n1*n2)

    case "/":
        print("Result:",n1/n2)

    case _:
        print("invalid.....")




