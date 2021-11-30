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
    for i in psswrd:

        if (i == 'a' or i == 'b' or i == 'c' or i == 'd'or i=='e' or i == 'f' or i == 'g' or i == 'h' or i=='i'or i == 'j' or i == 'k' or i == 'l' or 
        i == 'm' or i == 'n' or i=='o' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i=='u' or i == 'v' or i == 'w' or 
        i == 'x' or i == 'y' or i == 'z'):
            lower=lower+1
        
        if (i == 'A' or i == 'B' or i == 'C' or i == 'D' or i=='E' or i == 'F' or i == 'G' or i == 'H' or i=='I' or i == 'J' or i == 'K' or i == 'L' or 
        i == 'M' or i == 'N' or i=='O' or i == 'P' or i == 'Q' or i == 'R' or i == 'S' or i == 'T' or i=='U' or i == 'V' or i == 'W' or 
        i == 'X' or i == 'Y' or i == 'Z'):
            capital=capital+1

        if (i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' ):
            numb=numb+1

        if (i=='!' or i=='@' or i=='#' or i==' ' or i=='%' or i=='&' or i=='*' or i==',' or i=='.'or i=='-'or i=='_'):
            special=special+1

if (lower>=1 and capital>=1 and numb>=1 and special>=1 and lower+capital+numb+special==len(psswrd)):
    print("    -Valid Password")
else:
    print("    -Invalid Password")

        