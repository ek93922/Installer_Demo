import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image # pip install Pillow
import os
from subprocess import Popen
import sys
import sqlite3

# ------------------------------------------------------------------------------------------------------#
root = Tk()

# Define screen width and height
ws = root.winfo_screenwidth() / 3
hs = root.winfo_screenheight() / 4

# Define window width and height
w = 300
h = 500


# ------------------------------------------------------------------------------------------------------#
# Sets the Folder the Application is Executed as Root/Base Folder
dir_root = os.path.dirname(__file__)


# ------------------------------------------------------------------------------------------------------#
# Databases

# Path to database 
db_info = os.path.join(dir_root, 'Resources', 'info.db')

# Connect to info.db
conn = sqlite3.connect(db_info)
c = conn.cursor()

# Selects table that stores password value
c.execute('SELECT * FROM login_info')
# Changes the value to string
db_password = str((c.fetchone())[0])

# Close Connection
conn.close()

# ------------------------------------------------------------------------------------------------------#
# Create Login Window
top = Toplevel()
top.title('Login')
# Opens a window with dimension of 300x450 at screen coordinate of 300, 200
top.geometry('%dx%d+%d+%d' % (w, h, ws, hs))
# Prevents the user from resizing the window
top.resizable(False, False)
# Login window will always be the top window
top.attributes("-topmost", True)

password_label = Label(top, text="Password")
password = Entry(top, show="*") 
# Password Submit Button
submit_btn = Button(top, text="Login", command=lambda:login())
# Terminates the process
quit_btn = Button(top, text="Quit", command=lambda:quit())

password_label.grid(row=1, column=0)
password.grid(row=1, column=1,padx= 10, pady=20, columnspan=10)
submit_btn.grid(row=2, column=1)
quit_btn.grid(row=2, column=2)

def login():
    if password.get() == db_password:
        #
        root.deiconify()
        top.destroy()

def quit():
    top.destroy()
    root.destroy()
    sys.exit()


# ------------------------------------------------------------------------------------------------------#
root.title("Program Installer")
# Opens a window with dimension of 300x450 at screen coordinate of 300, 200
root.geometry('%dx%d+%d+%d' % (w, h, ws, hs))
# Prevents the user from resizing the window
root.resizable(False, False)
# Installer will always be the top window
root.attributes("-topmost", True)


# ------------------------------------------------------------------------------------------------------#
# Sets Icon images folder
dir_icon = os.path.join(dir_root, "Icons")

# Define Application Icons
class icons:
    # Import Application Icons
    app1_icon = ImageTk.PhotoImage(Image.open(os.path.join(dir_icon, "app1.png")))
    app2_icon = ImageTk.PhotoImage(Image.open(os.path.join(dir_icon, "app2.png")))
    app3_icon = ImageTk.PhotoImage(Image.open(os.path.join(dir_icon, "app3.png")))


# ------------------------------------------------------------------------------------------------------#
class prof_switch:
    def profile():
        # profile_var 1 is profile1
        if profile_var.get() == 1:
            app1.deselect()
            app2.deselect()
            app3.deselect()
            
            switch.app1_checked()
            switch.app2_checked()
            switch.app3_checked()

            app1.select()

            switch.app1_checked()

        # profile_var 2 is profile2 
        elif profile_var.get() == 2:
            app1.deselect()
            app2.deselect()
            app3.deselect()
            
            switch.app1_checked()
            switch.app2_checked()
            switch.app3_checked()

            app2.select()

            switch.app2_checked()

    # Clear button will deselect everything
    def clear_all():
            app1.deselect()
            app2.deselect()
            app3.deselect()

            switch.app1_checked()
            switch.app2_checked()
            switch.app3_checked()

            # Clears radio button
            profile_var.set(None)


# ------------------------------------------------------------------------------------------------------#
# Disables/Enables checkbuttons under specific circumstance
class switch:
    # Disables app2, and app3 if app1 is checked.
    # Enables the above app1 is unchecked.
    def app1_checked():
      if app1_var.get() == 'on':
          app2['state'] = DISABLED
          app3['state'] = DISABLED
      else:
          app2['state'] = NORMAL
          app3['state'] = NORMAL
    # Disables app1, and app3 if app2 is checked.
    # Enables the above app2 is unchecked.
    def app2_checked():
      if app2_var.get() == 'on':
          app1['state'] = DISABLED
          app3['state'] = DISABLED
      else:
          app1['state'] = NORMAL
          app3['state'] = NORMAL
    # Disables app1, and app2 if app3 is checked.
    # Enables the above app3 is unchecked.
    def app3_checked():
      if app3_var.get() == 'on':
          app1['state'] = DISABLED
          app2['state'] = DISABLED
      else:
          app1['state'] = NORMAL
          app2['state'] = NORMAL

# ------------------------------------------------------------------------------------------------------#
# Create "Help" window for explanation
import help
# Prompt confirmation window to proceed with installation
class howto():
    def help_window():
        helpWindow = Toplevel(root)
        helpWindow.title("Help")
        helpWindow.geometry('%dx%d+%d+%d' % (510, 310, ws, hs))
        helpWindow.attributes("-topmost", True)
        helpWindow.resizable(False, False)

        explanation = help.help()
        explanation_frame = Frame(helpWindow)
        explanation_frame.pack(expand=True, fill='both')
        explanation_label = Label(explanation_frame, text= explanation, justify='left')
        explanation_label.pack(expand=True, fill='both')

