#Wall thickness calculation as per ASME31.3
def require_wall_thickness(P, D, S, E, W, Y, c):
    t = (P * D) / (2 * (S * E * W + P * Y))
    return t + c

#Start Program
print('-'*20 + 'Pipe Thickness Calculator' + '-'*20)

#Input Value
P = float(input('Internal Design Gauge Pressure P(MPa): '))
D = float(input("Pipe Outside Diameter D(mm): "))
S = float(input("Stress Value for Material (S): "))
E = float(input("Quality Factor (E): "))
W = float(input("Weld Joint Strength Reduction Factor (W): "))
Y = float(input("Coefficient from Table 304.1.1 (Y): "))
c = float(input("Sum of Mechanical Allowance c(mm): "))

#Calculate Min. Wall
t_m = round(require_wall_thickness(P, D, S, E, W, Y, c),2)

#Result of calculation
print("*** Minimum required thickness is: " + str(t_m) + " mm ***")

print('-'*31 + 'End' + '-'*31)

