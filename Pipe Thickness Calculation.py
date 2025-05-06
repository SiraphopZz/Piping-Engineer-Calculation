#Pipe Thickness Calculation ASME31.3

def require_wall_thickness(P, D, S, E, W, Y, c):
    """
    P = internal design gage pressure
    D = outside diameter
    S = stress value
    E = quality factor
    W = weld joint factor
    Y = coefficient from table 304.1.1
    c = corrosion allowance
    """

    t = (P*D) / [2 *(S*E*W + P*Y)]
    
    return t + c