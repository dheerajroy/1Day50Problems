number_of_inputs = int(input('Enter number of inputs: '))
inputs = [int(input()) for _ in range(number_of_inputs)]
[print('YES') if i>=30 else print('NO') for i in inputs]