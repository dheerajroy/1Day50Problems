total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [dict(zip(map(int, input().split()), ['Alice', 'Bob', 'Charlie'])) for _ in range(total_number_of_tests)]
[print(test[max(test.keys())]) for test in tests]