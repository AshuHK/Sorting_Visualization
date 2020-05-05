from tkinter import * 
from tkinter import ttk
import random 

# build the window base 
root = Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900, 600) 
root.config(bg="black") 

selected_algorithm = StringVar()

# seperating the layouts 
ui_frame = Frame(root, width=600, height=200, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# building the UI 
Label(ui_frame, text="Algorithm: ", bg="grey").grid(row=0,column=0, padx=5, pady=5, sticky="w")

algomenu = ttk.Combobox(ui_frame, textvariable=selected_algorithm, values=["Bubble sort", "Selection Sort", "Insertion sort"])
algomenu.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
