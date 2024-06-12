# 설치 필요
# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI

st.title('🍎--- ai훈장샘  🥝---')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', '예)공자는 무엇을 중요히 여겼는가?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    prompt = """
    [system]: 
    챗봇의 역할  : 너는 논어의 내용을 묻고 답하는 챗봇이란다. 논어이외의 내용에 대해서는 답변하지 말라.
    아래 사용자 입력 이후로 들어오는 내용에 대해 논어 전문가로서 답변을 부탁해.
    사용자 입력 :
    """
    all_prompt = prompt + text
    generate_response(all_prompt)