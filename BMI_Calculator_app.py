import streamlit as st

# Title of the app
st.title("BMI Calculator and Health Advisor")

# Get user input
weight = st.number_input("Enter your weight (in kg)", min_value=0.0, step=0.1)
h_ft = st.number_input("Enter your height (Feet)", min_value=0, step=1)
h_inch = st.number_input("Enter your height (Inches)", min_value=0, step=1)

# Calculate BMI when the button is clicked
if st.button("Calculate BMI"):
    if weight <= 0 or h_ft <= 0 and h_inch <= 0:
        st.error("Weight and height must be positive numbers.")
    else:
        # Convert height from feet and inches to meters
        h_m = (h_ft * 0.3048) + (h_inch * 0.0254)

        # Calculate BMI
        BMI = weight / (h_m * h_m)
        st.write(f"**Your BMI is:** {BMI:.2f} kg/m²")

        # BMI ranges and advice
        if BMI < 18.5:
            st.write("Your BMI indicates that you are in the **Underweight** range.")
            st.subheader("Goal: Increase calorie intake to gain weight.")
            st.write("""
            **Advice:**
            - Focus on nutrient-dense foods like whole grains, lean proteins, fruits, and vegetables.  
            - Consult a dietitian for a personalized meal plan.  
            - Incorporate regular strength training to build muscle mass.
            """)
        elif 18.5 <= BMI <= 24.9:
            st.write("Your BMI indicates that you are in the **Healthy weight** range.")
            st.subheader("Goal: Maintain a healthy weight.")
            st.write("""
            **Advice:**
            - Continue a balanced diet with a variety of foods.  
            - Aim for regular physical activity, including both cardio and strength training.  
            - Manage stress through techniques like meditation or yoga.
            """)
        elif 25 <= BMI <= 29.9:
            st.write("Your BMI indicates that you are in the **Overweight** range.")
            st.subheader("Goal: Lose weight gradually.")
            st.write("""
            **Advice:**
            - Reduce calorie intake and increase physical activity.  
            - Focus on whole, unprocessed foods and portion control.  
            - Consult a dietitian for a personalized meal plan.
            """)
        elif 30 <= BMI <= 34.9:
            st.write("Your BMI indicates that you are in the **Obese** range.")
            st.subheader("Goal: Lose weight and improve overall health.")
            st.write("""
            **Advice:**
            - Create a personalized weight loss plan with a healthcare professional or registered dietitian.  
            - Incorporate a combination of diet and exercise.  
            - Address any underlying health conditions that may be contributing to weight gain.
            """)
        else:
            st.write("Your BMI indicates that you are in the **Morbid obesity** range.")
            st.subheader("Goal: Lose weight and improve overall health.")
            st.write("""
            **Advice:**
            - Create a personalized weight loss plan with a healthcare professional or registered dietitian.  
            - Incorporate a combination of diet and exercise.  
            - Address any underlying health conditions that may be contributing to weight gain.
            """)
