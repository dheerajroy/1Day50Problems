def swap_case(s):
    return ''.join([i.upper() if i.islower() else i.lower() for i in s])

if __name__ == '__main__':
    print(swap_case('this is some TEST TexT'))