def divide(input1, input2, result):
        if input2 == 0:
            raise ValueError("Cannot divide by zero.")
        else:
              result = input1 / input2
        return result
        print(result)
