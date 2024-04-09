from tkinter import *

PEACES = []

class Peace:
    def __init__(self, window, text, pos_x, pos_y):
        self.window = window
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 8
        self.height = 4 
        self.last_x = None
        self.last_y = None
    
    def create_peace(self):
        self.peace = Label(self.window, text=self.text, width=self.width, height=self.height)
        self.peace.bind("<ButtonPress-1>", lambda event, peace=self.peace: self.on_press(event, peace, self.pos_x, self.pos_y))
        self.peace.place(x=self.pos_x, y=self.pos_y)
        PEACES.append(self.peace)

    def on_press(self, event, peace, x, y):
        self.last_x = peace.winfo_x()
        self.last_y = peace.winfo_y()
        self.peace.bind("<B1-Motion>", lambda event, peace=self.peace: self.om_motion(event, peace))
        
    
    def om_motion(self, event, peace):
        screen_x = self.window.winfo_pointerx()
        screen_y = self.window.winfo_pointery()

        window_x = self.window.winfo_rootx()
        window_y = self.window.winfo_rooty()

        mouse_x = screen_x - window_x
        mouse_y = screen_y - window_y
        #print(mouse_x, mouse_y)
        #print(peace.winfo_x(), peace.winfo_y())
        #print(peace.winfo_width(), peace.winfo_height())
        self.peace.place(x=mouse_x-(62//2), y=mouse_y-(66//2))
        print(peace.winfo_x(), peace.winfo_x())
        self.peace.bind("<ButtonRelease-1>", lambda event, peace=self.peace: self.on_release(event, peace))
    
    def on_release(self, event, peace):
        screen_x = self.window.winfo_pointerx()
        screen_y = self.window.winfo_pointery()

        window_x = self.window.winfo_rootx()
        window_y = self.window.winfo_rooty()

        mouse_x = (screen_x - window_x) - 62//2
        mouse_y = (screen_y - window_y) - 66//2
        #print(mouse_x, mouse_y)
        #print(peace.winfo_x(), peace.winfo_y())
        #print(peace.winfo_width(), peace.winfo_height())
        print("PEÇA SEGURADA",peace.winfo_x(), peace.winfo_y())
        x = 0
        y = 0
        margin = 10
        for p in PEACES:
            if peace.winfo_x() == p.winfo_x() and peace.winfo_y() == p.winfo_y():
                x = p.winfo_x()
                y= p.winfo_y()
                peace.place(x=x, y=y)
                p.place(x=self.last_x, y=self.last_y)

        """if peace.winfo_x:
                self.peace.place(x=mouse_x, y=mouse_y)
        else:
            self.peace.place(x=self.pos_x, y=self.pos_y)"""



