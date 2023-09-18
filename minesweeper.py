from tkinter import *
from cell import Cell
import settings

root = Tk()
root.geometry(f'{settings.width}x{settings.height}')
root.configure(bg='black')
root.title('MineSweeper')
root.resizable(False,False)


top_frame = Frame(
    root,
    bg='black',
    width = settings.width,
    height = settings.height_percent(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=settings.width_percent(25),
    height=settings.height_percent(75)
)
left_frame.place(x=0, y=180)

centre_frame = Frame(
    root,
    bg='black',
    width=settings.width_percent(75),
    height=settings.height_percent(75)
)
centre_frame.place(x=settings.width_percent(25), y=settings.height_percent(25))

for x in range(settings.rows_and_cols):
    for y in range(settings.rows_and_cols):
        c1 = Cell(x,y)
        c1.cell_btn_object(centre_frame)
        c1.cell_btn_object.grid(
            row=x, column=y
        )

Cell.random_choices()
Cell.label_object(left_frame)
Cell.cell_label_object.place(x=0,y=0)








root.mainloop()


