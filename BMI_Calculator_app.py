import streamlit as st

# Set the page layout
st.set_page_config(page_title="BMI Calculator & Health Advisor", page_icon="⚖️", layout="centered")

# Title and subtitle
st.title("⚖️ BMI Calculator and Health Advisor")
st.write("Calculate your Body Mass Index (BMI) and get personalized health advice based on your result.")

# User input with more appealing widgets and hints
st.header("Enter Your Details:")
weight = st.number_input("💪 Enter your weight (in kg):", min_value=0.0, step=0.1, help="Your weight should be a positive number in kilograms.")
h_ft = st.number_input("🔢 Enter your height (Feet):", min_value=0, step=1, help="Feet value should be a positive integer.")
h_inch = st.number_input("🔢 Enter your height (Inches):", min_value=0, step=1, help="Inches value should be between 0 and 11.")

# Add a BMI calculation button
if st.button("🧮 Calculate BMI"):
    if weight <= 0 or h_ft <= 0 and h_inch <= 0:
        st.error("🚨 Weight and height must be positive numbers.")
    else:
        # Convert height from feet and inches to meters
        h_m = (h_ft * 0.3048) + (h_inch * 0.0254)

        # Calculate BMI
        BMI = weight / (h_m * h_m)
        st.success(f"**Your BMI is:** {BMI:.2f} kg/m²")

        # Provide dynamic results based on BMI
        if BMI < 18.5:
            st.markdown("<h3 style='color:orange;'>You are in the Underweight range. 🍂</h3>", unsafe_allow_html=True)
            st.subheader("🎯 Goal: Increase calorie intake to gain weight.")
            st.write("""
                **📝 Advice:**
                - Focus on nutrient-dense foods like whole grains, lean proteins, fruits, and vegetables.
                - Consult a dietitian for a personalized meal plan.
                - Incorporate regular strength training to build muscle mass.
                """)
        elif 18.5 <= BMI <= 24.9:
            st.markdown("<h3 style='color:green;'>You are in the Healthy weight range. 🌿</h3>", unsafe_allow_html=True)
            st.subheader("🎯 Goal: Maintain a healthy weight.")
            st.write("""
                **📝 Advice:**
                - Continue a balanced diet with a variety of foods.
                - Aim for regular physical activity, including both cardio and strength training.
                - Manage stress through techniques like meditation or yoga.
                """)
        elif 25 <= BMI <= 29.9:
            st.markdown("<h3 style='color:gold;'>You are in the Overweight range. ⚖️</h3>", unsafe_allow_html=True)
            st.subheader("🎯 Goal: Lose weight gradually.")
            st.write("""
                **📝 Advice:**
                - Reduce calorie intake and increase physical activity.
                - Focus on whole, unprocessed foods and portion control.
                - Consult a dietitian for a personalized meal plan.
                """)
        elif 30 <= BMI <= 34.9:
            st.markdown("<h3 style='color:red;'>You are in the Obese range. ❗</h3>", unsafe_allow_html=True)
            st.subheader("🎯 Goal: Lose weight and improve overall health.")
            st.write("""
                **📝 Advice:**
                - Create a personalized weight loss plan with a healthcare professional or registered dietitian.
                - Incorporate a combination of diet and exercise.
                - Address any underlying health conditions that may be contributing to weight gain.
                """)
        else:
            st.markdown("<h3 style='color:darkred;'>You are in the Morbid obesity range. ❌</h3>", unsafe_allow_html=True)
            st.subheader("🎯 Goal: Lose weight and improve overall health.")
            st.write("""
                **📝 Advice:**
                - Create a personalized weight loss plan with a healthcare professional or registered dietitian.
                - Incorporate a combination of diet and exercise.
                - Address any underlying health conditions that may be contributing to weight gain.
                """)

# Add a footer with additional resources
st.markdown("""
    ---
    **Additional Resources:**
    - [WHO BMI Guidelines](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
    - [Healthy Eating Tips](https://www.choosemyplate.gov)
""")


       
            
            
