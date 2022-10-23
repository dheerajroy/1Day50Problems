def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i: i+k]
        final_string = []
        for j in s:
            if j not in final_string:
                final_string.append(j)
        print(''.join(final_string))
    
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)