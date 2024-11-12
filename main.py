import tkinter as tk

Light_Gray = "#F5F5F5"
Label_Color = "#25265E"
font = ('Arial', 16)
font2 = ('Arial', 40, "bold")

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
        self.buttons_frame = self.create_buttons_frame()
    
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
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()