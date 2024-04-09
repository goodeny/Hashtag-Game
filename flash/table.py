from peace import Peace
from peace import PEACES
from tkinter import *

class Table:
    def __init__(self):
        pass

    def verify_peace(self):
        self.v_peace1()
        self.v_peace2()
        self.v_peace3()
    
    def v_peace1(self):
        if PEACES[0].winfo_x() == 50 and PEACES[0].winfo_y() == 50:
            PEACES[0].config(bg='green')
        elif PEACES[0].winfo_y() == 50 and PEACES[0].winfo_x() != 50:
            PEACES[0].config(bg='orange')
        else:
            PEACES[0].config(bg='white')
    
    def v_peace2(self):
        if PEACES[1].winfo_x() == 150 and PEACES[1].winfo_y() == 50:
            PEACES[1].config(bg='green')
        elif PEACES[1].winfo_y() == 50 and PEACES[1].winfo_x() != 150:
            PEACES[1].config(bg='orange')
        else:
            PEACES[1].config(bg='white')

    def v_peace3(self):
        if PEACES[2].winfo_x() == 250 and PEACES[2].winfo_y() == 50:
            PEACES[2].config(bg='green')
        elif PEACES[2].winfo_y() == 50 and PEACES[2].winfo_x() != 250:
            PEACES[2].config(bg='orange')
        else:
            PEACES[2].config(bg='white')
    

    def start(self,window):
        self.window = window

        self.peace1 = Peace(self.window, '1', 50, 50)
        self.peace1.create_peace()

        self.peace2 = Peace(self.window, '2', 150, 50)
        self.peace2.create_peace()

        self.peace3 = Peace(self.window, '3', 250, 50)
        self.peace3.create_peace()