from tkinter import *
import background
import pyperclip
import os

directory = os.getcwd()

def test_001():
    window = Tk()

    def selected_row(event):
            global selected_tuple
            try:    
                index=SelectionBox.curselection()[0]
                selected_tuple = SelectionBox.get(index)
                Name.delete(0,END)
                Name.insert(END,selected_tuple[1])
                Link.delete(0,END)
                Link.insert(END,selected_tuple[2])
                Rating.delete(0,END)
                Rating.insert(END,selected_tuple[3])
            except IndexError:
                pass

    def view_command():
        SelectionBox.delete(0,END)
        for row in background.view():
            SelectionBox.insert(END, row)

    def search_command():
        SelectionBox.delete(0,END)
        for row in background.search(Name_text.get(), Link_text.get(), Rating.get()):
            SelectionBox.insert(END, row)

    def delete_command():
        background.delete(selected_tuple[0])

    def add_command():
        background.insert(Name_text.get(),Link_text.get(),Rating_text.get())     
        SelectionBox.delete(0,END)
        SelectionBox.insert(END, Name_text.get(),Link_text.get(),Rating_text.get())

    def update_command():
        background.update(selected_tuple[0],Name_text.get(), Link_text.get(), Rating.get())  

    def copy_command():
        pyperclip.copy(Link_text.get())


    window_width = 700
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height/2 -window_height/2)
    position_right = int(screen_width / 2 - window_width/2)
    window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    window.resizable(False,False)               #this restricts the user from changing the window size

    #Canvas/Background color
    canvas = Canvas(window, bg = "pink", width = 750, height = 500)
    canvas.place(x=0, y=0)

    #Labels
    title=Label(window,text="ANIME DATABASE",fg = "white", bg = "#212741",font="Bold 20")
    title.place(x=220,y=15)

    NameLabel = Label(window, text="Name",bg = "pink", font="8")
    NameLabel.place(x = 50, y = 75)


    LinkLabel = Label(window, text="Link",bg = "pink", font="8")
    LinkLabel.place(x = 50, y = 125)

    RatingLabel = Label(window, text="Rating",bg = "pink", font="8")
    RatingLabel.place(x = 580, y = 75)

    #Entries
    Name_text = StringVar()
    Name=Entry(window,textvariable = Name_text, borderwidth = 1, highlightthickness=1, width = 75)
    Name.place(x = 110, y = 75)

    Link_text = StringVar()
    Link=Entry(window,textvariable = Link_text, borderwidth=1,highlightthickness=1, width = 75)   
    Link.place(x = 110, y = 125)

    Rating_text = StringVar()
    Rating=Entry(window,textvariable = Rating_text, borderwidth=1,highlightthickness=1, width = 5)    
    Rating.place(x = 645, y = 75)

    #Listbox
    SelectionBox=Listbox(borderwidth = 1, highlightthickness=1, width = 87, height = 15)
    SelectionBox.place(x = 70, y = 175)

    SelectionBox.bind('<<ListboxSelect>>',selected_row)

    #Scrollbar
    Scroll_Bar = Scrollbar()
    Scroll_Bar.place(x = 620, y = 175, height = 245)

    SelectionBox.configure(yscrollcommand = Scroll_Bar.set)
    Scroll_Bar.configure(command = SelectionBox.yview)


    #Buttons
    search_button = Button(window,text = "Search",  width = 12, command = search_command)
    search_button.place(x = 45, y = 455)

    add_button = Button(window, text = "Add",  width = 12, command = add_command)
    add_button.place(x = 145, y = 455)

    update_button = Button(window, text = "Update",  width = 12, command = update_command)
    update_button.place(x = 245, y = 455)

    delete_button = Button(window, text = "Delete",  width = 12, command = delete_command)
    delete_button.place(x = 345, y = 455)

    view_button = Button(window, text = "View",  width = 12, command = view_command)
    view_button.place(x = 445, y = 455)

    close_button = Button(window, text = "Close",  width = 12, command = window.destroy)
    close_button.place(x = 565, y = 455)

    copy_button = Button(window, text = "Copy",  width = 6, command = copy_command)
    copy_button.place(x = 580, y = 123)

    window.mainloop()
