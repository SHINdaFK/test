# # 4.1
# username = input("Enter your name: ")
# email = input("Enter your email: ")
# password = input("Enter your password: ")

# # 4.2
# password = input("Enter your password: ")
# repassword = input("Enter your password again: ")
# if ("@" in email) and (len(password) >= 8):
#     if (repassword == password):
#         print("Sign up success")
#         isDone = False
#     else:
#         print("Wrong password")
# else:
#     print("Password need to have atleast 8 Character")

# # 4.3 Case Login
# userInput = input("Enter your name: ")
# if ("@" in userinput) and (len(userInput) >= 8):

# while True:
#     userInput = input("Enter your name: ")
#     userpassword = input("Enter your password: ")
#     CorrectEmail = "gmd10116s@gmail.com"
#     CorrectPassword = "TuannguyeN"

#     if ("@" in userinput) and (len(userInput) >= 8):
#         if userInput == CorrectEmail:
#                 if userpassword == CorrectPassword
#             print("Login Success")
#             break
#         else:
#             print("Login Fail")

# 4.3 Case Signup
isDone = True

while isDone:
    email = input("Enter your email: ")
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    repassword = input("Reenter password: ")

    if ("@" in email) and (len(password) >= 8):
        if (repassword == password):
            print("Sign up success")
            isDone = False
        else:
            print("Wrong password")
    else:
        print("Password need to have atleast 8 Character")