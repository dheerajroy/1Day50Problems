number_of_inputs = int(input('Enter the number of inputs: '))
inputs = [int(input()) for _ in range(number_of_inputs)]
[print(i-10) if i > 100 else print(i) for i in inputs]