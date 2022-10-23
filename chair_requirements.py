total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print(x-y) if x>y else print(0) for x, y in tests]