import streamlit as st

st.set_page_config(
    page_title="Fresh News",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown(f'<h1 style="color:#000000;font-size:40px;">{"Fresh News"}</h1>', unsafe_allow_html=True)
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

col1, col2 = st.columns([2, 2])
col1.image("article1.jpg", width=450) 
if col1.button("Read article 1"):
    st.markdown("https://healthitanalytics.com/news/deep-learning-model-flags-non-smokers-at-increased-risk-for-lung-cancer", unsafe_allow_html=True)
col2.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 18px;">
    "A deep learning model can accurately identify non-smokers at high risk for lung cancer using only routine chest X-rays,
    according to research presented at this year’s meeting of the Radiological Society of North America (RSNA)"
    </div>
""", unsafe_allow_html=True)

col3, col4 = st.columns([2, 2])
col3.image("article2.jpg", width=450) 
if col3.button("Read article 2"):
    st.markdown("https://pubmed.ncbi.nlm.nih.gov/32866413/", unsafe_allow_html=True)
col4.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 18px;">
    "The CXR-LC model identified smokers at high risk for incident lung cancer, beyond 
     CMS eligibility and using information commonly available in the EMR"
    </div>
""", unsafe_allow_html=True)

col5, col6 = st.columns([2, 2])
col5.image("article3.jpg", width=460) 
if col5.button("Read article 3"):
    st.markdown("https://arxiv.org/abs/1705.02315", unsafe_allow_html=True)
col6.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 18px;">
    "The chest X-ray is one of the most commonly accessible radiological examinations for screening and diagnosis of many lung diseases."
    </div>
""", unsafe_allow_html=True)

col7, col8 = st.columns([2, 2])
col7.image("article4.jpg", width=460) 
if col7.button("Read article 4"):
    st.markdown("https://pubmed.ncbi.nlm.nih.gov/37761345/", unsafe_allow_html=True)
col8.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 18px;">
    "Our research focused on creating an advanced machine-learning algorithm that accurately detects anomalies in 
    chest X-ray images to provide healthcare professionals with a reliable tool for diagnosing various lung conditions."
    </div>
""", unsafe_allow_html=True)

col9, col10 = st.columns([2, 2])
col9.image("article5.jpg", width=460) 
if col9.button("Read article 5"):
    st.markdown("https://healthitanalytics.com/news/deep-learning-model-identifies-lung-cancer-risk-using-chest-x-rays", unsafe_allow_html=True)
col10.write("""
    <div style="text-align: left; font-family: 'Arial', sans-serif; font-size: 18px;">
    "In a recent study, researchers validated a deep-learning (DL) model to predict lung cancer risk using chest radiographs and EMR data."
    </div>
""", unsafe_allow_html=True)