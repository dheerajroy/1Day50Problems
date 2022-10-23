number_of_test_cases = int(input('Enter total number of test cases: '))
inputs = [map(int, input().split()) for _ in range(number_of_test_cases)]
[print(x*10 + y*90) for x, y in inputs]