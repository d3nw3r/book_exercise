from tkinter import *

top = Tk()

mb=  Menubutton ( top, text="CheckComboBox", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

Item0 = IntVar()
Item1 = IntVar()
Item2 = IntVar()

mb.menu.add_checkbutton ( label="Item0", variable=Item0)
mb.menu.add_checkbutton ( label="Item1", variable=Item1)
mb.menu.add_checkbutton ( label="Item2", variable=Item2)

mb.pack()
top.mainloop()