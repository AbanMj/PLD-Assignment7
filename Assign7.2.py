#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex. input: P@ssw0rd+P@ssw0rd, ouput: Valid


password = input("enter password: \n    ")

lower = 0
capital = 0
number = 0
if (len(password) >15 ):
    for i in password:
        if (i.islower()):
            lower+=1 
        if (i.isupper()):
            capital+=1
        if (i.isdigit()):
            number+=1

if (lower >=1 and 
    capital >= 1 and 
    number >=1 ):
    print ("valid")
else:
    print("invalid")