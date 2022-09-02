from tkinter import *
THEME_COLOR = "#375362"

class QuizInteface():
    
    def __init__(self):
        self.window = Tk()
        
        self.window.title('Quiz')
        self.window.config(padx=20,pady=20)
        self.false = PhotoImage('images/false.png')
        self.true = PhotoImage('2.1 quizzler-app-start/images/true.png')
       
        
        self.window.mainloop()