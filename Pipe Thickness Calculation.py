from tkinter import *

def require_wall_thickness(P, D, S, E, W, Y, c):
    t = (P * D) / (2 * (S * E * W + P * Y))
    return t + c

def calculate():
    try:
        P = float(P_input.get())
        D = float(D_input.get())
        S = float(S_input.get())
        E = float(E_input.get())
        W = float(W_input.get())
        Y = float(Y_input.get())
        c = float(c_input.get())

        result = require_wall_thickness(P, D, S, E, W, Y, c)
        result_var.set(f"Required Wall Thickness: {result:.4f}")
    except Exception as e:
        result_var.set(f"Error: {str(e)}")

# GUI Setup
GUI = Tk()
GUI.title("Pipe Thickness Calculation")
GUI.geometry("400x400")

# Input Labels and Entry Fields
Label(GUI, text="Internal Design Gauge Pressure (P)").grid(row=0, column=0, padx=10, pady=5)
P_input = Entry(GUI, width=20)
P_input.grid(row=0, column=1)

Label(GUI, text="Outside Diameter (D)").grid(row=1, column=0, padx=10, pady=5)
D_input = Entry(GUI, width=20)
D_input.grid(row=1, column=1)

Label(GUI, text="Allowable Stress (S)").grid(row=2, column=0, padx=10, pady=5)
S_input = Entry(GUI, width=20)
S_input.grid(row=2, column=1)

Label(GUI, text="Quality Factor (E)").grid(row=3, column=0, padx=10, pady=5)
E_input = Entry(GUI, width=20)
E_input.grid(row=3, column=1)

Label(GUI, text="Weld Joint Factor (W)").grid(row=4, column=0, padx=10, pady=5)
W_input = Entry(GUI, width=20)
W_input.grid(row=4, column=1)

Label(GUI, text="Coefficient (Y)").grid(row=5, column=0, padx=10, pady=5)
Y_input = Entry(GUI, width=20)
Y_input.grid(row=5, column=1)

Label(GUI, text="Corrosion Allowance (c)").grid(row=6, column=0, padx=10, pady=5)
c_input = Entry(GUI, width=20)
c_input.grid(row=6, column=1)

# Button and Result Label
Button(GUI, text="Calculate", command=calculate).grid(row=7, column=0, columnspan=1, pady=10)

result_var = StringVar()
Label(GUI, textvariable=result_var, fg="blue").grid(row=8, column=0, columnspan=2)

GUI.mainloop()
