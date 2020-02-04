def login():
    name = input("Please enter your name: ")
    email = input("Please enter your Email-id: ")
    while(email.endswith("@gmail.com")):
        if(email.endswith("@gmail.com")):
            password = input("Create a password: ")   
            confirm = input("Confirm password:")
            if(password==confirm):
                print("Login successful")
            else:
                print("Password doesnt match pls enter valid passwd")
        else:
            print("Please enter the valid email id")
        
login()
print ("Your login details have been saved. ")