total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [int(input()) for _ in range(total_number_of_tests)]
[print('YES') if x > 30 else print('NO') for x in tests]