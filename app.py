import streamlit as st
import requests

st.title("Speech-to-Text with wav2vec")
st.write("Upload a WAV file to transcribe")

uploaded_file = st.file_uploader("Choose a WAV file", type="wav")
if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, "audio/wav")}
    response = requests.post("http://localhost:8000/transcribe", files=files)
    transcription = response.json()["transcription"]
    
    st.write("Transcription:")
    st.write(transcription)
