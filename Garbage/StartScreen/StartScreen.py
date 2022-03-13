from tkinter import *
import pyrebase

from EmotionRecognition import EmotionRecognition

config = {
  "apiKey": "AIzaSyBkWxh3HyU8hyeGb77QrLfqei81L_mHuoA",
  "authDomain": "finalproject-50eb9.firebaseapp.com",
  "databaseURL": "finalproject-50eb9",
  "storageBucket": "finalproject-50eb9.appspot.com"
}

#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}


# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Email * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()

# Designing window for login
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

# Implementing event on register button
def register_user():
    username_info = username.get()
    password_info = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    try:
        user=auth.create_user_with_email_and_password(username_info, password_info)
        register_sucess()
    except:
        register_fail()

# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    try:
        user = auth.sign_in_with_email_and_password(username1 ,password1)
        login_sucess()
    except :
        login_fail()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def login_fail():
    global login_fail_screen
    login_fail_screen = Toplevel(login_screen)
    login_fail_screen.title("Login Failed")
    login_fail_screen.geometry("150x100")
    Label(login_fail_screen, text="Wrong email or password").pack()
    Button(login_fail_screen, text="OK", command=delete_login_fail).pack()

def register_sucess():
    global register_success_screen
    register_success_screen = Toplevel(register_screen)
    register_success_screen.title("Success")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text="Registration Success").pack()
    Button(register_success_screen, text="OK", command=delete_register_success).pack()

def register_fail():
    global register_fail_screen
    register_fail_screen = Toplevel(register_screen)
    register_fail_screen.title("Success")
    register_fail_screen.geometry("150x100")
    Label(register_fail_screen, text="Registration Failed").pack()
    Button(register_fail_screen, text="OK", command=delete_register_fail).pack()

def changeRecommendationOrKeepForward():
    global choose_screen
    choose_screen = Toplevel(main_screen)
    center(choose_screen)
    choose_screen.title("Hello There")
    choose_screen.geometry("300x250")
    # Label(recommendations_screen, text="Recommended For You:").pack()
    Button(choose_screen, text="Open Camera For Emotions Recognition", height="2", width="30", command=open_camera).pack()
    Button(choose_screen, text="Change Your Movies List", height="2", width="30", command=change_movies_list).pack()


from PyQt5 import QtWidgets

def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    # screen_width = toplevel.winfo_screenwidth()
    # screen_height = toplevel.winfo_screenheight()

    # PyQt way to find the screen resolution
    app = QtWidgets.QApplication([])
    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))
    toplevel.title("Centered!")


def change_movies_list():
    choose_screen.withdraw()
    global change_movies_screen
    change_movies_screen = Toplevel(choose_screen)
    change_movies_screen.title("Change Movies List")
    change_movies_screen.geometry("300x250")
    Label(change_movies_screen, text="TODO: TBD - Denis").pack()
    Label(change_movies_screen, text="Enter New Movies List").pack()
    Button(change_movies_screen, text="Save And Go Back", height="2", width="30", command=setTheSettingsBeforeDivert).pack()

def setTheSettingsBeforeDivert():
    change_movies_screen.destroy()
    changeRecommendationOrKeepForward()

def open_camera():
    choose_screen.withdraw()
    results = EmotionRecognition.start()
    emotion_recognition_camera_page(results)

def emotion_recognition_camera_page(results):
    global er_camera_screen
    er_camera_screen = Toplevel(choose_screen)
    er_camera_screen.title("Emotions Recognition Page")
    er_camera_screen.geometry("300x250")
    Label(er_camera_screen, text="Emotions Detected:\n" + str(results)).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    # hide it by the withdraw() method of the root window.
    # make the window visible again by the deiconify() (or wm_deiconify()) method.
    main_screen.withdraw()
    changeRecommendationOrKeepForward()

def delete_login_fail():
    login_fail_screen.destroy()

def delete_register_success():
    register_success_screen.destroy()

def delete_register_fail():
    register_fail_screen.destroy()

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Welcome", width="300", height="2", font=("David", 16)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", font=("David", 12), command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", font=("David", 12), command=register).pack()

    main_screen.mainloop()

main_account_screen()