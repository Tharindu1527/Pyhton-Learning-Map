def calculator():
    print("Calculator")

    try:
        num1 = float(input("Enter Number1: "))
        operator = input("Enter operator(+,-,*,/): ")
        num2 = float(input("Enter Number2: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0 :
                result = num1 / num2
            else:
                return "Error"
        else:
            return "Invalid operator"
        
        return f'{num1}{operator}{num2} = {result}'
    except ValueError:
        return "Error: Please enter valid numbers"
    
# Calling function
print(calculator())
