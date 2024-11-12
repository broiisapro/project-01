import tkinter as tk

Light_Gray = "#F5F5F5"
Label_Color = "#25265E"
White = "#FFFFFF"
offWhite = "#F8FAFF"
lightBlue = "#CCEDFF"

default = ('Arial', 20)
font = ('Arial', 16)
font2 = ('Arial', 40, "bold")
digit = ('Arial', 24, "bold")

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0,0)

        self.totalexpression = "0"
        self.currentexpression = "0"

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits ={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1 )

        self.create_operator_buttons()
        self.create_special_buttons()
    
    def create_special_buttons(self):
        self.create_equals_button()
        self.create_clear_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.totalexpression, anchor=tk.E, bg=Light_Gray, fg=Label_Color, padx= 24, font=font)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.currentexpression, anchor=tk.E, bg=Light_Gray, fg=Label_Color, padx= 24, font=font2)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=Light_Gray)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digit_buttons(self):
        for digit, grid_vaue in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=White, fg=Label_Color, font=digit, borderwidth=0)
            button.grid(row=grid_vaue[0], column=grid_vaue[1], sticky=tk.NSEW)
    
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=offWhite, fg=Label_Color, font=default, borderwidth=0)
            button.grid(row= i, column= 4, sticky=tk.NSEW)
            i+=1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=offWhite, fg=Label_Color, font=default, borderwidth=0)
        button.grid(row= 0, column= 1, columnspan= 3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=lightBlue, fg=Label_Color, font=default, borderwidth=0)
        button.grid(row= 4, column= 3, columnspan= 2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()