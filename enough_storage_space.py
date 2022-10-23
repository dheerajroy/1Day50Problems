total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print('YES') if n >= x + y*2 else print('NO') for n, x, y in tests]