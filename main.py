import tkinter as tk

class Calculator:
    def __innit__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator
    calc.run