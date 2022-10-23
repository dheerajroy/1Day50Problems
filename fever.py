number_of_inputs = int(input())
inputs = [int(input()) for _ in range(number_of_inputs)]
[print('YES') if temp>98 else print('NO') for temp in inputs]