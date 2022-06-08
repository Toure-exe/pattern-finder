# Project by Lorenzo Camilleri - Giulio Taralli - Ismaila Toure
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from utilities.matrix_utils import create_matrix, create_colored_matrix
from utilities.pattern_utils import get_pattern_from_file
from utilities.pattern_utils import find_pattern_in_matrix
from utilities.rotations import  rotate_pattern90
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


window = tk.Tk()
global rot_pattern
global matrix

def get_matrix_inputs():
    result = row_entry.get()
    result2 = col_entry.get()
    pattern = get_pattern_from_file()
    openNewWindow(int(result), int(result2), pattern)

def change_window_dimension(rows, columns, new_window):
    default_width = 500
    default_height = 800
    dimension_gap_width= 100 # increasing the dimension for every row/col > 5 so if it's 7 row/col it will be +100 then default 500 x 800
    dimension_gap_height = 20 # different dimensional gap
    if rows <=5 or columns <=5:
        new_window.geometry('500x800')
        new_window.resizable(False,False)
    elif rows<=15 or columns<=15:
        custom_height = str(default_height + ((rows-5)*dimension_gap_height))
        custom_width = str(default_width + ((rows-5)*dimension_gap_width))
        new_window.geometry(custom_width + "x"+ custom_height)
        new_window.resizable(False,False)
    else:
        new_window.geometry('1920x1080')

def elaborate_matrix_in_gui(rows, columns, ax, pattern, matrix_text):
    global matrix
    matrix = create_matrix(rows, columns)
    list_of_matches = find_pattern_in_matrix(pattern, matrix)
    write_matches_in_gui(list_of_matches, matrix_text)

    create_colored_matrix(list_of_matches, matrix, ax)


def write_matches_in_gui(list_of_matches, matrix_text):
    if len(list_of_matches) > 0:  # if there are matchs i write in the gui that there are tot matches
        matrix_text['text'] = "This is The Matrix, found " + str(len(list_of_matches)) + " pattern match"
    else:
        matrix_text['text'] = "This is The Matrix, no pattern found"


def rotate_pattern_gui(ax, pattern_label, canvas, matrix_text):
    global rot_pattern
    global matrix
    canvas.get_tk_widget().pack_forget()
    rotated_pattern = rotate_pattern90(rot_pattern)
    pattern_label['text'] = rotated_pattern
    rot_pattern=rotated_pattern
    list_of_matches = find_pattern_in_matrix(rotated_pattern, matrix)
    write_matches_in_gui(list_of_matches, matrix_text)
    create_colored_matrix(list_of_matches, matrix, ax)


