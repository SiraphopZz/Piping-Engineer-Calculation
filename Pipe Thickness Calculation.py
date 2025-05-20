import pandas as pd

#Wall thickness calculation ASME31.3
def require_wall_thickness(P, D, S, E, W, Y, c):

    t = (P * D) / (2 * (S * E * W + P * Y))
    return t + c

#Main program
print('-'*30 + 'Pipe Thickness Calculator ASME31.3' + '-'*30 + '\n')

#Input Value
try:
    P = float(input('Internal Design Gauge Pressure P (MPa): '))
    D = float(input("Pipe Outside Diameter D (mm): "))
    S = float(input("Stress Value for Material (S): "))
    E = float(input("Quality Factor (E): "))
    W = float(input("Weld Joint Strength Reduction Factor (W): "))
    Y = float(input("Coefficient from Table 304.1.1 (Y): "))
    c = float(input("Sum of Mechanical Allowance c (mm): "))
except ValueError:
    print("******Please enter numeric values only.******")
    exit()

#Calculate Min. Wall
t_m = round(require_wall_thickness(P, D, S, E, W, Y, c),3)
t_m_tolerance = round(t_m / 0.875, 3)

#Result of calculation
print("*** Minimum required thickness is: " + str(t_m) + " mm ***")
#Result of calculation considering mill tolerance
print("*** Minimum required thickness, considering mill tolerance is: " + str(t_m_tolerance) + " mm ***")

# Select next standard pipe thickness ≥ minimum required
pipe_db = pd.read_csv('Pipe Dimension DB.csv')
sel_thk = pipe_db[(pipe_db['OD (mm)']==D) & (pipe_db['Wall Thickness (mm)'] >= t_m_tolerance)]
print("\n< Recommended Pipe Thickness >\n")

if sel_thk.empty:
    print("******No pipe thickness available in the database.******")
else:
    print(sel_thk)


print('-'*45 + 'End' + '-'*45)

