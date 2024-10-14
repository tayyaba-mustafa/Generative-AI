import streamlit as st

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app title
st.title("Simple Calculator")

# Dropdown for selecting the operation
operation = st.selectbox(
    "Select an operation:",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Input fields for the numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Perform calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"The result is: {result}")