help_button = Button(root, text= "Help", command=howto.help_window, padx= 3, pady= 3)


# ------------------------------------------------------------------------------------------------------#
# Create app_Frame for the Profile check boxes to populate
profile_frame = LabelFrame(root, text="Select for Preset Profile")
profile_var = IntVar()

default = Radiobutton(
    profile_frame,
    text="Prof. 1",
    compound=LEFT,
    variable=profile_var,
    value=1,
    command= prof_switch.profile
)
default.grid(row=0, column=0, sticky=W)

property = Radiobutton(
    profile_frame,
    text="Prof. 2",
    compound=LEFT,
    variable=profile_var,
    value=2,
    command= prof_switch.profile
)
property.grid(row=0, column=1, sticky=W)

custom = Button(
    profile_frame,
    text="Clear Selection",
    compound=LEFT,
    command= prof_switch.clear_all
)
custom.grid(row=0, column=2, sticky=W)


# ------------------------------------------------------------------------------------------------------#
# Create app_Frame for the Application check boxes to populate
app_frame = LabelFrame(root, text="Select Programs to Install")

# Creates Check box for app1
app1_var = StringVar(value="off")
app1 = Checkbutton(
    app_frame,
    text="app1",
    image=icons.app1_icon,
    compound=LEFT,
    variable=app1_var,
    onvalue="on",
    offvalue="off",
    command= switch.app1_checked
)
app1.grid(row=0, column=0, sticky=W)

# Creates Check box for app2
app2_var = StringVar(value="off")
app2 = Checkbutton(
    app_frame,
    text="app2",
    image=icons.app2_icon,
    compound=LEFT,
    variable=app2_var,
    onvalue="on",
    offvalue="off",
    command= switch.app2_checked
)
app2.grid(row=1, column=0, sticky=W)

# Creates Check box for app3
app3_var = StringVar(value="off")
app3 = Checkbutton(
    app_frame,
    text="app3",
    image=icons.app3_icon,
    compound=LEFT,
    variable=app3_var,
    onvalue="on",
    offvalue="off",
    command= switch.app3_checked
)
app3.grid(row=2, column=0, sticky=W)



# ------------------------------------------------------------------------------------------------------#
# Defines the script folder
dir_script = os.path.join(dir_root, "scripts")

# Collection of functions to execute batch files
class r_scripts:
    def app1():
        if app1_var.get() == "on":
            filepath = os.path.join(dir_script, "app1.bat")
            p = Popen([filepath], cwd=dir_script)
            stdout, stderr = p.communicate()

    def app2():
        if app2_var.get() == "on":
            filepath = os.path.join(dir_script, "app2.bat")
            p = Popen([filepath], cwd=dir_script)
            stdout, stderr = p.communicate()

    def app3():
        if app3_var.get() == "on":
            filepath = os.path.join(dir_script, "app3.bat")
            p = Popen([filepath], cwd=dir_script)
            stdout, stderr = p.communicate()


    def install():
        r_scripts.app1()
        r_scripts.app2()
        r_scripts.app3()



# ------------------------------------------------------------------------------------------------------#
# Prompt confirmation window to proceed with installation
class confirmation():
    def confirm_window():
        confirmWindow = Toplevel(root)
        confirmWindow.title("Installation Confirmation")
        confirmWindow.geometry('%dx%d+%d+%d' % (w, h/3, ws, hs))
        # Confirmation window will always be the top window
        confirmWindow.attributes("-topmost", True)
        Label(
            confirmWindow,
            text="Proceed to installation?",
            padx=w/4,
            pady=h/18,
        ).grid(row=0, column=0, columnspan=6)
        # Creates a "Yes" button to proceed
        # Terminates the window first, and installs checked programs
        y_button= Button(
                    confirmWindow,
                    text="Yes",
                    command=lambda: [confirmWindow.destroy(), r_scripts.install()],
                    width=10)
        y_button.grid(row=1, column=2)

        # Creates "No" button
        # Terminates the confirmation pop-up window
        n_button= Button(
                    confirmWindow,
                    text="No",
                    command=confirmWindow.destroy,
                    width=10)
        n_button.grid(row=1, column=3)




# ------------------------------------------------------------------------------------------------------#
# root window pack

help_button.pack(anchor='e')
profile_frame.pack(pady=5, padx=10, anchor="nw", expand=FALSE, fill="both")
app_frame.pack(pady=5, padx=10, anchor="nw", expand=FALSE, fill="both")

# Create Button for installing selected Programs
install = Button(root, text="Install Programs", command=confirmation.confirm_window)
install.pack(pady=5, padx=10, anchor="w")

# Create Button for closing the window
exit = Button(root, text="Close Window", command=root.quit)
exit.pack(pady=5, padx=10, anchor="w")


# withdraw() hides the installer window. It's manifested but just cannot be seen.
root.withdraw()

root.mainloop()