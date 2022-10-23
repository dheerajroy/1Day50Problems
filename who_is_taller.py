number_of_inputs = int(input('Enter number of inputs: '))
inputs = [map(int, input().split()) for _ in range(number_of_inputs)]
[print('A') if i>j else print('B') for (i, j) in inputs]