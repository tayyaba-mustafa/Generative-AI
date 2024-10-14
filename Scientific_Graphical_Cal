import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to perform the basic arithmetic operations
def basic_operations(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2 if num2 != 0 else "Error (Division by Zero)"
    else:
        return "Invalid Operation"

# Function to perform scientific operations
def scientific_operations(operation, num1):
    if operation == 'Sine':
        return math.sin(num1)
    elif operation == 'Cosine':
        return math.cos(num1)
    elif operation == 'Tangent':
        return math.tan(num1)
    elif operation == 'Logarithm':
        return math.log(num1) if num1 > 0 else "Error (Log of non-positive)"
    elif operation == 'Square Root':
        return math.sqrt(num1) if num1 >= 0 else "Error (Square root of negative)"
    elif operation == 'Exponential':
        return math.exp(num1)
    elif operation == 'Power':
        num2 = st.number_input("Enter the power:", value=2.0)
        return math.pow(num1, num2)
    else:
        return "Invalid Operation"

# Function to plot a mathematical function
def plot_function(func, start=-10, end=10):
    x = np.linspace(start, end, 400)
    y = func(x)
    plt.plot(x, y)
    plt.title(f'Graph of {func.__name__}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    st.pyplot(plt)

# Streamlit UI
st.title("Scientific Graphical Calculator")

# Sidebar for choosing operation type
operation_type = st.sidebar.selectbox("Select Operation Type:", ["Basic", "Scientific", "Graphing"])

if operation_type == "Basic":
    st.header("Basic Operations")
    
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    operation = st.selectbox("Choose Operation", ['Add', 'Subtract', 'Multiply', 'Divide'])
    
    if st.button("Calculate"):
        result = basic_operations(operation, num1, num2)
        st.write(f"Result: {result}")

elif operation_type == "Scientific":
    st.header("Scientific Operations")
    
    num1 = st.number_input("Enter number:", value=0.0)
    operation = st.selectbox("Choose Operation", ['Sine', 'Cosine', 'Tangent', 'Logarithm', 'Square Root', 'Exponential', 'Power'])
    
    if st.button("Calculate"):
        result = scientific_operations(operation, num1)
        st.write(f"Result: {result}")

elif operation_type == "Graphing":
    st.header("Graph Mathematical Functions")
    
    func_name = st.selectbox("Choose Function to Graph", ['Sine', 'Cosine', 'Tangent', 'Exponential', 'Logarithm'])
    
    if func_name == 'Sine':
        func = np.sin
    elif func_name == 'Cosine':
        func = np.cos
    elif func_name == 'Tangent':
        func = np.tan
    elif func_name == 'Exponential':
        func = np.exp
    elif func_name == 'Logarithm':
        func = np.log
    
    if st.button("Plot Graph"):
        plot_function(func)
