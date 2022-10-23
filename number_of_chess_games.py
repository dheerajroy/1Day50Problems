total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [int(input()) for _ in range(total_number_of_tests)]
[print(int((n*60)/20)) for n in tests]