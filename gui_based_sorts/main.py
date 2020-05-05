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
    
    # removes any previous data that was on the canvas 
    canvas.delete("all")

    # set up the basic parameters for drawing the data 
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data_list) + 1)
    offset = 10
    spacing = 10

    # create a normalized size so it fills screen better 
    normalized_data = [i / max(data_list) for i in data_list]
    for i, height in enumerate(normalized_data):

        # top left
        x0 = (i * x_width) + offset + spacing
        y0 = canvas_height - (height * 340)

        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0 + 2, y0, anchor="sw", text=str(data_list[i]))


def generate():
    print("Algorithm Selected: {}".format(selected_algorithm.get()))

    try: 
        # pull the size from the user 
        size_value = int(size_entry.get())
    except ValueError: 
        size_value = 30 

    # Set a limit on the sizes that could be used
    if (size_value > 30) or (size_value < 3): 
        size_value = 15

    # create the list of random data 
    data_list = [i for i in range(size_value)]
    random.shuffle(data_list)

    draw_data(data_list)


# seperating the layouts
ui_frame = Frame(root, width=600, height=200, bg="grey")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# building the UI
Label(ui_frame, text="Algorithm: ", bg="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)

# drop down menu to pick the algorithm
algorithm_menu = ttk.Combobox(
    ui_frame,
    textvariable=selected_algorithm,
    values=[
        "Bubble sort",
        "Selection Sort",
        "Insertion sort",
        "Merge Sort",
        "Quick Sort",
    ],
)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)

# set the default algorithm to be the first one in the list
algorithm_menu.current(0)

# need to figure out how to change the background color
Button(ui_frame, text="Generate", command=generate, bg="white").grid(
    row=0, column=2, padx=5, pady=5
)

# size input
Label(ui_frame, text="Size: ", bg="grey").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
size_entry = Entry(ui_frame)
size_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

root.mainloop()
