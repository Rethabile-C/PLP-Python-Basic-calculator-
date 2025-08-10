#ask user to enter first number
num1 = int((input("Enter the first number :")))

#ask user to enter 2nd number 
num2 = int((input("Enter second number :")))

#ask user to enter operation 
operation = input("Enter operation(+, -, *, / ): ")

#calculater results based on the user's choice 

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else :
    result = "invalid operation"

#show results
print("Answer is :", result)