import random

charNum = input('how many character do you need?')
chars = input('Which characters do you need to generate?\n1 for number 2 for lower case 3 for upper case 4 for characters\n')

def only_number(num):
    password = ''
    while len(password)<num:
        password += str(random.randint(0, 9))
    return password

def only_lower_case(num):
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'
    password = ''
    while len(password)<num:
        password += lowerCase[random.randint(0, len(lowerCase)-1)]
    return password

def only_upper_case(num):
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''
    while len(password)<num:
        password += upperCase[random.randint(0, len(upperCase)-1)]
    return password

def only_characters(num):
    characters = '!@#$%^&*'
    password = ''
    while len(password)<num:
        password += characters[random.randint(0, len(characters)-1)]
    return password


password = ''
for i in range(len(chars)):
    tempNum = int(charNum)
    if len(password) != 0:
        # half it approximatly
        tempNum = random.randint(1, len(password)//2)
        password = password[:len(password)-tempNum]
    if chars[i] == '1':
        password += only_number(tempNum)
    elif chars[i] == '2':
        password += only_lower_case(tempNum)
    elif chars[i] == '3':
        password += only_upper_case(tempNum)
    else:
        password += only_characters(tempNum)
    #shuffle
    tempList = list(password)
    random.shuffle(tempList)
    password = ''.join(tempList)
print(f'Your password is: {password}')
