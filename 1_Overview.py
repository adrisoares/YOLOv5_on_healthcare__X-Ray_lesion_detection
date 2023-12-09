import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Overview",
    page_icon=":medical_symbol:",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown(f'<h1 style="color:#000000;font-size:40px;">{"Powered by Patient Data"}</h1>', unsafe_allow_html=True)
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
    At St. Matthew Hospital, <b>we learn from the best!</b> Our most valuable insights to date rely on your
    collaboration and trust in our hospital, providing us with the right tools to innovate and work 
    toward cancer prevention.
    </div>
""", unsafe_allow_html=True)
st.write("""
         """)
st.write("""
         """)
st.markdown("---") # Separator line

#### Number of x-rays #####
feat = pd.read_csv("C:\Armazenamento\Imagens\Data_Entry_2017.csv")
def label_function(x):
    for label in ["No Finding"]:
        if label in x:
            return label
    return "Suspicious"
feat_presentation = feat["Finding Labels"].apply(label_function)
data = feat_presentation.value_counts()

col1, col2, col3 = st.columns([1,1.6,0.7])
fig, ax = plt.subplots(figsize=(4, 2))
data.plot(kind='bar', ax=ax, color=['#7E587E', 'tan', 'lightpink'])
ax.set_ylabel('Number of Findings')
ax.set_title('Chest X-Ray distribution')
col1.write("""
""")
col1.pyplot(fig)
content = """
    <br>
    <br>
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 20px;">
        <b>The plot illustrates the distribution of Chest X-Rays (CXR) and since our 
        establishment in 2020, we have conducted over 110,000 exams.<b>
    </div>

    <br>
    <br>
    <br>

    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 20px;">
        <b>The circular diagram illustrates the correlation of all main findings,
        showing that often one occurrence is associated with another.<b>  
    </div>
"""
col2.write(content, unsafe_allow_html=True)
col3.image("combination.png", width=320)
st.markdown("---") # Separator line
st.write("""
""")


col4, col5,col6 = st.columns([1,1.1,1])
col4.write("""
""")
col4.image("graph.png", width=420)
col5.write("""
""")
col5.write("""
""")
content_1 = """
    <br>
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 21px;">
        <b>To enhance Matthew's precision and accuracy, we instructed him to recognize only unique events.<b>
    </div>
    <br>
    <br>
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 21px;">
        <b>Still, this proved to be a demanding task for fully-automated diagnosis, because unique events are also smaller
           and harder to detect!<b>  
    </div>
"""
col5.write(content_1, unsafe_allow_html=True)

col6.write("""
""")
col6.write("""
""")
col6.write("""
""")
col6.image("88.png", width=460)
col6.write("""
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 16px;">
    Eight illustrative examples and the pathological findings 
    </div>
""", unsafe_allow_html=True)
col6.write("""
""")
st.markdown("---") # Separator line
st.write("""
""")


col7,col8 = st.columns([2,1.75])

col7.image("robotflow.jpg", width=700)
col7.write("""
""")
col7.write("""
""")
col8.write("""
    <br>
    <br>      
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 22px;">
    <b>Fortunately we have already in our database about 1000 labeled images - enough just to start off the training.<b>
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 22px;">
    <br>
    <b>Coordinates normalization and tranform them into YOLO's format.
    </div>
""", unsafe_allow_html=True)
col7.write("""
    <div style="text-align: center; font-family: 'Arial', sans-serif; font-size: 16px;">
    Annotation example using Robotflow
    </div>
""", unsafe_allow_html=True)
