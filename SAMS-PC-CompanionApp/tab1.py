import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import sv_ttk as sv_ttk
import darkdetect



root = tk.Tk()
root.title("Student Attendance Monitoring System Public Release V0.1")
root.resizable(False, False)
place_h_profile = tk.PhotoImage(file="profile.png")
window_width = 1000
window_height = 600
def side_bar():
    profile = ttk.Label(image=place_h_profile)
    profile.grid(sticky="E",pady=2,padx=2,column=0,row=1)
    acc_name = ttk.Label(text="Personnel Name",font=("Arial",15))
    acc_name.grid(sticky="E",pady=10,padx=0,column=2,row=1)
    role = ttk.Label(text="Class Adviser",font=("Arial",8))
    role.grid(sticky="E",padx=0,column=2,row=2)
    home = ttk.Button(text='Home')
    home.grid(sticky="SE",pady=5)
    settings = ttk.Button(text="Settings")
    settings.grid(sticky="SE",pady=5)

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
side_bar()
root.mainloop()