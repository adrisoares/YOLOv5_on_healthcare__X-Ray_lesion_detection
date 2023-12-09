import streamlit as st
from datetime import datetime, timedelta
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Online Booking",
    page_icon="date",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown(f'<h1 style="color:#000000;font-size:40px;">{"Online Booking"}</h1>', unsafe_allow_html=True)
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
#st.markdown("---") # Separator line

st.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 24px;">
    According with the current lung cancer screening recommendations, individuals aged between 
    55 and 74 who have a history of smoking are eligible for lung screening under the national healthcare system (SNS).
    </div>
""", unsafe_allow_html=True)
st.write("---") ### separator

col1,col2, col3 = st.columns(3)
col1.text_input("First Name")
col2.text_input("Last Name")
col3.date_input("Enter your date of birth", datetime.today() - timedelta(days=365*60))
col3.text_input("Enter your SNS user number")
a = col1.date_input("Preference Date")
b = col2.time_input("Preference Schedule")
st.write(f"""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 22px;">
        <b>Your preference booking is on {a} at {b}</b>
    </div>
""", unsafe_allow_html=True)
st.write("---") ### separator
st.write("""
""")

st.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 24px; color: #000000;">
    We will prioritize eligible individuals and anyone who exhibits at least one of the symptoms listed below:
    </div>
""", unsafe_allow_html=True)
st.write("""
""")
symptoms_list = [
    "Cough that does not go away after 3 weeks",
    "Chest infections that keep coming back",
    "Existing cough that changes or gets worse",
    "Coughing up blood",
    "Being short of breath a lot",
    "Unexplained tiredness",
    "Ache or pain when breathing or coughing",
    "Loss of appetite or unexplained weight loss"]

selected_symptom = st.selectbox("Use the drop down menu", symptoms_list)

add_to_file = st.checkbox("Add to my file")
if st.button("Add to File"):
    if add_to_file:
        st.write(f"Added {selected_symptom} to your file.")
    else:
        st.write("File not updated.")
