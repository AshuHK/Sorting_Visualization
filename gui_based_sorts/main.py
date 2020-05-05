from tkinter import * 
from tkinter import ttk
import random 

# build the window base 
root = Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900, 600) 
root.config(bg="black") 

selected_algorithm = StringVar()

def draw_data(data_list):
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data_list) + 1) 

    offset = 30
    spacing = 10 
    for i, height in enumerate(data_list): 

        # top left 
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height
        
        # bottom right 
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor="sw", text=str(data_list[i]))

def generate(): 
    print("Algorithm Selected: {}".format(selected_algorithm.get()))

    data_list = [1, 2, 3, 4, 5, 100]
    draw_data(data_list)

# seperating the layouts 
ui_frame = Frame(root, width=600, height=200, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# building the UI 
Label(ui_frame, text="Algorithm: ", bg="grey").grid(row=0,column=0, padx=5, pady=5, sticky="w")

# drop down menu to pick the algorithm
algorithm_menu = ttk.Combobox(ui_frame, textvariable=selected_algorithm, values=["Bubble sort", "Selection Sort", "Insertion sort", "Merge Sort", "Quick Sort"])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)

# set the default algorithm to be the first one in the list
algorithm_menu.current(0)

# need to figure out how to change the background color 
Button(ui_frame, text="Generate", command=generate, bg="white").grid(row=0, column=2, padx=5, pady=5)

# size input 
Label(ui_frame, text="Size: ", bg="grey").grid(row=1,column=0, padx=5, pady=5, sticky="w")
size_entry = Entry(ui_frame)
size_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

Label(ui_frame, text="Min value: ", bg="grey").grid(row=1,column=2, padx=5, pady=5, sticky="w")
min_entry = Entry(ui_frame)
min_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

Label(ui_frame, text="Max value: ", bg="grey").grid(row=1,column=4, padx=5, pady=5, sticky="w")
max_entry = Entry(ui_frame)
max_entry.grid(row=1, column=5, padx=5, pady=5, sticky="w")

root.mainloop()
