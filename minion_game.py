def minion_game(string):
    kev = 0
    stu = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            kev += (len(s)-i)
        else:
            stu += (len(s)-i)

    if kev > stu:
        print("Kevin", kev)
    elif kev < stu:
        print("Stuart", stu)
    else:
        print("Draw")
    
            
if __name__ == '__main__':
    s = input('Enter string: ')
    minion_game(s)