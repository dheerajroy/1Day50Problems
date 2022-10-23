number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(number_of_tests)]
[print(y-x) if y>x else print(0) for x, y in tests]