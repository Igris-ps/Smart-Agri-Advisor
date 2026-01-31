import streamlit as st
from backend.text_handler import classify_text_query
from backend.image_handler import analyze_image
from backend.advisory_engine import generate_advice

st.title("🌾 AI-Based Farmer Advisory System")

st.write("Enter your problem or upload a crop image")

query = st.text_input("Describe your problem")
image = st.file_uploader("Upload crop image", type=["jpg", "png", "jpeg"])

if st.button("Get Advice"):
    if query:
        problem_type = classify_text_query(query)
    elif image:
        problem_type = analyze_image(image)
    else:
        problem_type = "unknown"

    result = generate_advice(problem_type)

    st.subheader("Identified Issue")
    st.write(result["issue"])

    st.subheader("Recommended Actions")
    for step in result["advice"]:
        st.write("•", step)
