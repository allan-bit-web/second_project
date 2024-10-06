import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to hold the expression
expression = ""

# Function to update the expression in the entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))  # Evaluate the expression
        equation.set(total)  # Set the result in the entry box
        expression = total  # Store the result for further calculations
    except:
        equation.set(" error ")  # Show error message
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar to hold the text in the entry widget
equation = tk.StringVar()

# Create the entry widget
entry_box = tk.Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=14, borderwidth=4)
entry_box.grid(row=0, column=0, columnspan=4)

# Creating buttons
button1 = tk.Button(root, text='1', font=('arial', 20, 'bold'), command=lambda: press(1), height=1, width=4)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text='2', font=('arial', 20, 'bold'), command=lambda: press(2), height=1, width=4)
button2.grid(row=1, column=1)

button3 = tk.Button(root, text='3', font=('arial', 20, 'bold'), command=lambda: press(3), height=1, width=4)
button3.grid(row=1, column=2)

button4 = tk.Button(root, text='4', font=('arial', 20, 'bold'), command=lambda: press(4), height=1, width=4)
button4.grid(row=2, column=0)

button5 = tk.Button(root, text='5', font=('arial', 20, 'bold'), command=lambda: press(5), height=1, width=4)
button5.grid(row=2, column=1)

button6 = tk.Button(root, text='6', font=('arial', 20, 'bold'), command=lambda: press(6), height=1, width=4)
button6.grid(row=2, column=2)

button7 = tk.Button(root, text='7', font=('arial', 20, 'bold'), command=lambda: press(7), height=1, width=4)
button7.grid(row=3, column=0)

button8 = tk.Button(root, text='8', font=('arial', 20, 'bold'), command=lambda: press(8), height=1, width=4)
button8.grid(row=3, column=1)

button9 = tk.Button(root, text='9', font=('arial', 20, 'bold'), command=lambda: press(9), height=1, width=4)
button9.grid(row=3, column=2)

button0 = tk.Button(root, text='0', font=('arial', 20, 'bold'), command=lambda: press(0), height=1, width=4)
button0.grid(row=4, column=0)

plus = tk.Button(root, text='+', font=('arial', 20, 'bold'), command=lambda: press('+'), height=1, width=4)
plus.grid(row=1, column=3)

minus = tk.Button(root, text='-', font=('arial', 20, 'bold'), command=lambda: press('-'), height=1, width=4)
minus.grid(row=2, column=3)

multiply = tk.Button(root, text='*', font=('arial', 20, 'bold'), command=lambda: press('*'), height=1, width=4)
multiply.grid(row=3, column=3)

divide = tk.Button(root, text='/', font=('arial', 20, 'bold'), command=lambda: press('/'), height=1, width=4)
divide.grid(row=4, column=3)

equal = tk.Button(root, text='=', font=('arial', 20, 'bold'), command=equalpress, height=1, width=4)
equal.grid(row=4, column=2)

clear = tk.Button(root, text='C', font=('arial', 20, 'bold'), command=clear, height=1, width=4)
clear.grid(row=4, column=1)

# Run the main loop
root.mainloop()
