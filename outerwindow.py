#IMPORTING ALL THE REQUIRED PACKAGES/LIBRARIES
from tkinter import * #Package to create GUI
import os #Package to navigate paths
import innerwindow

directory = os.getcwd() #This gets the path/location of current directory

#Creating a GUI and assigning its dimensions as well as 
#writing a code for the window to open at the centre of the screen

owindow = Tk()          #Any other name can be given in place of "owindow" for example "root"
owindow_width = 304
owindow_height = 370
oscreen_width = owindow.winfo_screenwidth()
oscreen_height = owindow.winfo_screenheight()
oposition_top = int(oscreen_height/2 -owindow_height/2)
oposition_right = int(oscreen_width / 2 - owindow_width/2)
owindow.geometry(f'{owindow_width}x{owindow_height}+{oposition_right}+{oposition_top}')
owindow.resizable(False,False)

#Initialising the background color using canvas
obackGround = Canvas(owindow, bg="pink", height=547, width=301)
obackGround.place(x = 0, y = 0) 

#FUNCTIONS
def invalid():
    olb4 = Label(owindow, text = "INVALID", fg="red", bg = "#2f3044",font="bold 16")
    olb4.place(x = 105, y = 207)

def check_command():
    if str(oe1_value.get()) == "test" and str(oe2_value.get()) == "test":   #you can change username and pass here
        owindow.destroy()
        innerwindow.test_001()
    else:
        invalid()

#LABELS
olb1 = Label(owindow, text = "Username", bg = "pink",font="bold 16")
olb1.place(x = 25,y =120)

olb2 = Label(owindow, text = "Password", bg = "pink",font="bold 16")
olb2.place(x = 25,y =160)

olb3 = Label(owindow, text = "ANIME DATABASE",fg = "#e94b3c", bg = "pink",font="bold 20 underline")
olb3.place(x = 30,y =40)


#ENTRIES
oe1_value = StringVar()
oe1 = Entry(owindow,textvariable = oe1_value, borderwidth = 4, highlightthickness=0, width = 20)
oe1.place(x=135, y=123)

oe2_value = StringVar()
oe2 = Entry(owindow,show="*", textvariable = oe2_value,borderwidth = 4, highlightthickness=0, width = 20)
oe2.place(x=135, y = 163)

#BUTTONS
check_button = Button(owindow,text = "LOG IN", width = 14, command = check_command)
check_button.place(x = 93, y = 260)

oclose = Button(owindow,text="Close", width = 12, command= owindow.destroy)
oclose.place(x = 100, y = 315)

owindow.mainloop()    
