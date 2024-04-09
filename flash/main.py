from tkinter import *
from gui import GUI
from peace import Peace
from table import Table

class Game:
    def __init__(self):
        self.window = Tk()        
        GUI.center(self.window, 500, 500)
        self.window.config(bg='black')
        self.table = Table()
        self.table.start(self.window)
        self.verify_table()
    
    def verify_table(self):
        self.table.verify_peace()
        self.window.after(1000, self.verify_table)
       
if __name__ == "__main__":
    game = Game()
    game.window.mainloop()