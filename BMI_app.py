import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to provide health advice based on BMI
def health_advice(bmi):
    if bmi < 18.5:
        return "You are underweight. It is advisable to eat a nutritious and balanced diet to reach a healthy weight."
    elif 18.5 <= bmi < 24.9:
        return "You have a healthy weight. Maintain a balanced diet and regular physical activity to stay healthy."
    elif 25 <= bmi < 29.9:
        return "You are overweight. Consider a healthy eating plan and increase physical activity to reduce your BMI."
    else:
        return "You are in the obese category. It is advisable to consult a healthcare professional for personalized advice."

# Streamlit App
def main():
    st.title("BMI Calculator and Health Advisor")

    st.write("### Enter your details below:")

    weight = st.number_input("Enter your weight in kilograms (kg):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height in meters (m):", min_value=0.0, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"### Your BMI is: {bmi}")

            advice = health_advice(bmi)
            st.write(f"### Health Advice: {advice}")
        else:
            st.write("Please enter a valid height.")

if __name__ == '__main__':
    main()
