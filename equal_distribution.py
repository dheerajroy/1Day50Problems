total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print('YES') if not (a+b)%2 else print('NO') for a, b in tests]