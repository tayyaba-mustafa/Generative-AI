import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Function to perform the basic arithmetic operations
def basic_operations(operation, num1, num2=None):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Zero Division Error: Division by zero is not allowed."
    elif operation == 'power':
        return math.pow(num1, num2)
    else:
        return "Invalid Operation"

# Function to perform scientific operations
def scientific_operations(operation, num1):
    if operation == 'sin':
        return math.sin(num1)
    elif operation == 'cos':
        return math.cos(num1)
    elif operation == 'tan':
        return math.tan(num1)
    elif operation == 'log':
        if num1 > 0:
            return math.log(num1)
        else:
            return "Error: Logarithm of non-positive number"
    elif operation == 'sqrt':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error: Square root of negative number"
    elif operation == 'exp':
        return math.exp(num1)
    else:
        return "Invalid Operation"

# Function to plot a mathematical function
def plot_function(func, start=-10, end=10):
    x = np.linspace(start, end, 400)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f'Graph of {func.__name__}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)
    st.pyplot(fig)

# Streamlit app structure
st.title("Scientific Graphical Calculator")

# User inputs for basic operations
num1 = st.number_input("Enter Number 1", value=0.0)
num2 = st.number_input("Enter Number 2 (if applicable)", value=0.0)

operation = st.selectbox("Choose an Operation", 
                         ['add', 'subtract', 'multiply', 'divide', 'power', 'sin', 'cos', 'tan', 'log', 'sqrt', 'exp'])

# Button to perform the operation
if st.button("Calculate"):
    if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
        result = basic_operations(operation, num1, num2)
    else:
        result = scientific_operations(operation, num1)
    
    st.write(f"Result: {result}")

# Graphing section
graph_func = st.selectbox("Select a function to plot", ['None', 'sin', 'cos', 'tan', 'log', 'exp'])

if graph_func != 'None':
    if graph_func == 'sin':
        func = np.sin
    elif graph_func == 'cos':
        func = np.cos
    elif graph_func == 'tan':
        func = np.tan
    elif graph_func == 'log':
        func = np.log
    elif graph_func == 'exp':
        func = np.exp
    
    st.write(f"Plotting {graph_func} function")
    plot_function(func)
