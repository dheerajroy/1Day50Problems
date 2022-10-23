total_number_of_tests = int(input('Enter total number of test cases: '))
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print(x*4 + y*2) for x, y, _ in tests]