import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora KY")
        self.geometry("300x400")

        self.result_var = ctk.StringVar(value="0")
        self.create_widgets()

    def create_widgets(self):
        entry = ctk.CTkEntry(self, textvariable=self.result_var, font=("Lato", 24), justify="right")
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = ctk.CTkButton(self, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.grid_rowconfigure(row, weight=1)
            self.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.result_var.set("0")
        elif char == "=":
            try:
                expr = self.result_var.get()
                result = str(eval(expr))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current = self.result_var.get()
            if current == "0" or current == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

if __name__ == "__main__":
    calculadora = Calculator()
    calculadora.mainloop()