from tkinter import *

board = Tk()
board.title("Sudoku")
board.geometry("900x900")


class Square:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.x = canvas.coords(rectangle)[0]
        self.y = canvas.coords(rectangle)[1]
        self.pencil_lable = canvas.create_text(self.x+5, self.y+5, text = "1,2,3,4", font=("Helvetica", 5))
        self.marker_lable = canvas.create_text(self.x+40,self.y+40, text = "4", font=("Helvetica", 20))

    def __str__(self):
            return "Square"

    def __repr__(self):
            return str(self)




mode = "Marker"
numbers = [1,2,3,4,5,6,7,8,9]
def key_pressed(event):
    global current_button , canvas, numbers, mode
    canvas.itemconfig(current_button, fill = "yellow")
    kp = event.char
    if kp == "m":
        mode = "Marker"
    elif kp == "p":
        mode = "Pencil"
    elif mode == "pencil" and kp in numbers:
        pass
    elif mode == "Marker" and kp in numbers:
        pass    
    
def set_button(button):
    global current_button
    current_button = button

    

canvas = Canvas(board, bg = "gray", width = 810, height = 810)
canvas.grid(row=0, column=0, columnspan=9, rowspan=9)
board.bind("<Key>", key_pressed)

current_button = 0
for j in range(9):
    for i in range(9):
        b = Square(canvas.create_rectangle(0+(i*90),0+(j*90),90+(i*90),90+(j*90), fill = "red")).rectangle
        canvas.tag_bind(b, "<ButtonPress-1>", lambda event, button = b :set_button(button))
board.mainloop()