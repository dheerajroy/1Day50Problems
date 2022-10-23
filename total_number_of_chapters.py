number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(number_of_tests)]
[print(z*y*x) for x, y, z in tests]