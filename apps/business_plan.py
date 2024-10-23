import streamlit as st
from pymongo import MongoClient
import json
from apps.api import *

with open('params.json', 'r') as f:
    params = json.load(f)
    sequoia_guideline = params['sequoia']


st.title("Business Plan")
if "bp" not in st.session_state:
    st.session_state.bp = sequoia_guideline.keys() 

# Chat Input 
input_text = st.chat_input("Input your thoughts here:", key="business_plan")
if input_text:
    with st.spinner("Generating your business plan..."):
        st.session_state.bp = generate_bp(sequoia_guideline, input_text)
        
## Section 1: Company Purpose
with st.expander("Company Purpose"):
    st.write(sequoia_guideline["Company purpose"])
st.text_area(
    label="company_purpose",
    value=st.session_state.bp["Company purpose"],
    label_visibility="collapsed",
    key="company_purpose"
)

## Section 2: Problem
with st.expander("Problem"):
    st.write(sequoia_guideline["Problem"])
st.text_area(
    label="problem",
    label_visibility="collapsed",
    placeholder="""Entrepreneurs struggle to formulate their business plans""", 
    key="problem"
)

## Section 3: Solution
with st.expander("Solution"):
    st.write(sequoia_guideline["Solution"])
st.text_area(
    label="solution",
    label_visibility="collapsed",
    placeholder="""We solve the problem by providing a platform that helps entrepreneurs formulate their business plans""", 
    key="solution"
)

with st.expander("Why Now?"):
    st.write(sequoia_guideline["Why now?"])
st.text_area(
    label="why_now",
    label_visibility="collapsed",
    placeholder="""The market is growing and the technology is mature""", 
    key="why_now"
)      

with st.expander("Market Potential"):
    st.write(sequoia_guideline["Market potential"])
st.text_area(
    label="market_potential",
    label_visibility="collapsed",
    placeholder="""The market is large and growing""", 
    key="market_potential"
)      

with st.expander("Competition / Alternatives"):
    st.write(sequoia_guideline["Competition / alternatives"])
st.text_area(
    label="competition",
    label_visibility="collapsed",
    placeholder="""The main competitors are other business plan platforms""", 
    key="competition"
)      

with st.expander("Business Model"):
    st.write(sequoia_guideline["Business model"])
st.text_area(
    label="business_model",
    label_visibility="collapsed",
    placeholder="""We make money by charging a subscription fee""", 
    key="business_model"
)      

with st.expander("Team"):
    st.write(sequoia_guideline["Team"])
st.text_area(
    label="team",
    label_visibility="collapsed",
    placeholder="""We have a team of experienced entrepreneurs and technologists""", 
    key="team"
)   

with st.expander("Financials"):
    st.write(sequoia_guideline["Financials"])
st.text_area(
    label="financials",
    label_visibility="collapsed",
    placeholder="""We expect to make $100,000 in revenue this year""", 
    key="financials"
)      




