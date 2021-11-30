#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex. input: P@ssw0rd+P@ssw0rd, ouput: Valid

psswrd = input("Enter password: \n    ")
lower=0
capital=0
numb=0
special=0

if len(psswrd)>15:
    for char in psswrd:
        if (char.islower()):
            lower=lower+1

        if (char.isupper()):
            capital=capital+1

        if (char.isdigit()):
            numb=numb+1

        if (char=='$'or char=='@' or char=='#' or char=='%' or char=='!' or char=='#' or char=='&'
        or char=='*' or char=='-' or char=='_' or char==' ' or char==',' or char=='.'):
            special=special+1

if (lower>=1 and capital>=1 and numb>=1 and special>=1 and lower+capital+numb+special==len(psswrd)):
    print("    -Valid Password")
else:
    print("    -Invalid Password")
