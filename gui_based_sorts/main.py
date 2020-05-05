from tkinter import * 
from tkinter import ttk
import random 

# build the window base 
root = Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900, 600) 
root.config(bg='black') 

# building the UI
ui_frame = Frame(root, width=600, height=200, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white' )
canvas.grid(row=1, column=0, padx=10, pady=5)


root.mainloop()
