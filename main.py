import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def angular_fluc(OmegaGW, OBSperiod=True,Freq=False):
    
    
    alpha_list=[0.833333, 0.116667, 0.03, 0.0104762, 0.00442177, 0.00212585, 0.00112434, 0.000639731, 0.000385675, 0.000243696]
    
    #Calculating Sigma
    sigma = lambda f: OmegaGW / (f**2 * (np.trapz((f**-3) * OmegaGW, f)))
    
    #Calculate theta RMS for E and B modes
    theta_rms = lambda f, H: np.sqrt(np.trapz(H**2/f**3)*OmegaGW)
    

def create_function(expression, variable_names):
    print(variable_names)
    variables = symbols(variable_names)
    expr = sympify(expression)
    f = lambdify(variables, expr)
    print(f"Function created: f({', '.join(variable_names)}) = {expression}")
    return f

expression = input("Enter the mathematical expression: ")
variable_names = [var.strip() for var in input("Enter the variable names (separated by commas): ").split(",")]
print(variable_names)
function = create_function(expression, variable_names)

# Example usage
values = input(f"Enter values for {', '.join(variable_names)} (separated by commas): ").split(",")
values = [float(val.strip()) for val in values]
result = function(*values)
print(f"f({', '.join(map(str, values))}) = {result}")
