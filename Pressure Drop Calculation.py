#This program calculate pressure drop in pipe
from math import *

def Re(rho, V, D, mu):
    return (rho * V * D) / mu

def Darcy_Eq(f, L, D, V, g = 9.81):
    return f * (L/D) * (V**2/(2 * g))
    
def Colebrook_EQ(e, D, Re, iteration=100):
    f_old = 0.02
    for _ in range(iteration):
        f_new = (-2 * log10((e / (3.7 * D)) + 2.51 / (Re * sqrt(f_old)))) ** -2
        if abs(f_new - f_old) <= 0.0001:
            return f_new
        f_old = f_new

    print("Warning: Colebrook equation did not converge.")
    return None

#main program
print('-'*20 + 'Pressure Drop Calculation' + '-'*20)

#User input
L = float(input('Length of pipe, L (m): '))
D = float(input('Pipe inside diameter, D (m): '))
e = float(input('Pipe roughness, e: '))
V_dot = float(input('Flow rate, V_dot (m3/s): '))
rho = float(input('Fluid density, rho (kg/m3): '))
mu = float(input('Fluid viscosity, mu (Pa.s): '))

#Calculation part
V = V_dot / (pi*D**2/4)         #Calculate flow velocity (m/s)
Reynolds = Re(rho, V, D, mu)    #Reynolds Number
print(f"Reynolds number is: {Reynolds:.2f}")

#Check type of flow amd calculate
if Reynolds < 2100:             #laminar flow
    f = 64/Reynolds
    h_f = Darcy_Eq(f, L, D, V)
    print(f'Friction factor is: {f:.4f}')
    print(f'The head loss due to friction is {h_f:.2f} m')
    
elif Reynolds > 4000:           #turbulent flow
    f = Colebrook_EQ(e, D, Reynolds)
    if f is None:
        print('Friction factor is undefined.')
    else:
        h_f = Darcy_Eq(f, L, D, V)
        print(f'Friction factor is: {f:.4f}')
        print(f'The head loss due to friction is {h_f:.2f} m')

else:                           #Critical Zone
    print("Flow type is in critical region")

print('-'*30 + 'End' + '-'*30)
