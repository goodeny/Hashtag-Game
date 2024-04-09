from tkinter import *

class GUI:
    def center(window, h, w):
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = (width - w)//2
        y = (height - h)//2
        return window.geometry(f'{w}x{h}+{x}+{y}')