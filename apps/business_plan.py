import streamlit as st
from pymongo import MongoClient
import json
from apps.api import *

with open('params.json', 'r') as f:
    params = json.load(f)
    sequoia_guideline = params['sequoia']


st.title("Business Plan")
if "bp" not in st.session_state:
    st.session_state.bp = {}

# Chat Input 
input_text = st.chat_input("Input your thoughts here:", key="business_plan")
if input_text:
    with st.spinner("Generating your business plan..."):
        st.session_state.bp = generate_bp(sequoia_guideline, input_text)
        
## Section 1: Company Purpose
key1 = "Company purpose"
with st.expander(key1):
    st.write(sequoia_guideline[key1])   
st.text_area(
    label="company_purpose",
    value=st.session_state.bp.get(key1, ""),    
    label_visibility="collapsed",
    key="company_purpose"
)

## Section 2: Problem
key2 = "Problem"
with st.expander(key2):
    st.write(sequoia_guideline[key2])
st.text_area(
    label="problem",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key2, ""),
    key="problem"
)

## Section 3: Solution
key3 = "Solution"
with st.expander(key3):
    st.write(sequoia_guideline[key3])
st.text_area(
    label="solution",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key3, ""),
    key="solution"
)

key4 = "Why now?"
with st.expander(key4):
    st.write(sequoia_guideline[key4])
st.text_area(
    label="why_now",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key4, ""),
    key="why_now"
)      

key5 = "Market potential"
with st.expander(key5):
    st.write(sequoia_guideline[key5])
st.text_area(
    label="market_potential",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key5, ""),
    key="market_potential"
)      

key6 = "Competition / alternatives"
with st.expander(key6):
    st.write(sequoia_guideline[key6])
st.text_area(
    label="competition",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key6, ""),
    key="competition"
)      

key7 = "Business model"
with st.expander(key7):
    st.write(sequoia_guideline[key7])
st.text_area(
    label="business_model",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key7, ""),
    key="business_model"
)      

key8 = "Team"
with st.expander(key8):
    st.write(sequoia_guideline[key8])
st.text_area(
    label="team",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key8, ""),
    key="team"
)   

key9 = "Financials"
with st.expander(key9):
    st.write(sequoia_guideline[key9])
st.text_area(
    label="financials",
    label_visibility="collapsed",
    value=st.session_state.bp.get(key9, ""),
    key="financials"
)      




