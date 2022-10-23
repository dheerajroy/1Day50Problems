total_number_of_tests = int(input())
tests = [map(int, input().split()) for _ in range(total_number_of_tests)]
[print(sorted(test)[-2]) for test in tests]