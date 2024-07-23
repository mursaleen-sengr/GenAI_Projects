
import requests
import streamlit as st


def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


st.title('Langchain Demo With LLAMA3 by making  API')
input_text=st.text_input("Write an essay on")




if input_text:
    st.write(get_ollama_response(input_text))