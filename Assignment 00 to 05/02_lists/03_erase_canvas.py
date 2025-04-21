# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

""" This program implements an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white. """

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Eraser on Canvas")

# Canvas setup
canvas_width = 400
canvas_height = 400
cell_size = 40
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Store all cell rectangles
cells = []

# Draw grid of blue rectangles (cells)
for y in range(0, canvas_height, cell_size):
    row = []
    for x in range(0, canvas_width, cell_size):
        rect = canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="blue", outline="black")
        row.append(rect)
    cells.append(row)

# Create the eraser (a white rectangle)
eraser_size = 60
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, outline="red")

# Function to move eraser and erase blue cells
def move_eraser(event):
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)

    # Get coordinates of eraser
    ex1, ey1, ex2, ey2 = canvas.coords(eraser)

    # Check which cells the eraser touches
    for row in cells:
        for rect in row:
            x1, y1, x2, y2 = canvas.coords(rect)
            # Check overlap
            if not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2):
                canvas.itemconfig(rect, fill="white")

# Bind mouse drag to move eraser
canvas.bind("<B1-Motion>", move_eraser)

# Start GUI loop
root.mainloop()
