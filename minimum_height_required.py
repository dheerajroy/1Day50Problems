number_of_inputs = int(input())
inputs = [map(int, input().split()) for _ in range(number_of_inputs)]
[print('YES') if x>=h else print('NO') for (x, h) in inputs]