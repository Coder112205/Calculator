def addition(input1, input2, result):
    result = input1 + input2
    return result
    print(result)


def subtraction(input1, input2, result):
    result = input1 - input2
    return result
    print(result)

def multiplication(input1, input2, result):
    result = input1 * input2
    return result
    print(result)
    
def divide(input1, input2, result):
        if input2 == 0:
            raise ValueError("Cannot divide by zero.")
        else:
              result = input1 / input2
        return result
        print(result)

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))
switch = input("Enter the operation (+, -, *, /): ")
if switch == "+":
    result = addition(input1, input2, 0)
    print("The result of addition is:", result)
elif switch == "-":
    result = subtraction(input1, input2, 0)
    print("The result of subtraction is:", result)
elif switch == "*":
    result = multiplication(input1, input2, 0)
    print("The result of multiplication is:", result)
elif switch == "/":
    result = divide(input1, input2, 0)
    print("The result of division is:", result) 
