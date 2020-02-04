def register():
    username = input("Please enter your name ")
    password = input("Please input your desired password ")
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")

def login():
    username = input("Please enter your username")
    password = input("Please enter your password")  
    for line in open("accountfile.txt","r").readline(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username+' '+password+'\n'==line:
            print("Correct credentials!")
            print("Welcome")
            return True
    print("Incorrect credentials.")
   
    return False
print("Are you a new user?(Yes/No):")
user=input()
if user == "Yes":
    login()

elif user =="No":
    register()