# function to open a new window with matrix and pattern rotation
def openNewWindow(rows, columns, pattern):
    global rot_pattern

    new_window = Toplevel(window)
    padding_x = (250 / 2)
    padding_y = (500 / 8) / 2

    change_window_dimension(rows, columns, new_window)
    new_window.title("Search Window")
    new_window.minsize(300, 300)
    new_window.maxsize(1920, 1080)
    new_window.configure(background='white')

    #create the outer frame where vertical scroll will be placed
    main_frame = tk.Frame(new_window, bg="white")
    main_frame.pack(fill=BOTH, expand=True)

    fig = Figure(figsize=(rows, columns))
    ax = fig.add_subplot(111)
    ax.axis('off')

    #create canvas inside main frame
    canvas = tk.Canvas(main_frame, bg='white')
    canvas.pack(side=LEFT,fill=BOTH, expand=True)

    #create scrollbar for vertical purpose attached to main frame
    my_scrollbar_vertical = Scrollbar(main_frame, orient = VERTICAL, command = canvas.yview)
    my_scrollbar_vertical.pack(side=RIGHT, fill=Y)

    #Configure The Canvas for Scrollbar
    canvas.configure(yscrollcommand=my_scrollbar_vertical.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    #create a second frame inside the canvas to place the objects
    second_frame = Frame(canvas, bg='white')
    second_frame.pack(fill=BOTH, expand=True)
    canvas.create_window((0,0), window=second_frame, anchor='nw', tags='frame')
    canvas.itemconfig(window, state=HIDDEN)
    rot_pattern = pattern

    #initialize labels
    pattern_text = Label(second_frame, text="This is the Pattern", font=("Courier", 14), padx=padding_x, pady=padding_y, bg='white')
    pattern_text.grid(row=0, column=0)
    pattern_text.grid(row=0, column=0)
    pattern_text.grid_rowconfigure(1, weight=1)
    pattern_text.grid_columnconfigure(1, weight=1)
    pattern_label = Label(second_frame, text=pattern, font=("Courier", 15), padx=padding_x, pady=padding_y, bg='white')
    pattern_label.grid(row=1)
    matrix_text = Label(second_frame, text="This is the Matrix", font=("Courier", 14), padx=padding_x, pady=padding_y, bg='white')
    matrix_text.grid(row=3)

    #create another canvas for the matrix itself using matplotlib and tkinker
    canvas1 = FigureCanvasTkAgg(fig, master=second_frame)  # A tk.DrawingArea.
    canvas1.get_tk_widget().grid(row=4, column=0)
    elaborate_matrix_in_gui(rows, columns, ax, pattern, matrix_text)

    #Rotate pattern button
    rotate_clockwise = tk.Button(second_frame,text="ROTATE PATTERN", bg="black", fg="white",
                              activeforeground="Orange",
                              activebackground="blue", #used lambda because is the only method to pass an argument to a button function
                              font="calibri", highlightcolor="purple", command=lambda: rotate_pattern_gui(ax, pattern_label, canvas1, matrix_text))
    rotate_clockwise.grid(row=2, column=0)

    #create scrollbar
    my_scrollbar_horizontal = Scrollbar(canvas, orient = HORIZONTAL, command = canvas.xview)
    my_scrollbar_horizontal.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=my_scrollbar_horizontal.set)
    canvas.moveto('0.50')



#MAIN PROGRAM SETTING FIRST WINDOW
window.title("Pattern Search Algorithm")

canvas = tk.Canvas(window, width=500, height=500)
# window.resizable(False, False)
padding_x = 125 / 2
padding_y = (500 / 12) / 2
window.minsize(700, 500)
window.maxsize(700, 500)
canvas.grid(rowspan=7)
canvas.grid_rowconfigure(0, weight=1)
canvas.grid_columnconfigure(0, weight=1)

# initialization of labels
program_label = Label(canvas, text="Insert rows and columns of the matrix", font=("Courier", 18, 'bold'),
                      padx=padding_x, pady=padding_y + 10)
program_label.grid_rowconfigure(1, weight=1)
program_label.grid_columnconfigure(1, weight=1)
rows_label = Label(canvas, text="Rows", font=("Courier", 14), padx=padding_x, pady=padding_y - 20)
columns_label = Label(canvas, text="Columns", font=("Courier", 14), padx=padding_x, pady=padding_y - 20)
bottom_text_label = Label(canvas, text="Progetto By Lorenzo Camilleri, Giulio Taralli & Ismaila Toure",
                             font=("Courier", 12), padx=padding_x - 20, pady=padding_y + 40)

program_label.grid(row=0)
rows_label.grid(row=1)
columns_label.grid(row=3)
bottom_text_label.grid(row=6)

# entry initialization
row_entry = Entry(canvas, font=("Courier", 14), justify='center')
col_entry = Entry(canvas, font=("Courier", 14), justify='center')
row_entry.grid(row=2, padx=padding_x, pady=padding_y)
col_entry.grid(row=4, padx=padding_x, pady=padding_y)

# initialization of buttons
insert_button = tk.Button(text="INSERT", bg="black", fg="white", command=get_matrix_inputs, activeforeground="Orange",
                          activebackground="blue",
                          font="calibri", highlightcolor="purple", width=15, padx=padding_x, pady=padding_y)
insert_button.grid(row=7)

window.mainloop()