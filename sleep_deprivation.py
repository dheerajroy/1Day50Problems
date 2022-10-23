number_of_inputs = int(input())
inputs = [int(input()) for _ in range(number_of_inputs)]
[print('YES') if time<7 else print('NO') for time in inputs]