# # Deleting popups
# def delete_login_success():
#     login_success_screen.destroy()
#     login_screen.destroy()
#     # hide it by the withdraw() method of the root window.
#     # make the window visible again by the deiconify() (or wm_deiconify()) method.
#     main_screen.withdraw()
#     MainScreen.mainMenu()


# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()