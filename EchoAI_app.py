import os
import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Content Generator", page_icon="📝", layout="wide")

# Display the logo
logo = "logo.png"  # Replace with your logo file name
st.image(logo, width=200)  # Adjust width as necessary

# Page title
st.title("AI Content Generator for Social Media")
st.write("Generate engaging and creative content for social media using AI.")

# Sidebar
st.sidebar.header("Settings")
content_type = st.sidebar.selectbox("Select Content Type:", ["Tweet", "Instagram Caption", "LinkedIn Post", "Facebook Post"])
max_length = st.sidebar.slider("Max Length of Generated Content", 50, 300, 150)
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# New feature: Brand Voice Integration
st.sidebar.header("Brand Voice Integration")
brand_tone = st.sidebar.selectbox("Select Brand Tone:", ["Friendly", "Professional", "Casual", "Formal"])
brand_style = st.sidebar.selectbox("Select Writing Style:", ["Conversational", "Informative", "Persuasive", "Playful"])

# Input for user prompt
prompt = st.text_area("Enter your content prompt:", help="Type a brief idea for your social media post.")

# Placeholder function to simulate content generation (replace with actual API call)
def generate_content_with_groq(prompt, tone, style):
    # Combine the user prompt with the selected brand tone and style
    brand_prompt = f"Generate a {content_type} in a {tone} tone and {style} style. {prompt}"
    
    # Simulating the response (replace this with an actual call to Groq API)
    return f"[Simulated Groq Llama Content] {brand_prompt}"

# Button to generate content
if st.button("Generate Content"):
    if prompt:
        with st.spinner('Generating content...'):
            generated_content = generate_content_with_groq(prompt, brand_tone, brand_style)
            st.success("Generated Content:")
            st.write(generated_content)
    else:
        st.error("Please enter a prompt to generate content.")

# Footer
st.write("© 2024 Echo AI Content Generator")
