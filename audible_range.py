number_of_inputs = int(input('Enter the number of inputs: '))
inputs = [int(input()) for _ in range(number_of_inputs)]
[print('YES') if 67<=i<=45000 else print('NO') for i in inputs]