
def main():
    password = input("Enter password: \n    ")
      
    if (password_check(password)):
        print("Password is valid")
    else:
        print("Invalid Password ")
    return password
    

def password_check(password):
      
    SpecialSym =['$', '@', '#', '%','!','#','&','*','-','_',' ',',','.']
    val = True
    
    if len(password) <15:
        print('    -Length should be greater than 15')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('    -Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('    -Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('    -Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('    -Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

password = main()




  



    




