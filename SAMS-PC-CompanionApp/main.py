import tkinter as tk 
from tkinter import ttk
from time import sleep
import sv_ttk as sv_ttk



root = tk.Tk()
icon = tk.PhotoImage(file="icon.png")
window_width = 650
window_height = 350
root.title("SAMS Public Release V0.1")
root.resizable("false", "false")
root.iconphoto(True,icon)
def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    """Citations: https://pythonprogramming.altervista.org/how-to-center-your-window-with-tkinter-in-python/"""
center_screen()
def timed():
    import time
    global timeval,intify
    timeval=time.strftime("%S",time.localtime())
    intify = int(timeval)



def prog():
    progressbar = ttk.Progressbar(length=250,maximum=100)
    progressbar.place(y=145,x=75)    
    progressbar.step(1)
    progressbar.after(1000,prog)
timed()

def leave():
    root.quit()
def get_id():
    from acc import connect_to_db 
    pas = password.get()
    print("Password: ",pas)
    ush = user.get()
    print("Username: ",ush)
    error_1 = tk.Tk()
    error_1.title("Error")
    error_1.resizable("false","false")
    window_height = 100
    window_width = 500
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = error_1.winfo_screenwidth()
        screen_height = error_1.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        error_1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        """Citations: https://pythonprogramming.altervista.org/how-to-center-your-window-with-tkinter-in-python/"""            
    if pas == "":
            center_screen()
    if ush == "":
            center_screen()
    if pas and ush != "":
         connect_to_db()
         error_1.destroy()

def signup():
    global welcome,thanks,u_Signup,u_signup_label,p_label,p_signup,p_signup_label,confirm,confirm_pas,confirm_pas_entry,Submit,ret
    Logo.destroy()
    ver.destroy()
    Signup.destroy()
    Signin.destroy()
    quit_prg.destroy()
    welcome = ttk.Label(text="Welcome!",font=("Arial",14))
    welcome.pack(pady=5)
    thanks = ttk.Label(text="Thank you for using SAMS",font=("Helvetica",14))
    thanks.pack(pady=10)
    u_Signup = ttk.Entry()
    u_signup_label = ttk.Label(text="Username")
    u_Signup.pack()
    u_signup_label.pack()
    p_signup = ttk.Entry()
    p_signup_label = ttk.Label(text="Password")
    p_signup.pack()
    p_signup_label.pack()
    confirm_pas_entry = ttk.Entry()
    confirm_pas_entry.pack()
    confirm_pas = ttk.Label(text="Confirm Password")
    confirm_pas.pack()
    Submit = ttk.Button(text="Submit")
    Submit.pack()
    ret = ttk.Button(text="Return",command=ret_to_startup)
    ret.pack(pady=5)
def ret_to_startup():
     ret.destroy()
     Submit.destroy()
     confirm_pas.destroy()
     confirm_pas_entry.destroy()
     p_signup_label.destroy()
     p_signup.destroy()
     u_signup_label.destroy()
     u_Signup.destroy()
     thanks.destroy()
     welcome.destroy()
     at_startup()


     
def login():
    global u_label,p_label,password,user,ret,confirm
    Logo.destroy()
    ver.destroy()
    Signup.destroy()
    Signin.destroy()
    quit_prg.destroy()
    u_label = ttk.Label(text="Username:")
    u_label.pack(pady=2)
    user = ttk.Entry()
    user.pack(pady=2)
    p_label = ttk.Label(text="Password")
    p_label.pack(pady=2)
    password = ttk.Entry()
    password.pack(pady=2)
    confirm = ttk.Button(text="Confirm",command=get_id)
    confirm.pack(pady=2)
    ret = ttk.Button(text="Return",command=del_login)
    ret.pack(pady=2)
log_o = tk.PhotoImage(file='Logo.png')
def at_startup():
    sv_ttk.set_theme("dark")
    global Logo,Signin,Signup,t_or,quit_prg,ver
    Logo = ttk.Label(image=log_o)
    Logo.pack(pady=5)
    Signup =ttk.Button(text="Sign Up",command=signup)
    Signup.pack(pady=5) 
    Signin =ttk.Button(text="Sign In",command=login)
    Signin.pack(pady=5)
    quit_prg = ttk.Button(text="Quit Program",command=leave)
    quit_prg.pack(pady=5)
    version_info = "V0.1 Public Github Release - Currently Running The Latest Version of SAMS"
    ver = ttk.Label(text=version_info)
    ver.pack()
at_startup()
def del_login():
    confirm.destroy()
    u_label.destroy()
    p_label.destroy()
    user.destroy()
    password.destroy()
    ret.destroy()
    at_startup()

def run():
    root.mainloop()
run()