import streamlit as st

st.set_page_config(page_title="St. Matthew Hospital",
                   page_icon="lungs",
                   layout="wide",

                   initial_sidebar_state="expanded")

st.markdown(f'<h1 style="color:#7E587E;font-size:50px;">{"St. Matthew Hospital, Lisbon"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:40px;">{"Where expertise meets innovation"}</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
        hr {
            border: 2px solid #7E587E;  /* Dark purple nude color */
            margin: 15px 0;  /* Adjust margin as needed */
        }
    </style>
    """,
    unsafe_allow_html=True)
st.markdown("---") # Separator line

col1,col2 = st.columns(2)
col1.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 23px;">
        Specialized in lung care, we leverage our services with Machine Learning to
        ensure the highest standard of respiratory health.<br>
           <br>
        <b>Matthew</b>, our CXR-Tool is learning to identify individuals at an elevated risk of developing lung cancer and 
        our advanced technology aims to make screening more accessible, prioritizing the safety and affordability of X-rays.<br>
           <br>
        <b>The future of HealthCare is now!</b>
    </div>
""", unsafe_allow_html=True)
col2.image("https://www.mayoclinic.org/-/media/kcms/gbs/patient-consumer/images/2019/10/28/15/57/roch-hero-828x386-3714034-0006.jpg?la=en&hash=BE3BADC0E9C99C515B7559EC06F31533BA94EC8D")
st.write("---") ### separator


col3,col4,col5 = st.columns([1,3,2])
col4.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 24px;">
        St Matthew Hospital was honored with an award for a new
        and groundbreaking contribution to the latest scientific 
        research in healthcare.
        <br>
        <br>
        "YOLOv5-based Matthew X-ray Tool for Findings Detection and Validation
         in a Hospital-Scale Chest X-ray Database"
    </div>
""", unsafe_allow_html=True)

col5.image("https://healthitanalytics.com/images/site/article_headers/_normal/Getty_correct_size_AI_lung.jpg")

col3.image("https://cdn.statcdn.com/LandingPages/9e7ed43ebb74d5c6d173f8e93140b610.png")
st.write("---") 