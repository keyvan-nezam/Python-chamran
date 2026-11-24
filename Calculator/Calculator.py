import tkinter as tk
from tkinter import messagebox

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "×": lambda a, b: a * b,
    "÷": lambda a, b: a / b
}

num1 = 0
operator = None


def choose_operator(symbol):
    global num1, operator

    try:
        num1 = float(entry_num1.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter the first number.")
        return

    if operator == symbol:
        messagebox.showerror("Error", "You have already selected this operator.")
        return

    operator = symbol
    operator_label.config(text=symbol)


def calculate():
    if operator is None:
        messagebox.showerror(
            "Error",
            "Please select one of the four operators first."
        )
        return

    try:
        num2 = float(entry_num2.get())

        result = operations[operator](num1, num2)

        result_label.config(text=f"Result: {result:g}")

    except ValueError:
        messagebox.showerror("Error", "Please enter the second number.")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")


window = tk.Tk()
window.title("My Calculator")
window.geometry("400x350")
window.resizable(False, False)


tk.Label(window, text="First Number:").pack(pady=5)

entry_num1 = tk.Entry(window, justify="center", font=("Arial", 13))
entry_num1.pack()


tk.Label(window, text="Selected Operator:").pack(pady=5)

operator_label = tk.Label(
    window,
    text="None",
    font=("Arial", 16, "bold")
)
operator_label.pack()


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

for symbol in operations:
    tk.Button(
        button_frame,
        text=symbol,
        width=5,
        font=("Arial", 13),
        command=lambda op=symbol: choose_operator(op)
    ).pack(side="left", padx=5)


tk.Label(window, text="Second Number:").pack(pady=5)

entry_num2 = tk.Entry(window, justify="center", font=("Arial", 13))
entry_num2.pack()


tk.Button(
    window,
    text="=",
    width=15,
    font=("Arial", 13),
    command=calculate
).pack(pady=15)


result_label = tk.Label(
    window,
    text="Result:",
    font=("Arial", 15, "bold")
)
result_label.pack()


window.mainloop()
