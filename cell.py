from tkinter import Button
from tkinter import Label
import settings
from settings import rows_and_cols
from settings import cells_left_count
import random

class Cell:
    all = []
    open_count = settings.cells_left_count
    cell_label_object = None
    cell_btn_object = None

    def __init__(self, x, y, is_mine = False,is_cell_open = False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.is_cell_open = is_cell_open
        (Cell.all.append(self))





    def cell_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4
        )

        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def label_object(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            font=("",34),
            text=f"Cells left: {settings.cells_left_count}"
        )
        Cell.cell_label_object = lbl

    def left_click_actions(self,event):
        if self.is_mine:
                self.show_mine()

        else:
            if self.surrounded_cells_len == 0:
                for c in self.show_cell:
                    c.cell_btn_object.configure(text=f'{c.surrounded_cells_len}')

            self.cell_btn_object.configure(text=f'{self.surrounded_cells_len}')

        self.is_cell_open = True




    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def show_cell(self):
        if Cell.cell_label_object:
            Cell.cell_label_object.configure(text = f"Cells left: {Cell.open_count}" )


        surrounded = [self.get_cell_by_axis(self.x-1,self.y-1),
                      self.get_cell_by_axis(self.x - 1, self.y),
                      self.get_cell_by_axis(self.x - 1, self.y +1),
                      self.get_cell_by_axis(self.x , self.y - 1),
                      self.get_cell_by_axis(self.x + 1, self.y - 1),
                      self.get_cell_by_axis(self.x + 1, self.y),
                      self.get_cell_by_axis(self.x + 1, self.y + 1),
                      self.get_cell_by_axis(self.x , self.y + 1)
                ]


        surrounded = [scell for scell in surrounded if scell!= None ]
        return surrounded


    @property
    def surrounded_cells_len(self):


        counter = 0
        for cell in self.show_cell:
            if cell.is_mine:
                counter += 1
        return counter



    def show_mine(self):
        self.cell_btn_object.configure(bg='red')

    def right_click_actions(self,event):
        print(event)
        print("I am Right Clicked")

    @staticmethod
    def random_choices():
        pick_cells = random.sample(Cell.all,rows_and_cols**2//4)
        for i in pick_cells:
            i.is_mine = True

    def count_checker(self):
        if self.is_cell_open != 1:
            Cell.open_count -= Cell.open_count
            self.is_cell_open = True



    def __repr__(self):
        return f"Cell({self.x},{self.y})"

