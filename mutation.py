def mutate_string(string, position, character):
    l = list(string); l[position] = character; return ''.join(l)

if __name__ == '__main__':
    s = input('Enter string: ')
    i, c = input('Enter position and character: ').split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)