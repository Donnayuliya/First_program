s = input().split('-')
print(s)
print(len(s))
if len(s) == 4 and s[0] == '7':
    del s[0]
if len(s) == 3 and ''.join(s).isdigit():
    if len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')