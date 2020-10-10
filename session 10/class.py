from tkinter import *
from tkinter import messagebox

window = Tk()

def popUpMessageBox(text=""):
    messagebox.showinfo("Result",text)


def validateInfo():
    username = userInput.get()
    psw = passwordInput.get()
    result = ''
    if (username == 'mindx'):
        if (psw == '1234'):
            result = 'success'
        else: 
            result = 'wrong'
    showResult(result)

def showResult(result):
    print(result)
    resultLabel = Label(text=result)
    resultLabel.grid(row=4, column = 1)


window.geometry("800x600")

window.title('Form Sign In/Sign Up')


greeting = Label(text="Welcome to my app", bg="red")
greeting.grid(row=0, column=5)

btnSignIn = Button(text="Sign In", bg="green", padx="16", pady="8", command=lambda: [popUpMessageBox('You have clicked'), validateInfo()])

# TODO: Click button to sign in ====> "You have clicked"
userLabel = Label(text="username")
userLabel.grid(row=0, column=0)
userInput = Entry(window, textvariable=StringVar())
userInput.grid(row=0, column=1)

passwordLabel = Label(text="password")
passwordLabel.grid(row=1, column=0)
passwordInput = Entry(window, show = "*", textvariable=StringVar())
passwordInput.grid(row=1, column=1)

btnSignIn = Button(text="Sign In", bg="green", padx="16", pady="8", command=lambda: [validateInfo()])
btnSignIn.grid(row=3, column=12)

window.mainloop()