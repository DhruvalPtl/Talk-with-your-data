#Talk With Your Data
import streamlit as st
import google.generativeai as genai
import pandas as pd

def read_file():
    # Read the CSV file
    df = pd.read_csv('data.csv')
    return df

api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)
model_name = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name=model_name)


st.title("Talk With Your Data")
with st.sidebar:
    st.write("This is a sidebar")
    st.text_input("API key",type="password")
    file = st.file_uploader("Upload CSV file")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
if prompt := st.chat_input():
    st.session_state.messages.append({"role":"human","content": prompt})
    st.chat_message("human").write(prompt)
    response = model.generate_content(prompt)
    st.session_state.messages.append({"role":"ai","content": response.text})
    st.chat_message("ai").write(response.text)
    