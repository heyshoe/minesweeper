from Tkinter import *

class block(Button):
    def __init__(self):
        Button.__init__(self)
        self.revlealed=False
        self.flagged=False
        self.num=0
    def reveal(self):
        
        
