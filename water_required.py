number_of_tests = int(input('Enter total number of test cases: '))
tests = [int(input()) for _ in range(number_of_tests)]
[print(n*2) for n in tests]