total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print(k*7-x) for k, x in tests]