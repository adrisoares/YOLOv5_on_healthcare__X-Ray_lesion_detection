
import streamlit as st
import base64

st.set_page_config(page_title="Contacts",
                   page_icon=":calling:",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.markdown(f'<h1 style="color:#000000;font-size:40px;">{"Contacts"}</h1>', unsafe_allow_html=True)
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
st.markdown("---")  # separator


email = "adrisoaresborges@hotmail.com"
linkedin_profile_link = "https://www.linkedin.com/in/adriana-borges-769890272/"


linkedin_logo_path = 'link.jpg'
with open(linkedin_logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode('utf-8')


st.write("""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
        <div style="margin-bottom: 10px;">📧</div>
        <div style="font-size: 18px; margin-bottom: 20px;"><b>{}</b></div>
        <div>
            <a href="{}" target="_blank">
                <img src="data:image/jpeg;base64,{}" alt="LinkedIn Logo" style="width: 30px; height: 30px;">
            </a>
        </div>
        <div style="font-size: 18px; margin-top: 10px;">
            <b>
                <a href="{}" target="_blank">LinkedIn Profile</a>
            </b>
        </div>
    </div>
""".format(email, linkedin_profile_link, encoded_logo, linkedin_profile_link), unsafe_allow_html=True)


st.markdown("---")  # separator

st.markdown(
    f'<h1 style="color:#000000;font-size:40px; text-align: center;">{"Thank You (for every moment)!"}</h1>',
    unsafe_allow_html=True
)
st.image('IMG_2250.jpg', use_column_width=True)

st.markdown("---")  # separator