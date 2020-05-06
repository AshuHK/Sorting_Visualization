from tkinter import *
from tkinter import ttk

from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from QuickSort import quick_sort
from MergeSort import merge_sort

import random

# build the window base
root = Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900, 600)
root.config(bg="black")

# Global variables
selected_algorithm = StringVar()
data_list = []


def draw_data(data_list, color_list):

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

        # draws the rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_list[i])
        canvas.create_text(x0 + 2, y0, anchor="sw", text=str(data_list[i]))

    root.update()


def generate():
    global data_list

    try:
        # pull the size from the user
        size_value = int(size_entry.get())
    except ValueError:
        size_value = 30

    # Set a limit on the sizes that could be used
    if (size_value > 30) or (size_value < 3):
        size_value = 30

    # create the list of random data
    data_list = [i for i in range(1, size_value + 1)]
    random.shuffle(data_list)

    draw_data(data_list, ["red" for x in range(len(data_list))])


def start_algorithm():
    global data_list

    if algorithm_menu.get() == "Bubble Sort":
        bubble_sort(data_list, draw_data, speed_scale.get())

    elif algorithm_menu.get() == "Selection Sort":
        selection_sort(data_list, draw_data, speed_scale.get())

    elif algorithm_menu.get() == "Insertion Sort":
        insertion_sort(data_list, draw_data, speed_scale.get())

    elif algorithm_menu.get() == "Quick Sort":
        quick_sort(data_list, 0, len(data_list) - 1, draw_data, speed_scale.get())

    elif algorithm_menu.get() == "Merge Sort":
        merge_sort(data_list, 0, len(data_list) - 1, draw_data, speed_scale.get())


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
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Quick Sort",
        "Merge Sort",
    ],
)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)

# set the default algorithm to be the first one in the list
algorithm_menu.current(0)

# making a speed scale
speed_scale = Scale(
    ui_frame,
    from_=0.1,
    to=2.0,
    length=200,
    digits=2,
    resolution=0.2,
    orient=HORIZONTAL,
    label="Select Speed(sec)",
)
speed_scale.grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text="start", command=start_algorithm, bg="red").grid(
    row=0, column=3, padx=5, pady=5
)

# size input
Label(ui_frame, text="Size: ", bg="grey").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
size_entry = Entry(ui_frame)
size_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# need to figure out how to change the background color
Button(ui_frame, text="Generate", command=generate, bg="white").grid(
    row=1, column=2, padx=5, pady=5
)

root.mainloop()
