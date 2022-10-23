number_of_inputs = int(input('Enter total number of test cases: '))
inputs = [map(int, input().split()) for _ in range(number_of_inputs)]
[print('YES') if k>n else print('NO') for n,k in inputs]