import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

app = tk.Tk()
app.title("Add Two Numbers")

# Create input fields for two numbers
entry_num1 = tk.Entry(app)
entry_num1.pack()

entry_num2 = tk.Entry(app)
entry_num2.pack()

# Create a button to calculate the sum
calculate_button = tk.Button(app, text="=", command=add_numbers)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()

