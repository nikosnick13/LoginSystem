
from distutils.log import error

def register():
    db = open("Database.txt" , 'r')
    Username = input("Great your username:")
    Password = input("Great a password:")
    AthedicationPass = input("Confirm your password:")
    l=[]
    d=[]
    for i in db:
        a,b = i.split(', ') 
        b = b.strip() 
        l.append(a)
        d.append(b)
        data= dict(zip(l,d))


    if Password != AthedicationPass:
        print("The password don't match. pleace try again")
        register()
    else:
        if len(Password) < 6:
            print("This is week password try more characters")
            register()
        elif Username in l:
            print("This username is already exist!!")
            register()
        else:
            db = open("Database.txt",'a')
            db.write(Username+", "+Password+"\n")
            print("Succes login!!!!!")

def access():
    db = open("Database.txt" ,'r')
    Username = input("Enter your username:")
    Password = input("Enter your password:")
    #tsekaroume an o xristis exei simplirosi panw apo ena stixio sto username i sto password 
    if not len(Username or Password) < 1:
        l=[]
        d=[]
        for i in db:
            a,b = i.split(', ') 
            b = b.strip()             
            l.append(a)
            d.append(b)
        data= dict(zip(l,d))
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login Success!!!")
                        print("Hi " +Username)
                    else:
                        print("Password or Username is not correct")
                except:
                    print("Your Username or Password is incorect")
            else:
                print("Username doesn't exist")        
        except:
            print('Login Error')
    else:
        print("Type a value")


def home(option = None ):
    option = input("Login | Sing Up:")
    if option.lower() == "login":
        access()
    elif option.lower() == "sing up":
        register()
    else:
        print("Enter a option")

home()
