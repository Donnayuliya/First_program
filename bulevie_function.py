# объявление функции
def is_valid_password(password):
    i = 0
    s1 = []
    count = 0
    while password[i] != ':':
        s1.append(password[i])
        i += 1
    str1 = s1[::-1]
    if s1 == str1:
        count += 1
    else:
        return 'False1'
    s2 = []
    i += 1
    while password[i] != ':':
        s2.append(password[i])
        i += 1
    str2 = int(''.join(s2))
    for j in range (2,str2):
        if str2 % j == 0 or str2 == 1 or str2 == 0:
            return 'False2'
    count += 1
    return i
    
print(is_valid_password('11111:71:90000'))