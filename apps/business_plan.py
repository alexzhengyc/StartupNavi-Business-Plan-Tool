import os
import streamlit as st
import json
from apps.api import *



def load_bp():
    try:
        with open(st.session_state.bp_selector, 'r') as f:
            st.session_state.bp = json.load(f)
    except Exception as e:
        st.error(f"Error loading business plan: {e}")
        st.session_state.bp = {}

def save_bp():
    st.session_state.bp["name"] = st.session_state.get("name", "")
    for key in sequoia_guideline.keys():
        st.session_state.bp[key] = st.session_state.get(key, "")

    filename = f"data/{st.session_state.bp['name']}_bp.json"
    with open(filename, 'w') as f:
        json.dump(st.session_state.bp, f)

def export_bp():
    markdown_content = st.session_state.bp["name"] + "\n\n"
    for key, value in st.session_state.bp.items():
        markdown_content += f"## {key.replace('_', ' ').title()}\n\n{value}\n\n"
    return markdown_content
    

with open('params.json', 'r') as f:
    params = json.load(f)
    sequoia_guideline = params['sequoia']

# Find all business plans in the data folder
business_plans = [f"data/{f}" for f in os.listdir('data') if f.endswith('bp.json')]
st.selectbox("Current Business Plan", business_plans, key="bp_selector", on_change=load_bp)

# Initialize session state for business plan
if "bp" not in st.session_state:
    load_bp()


name = st.text_input("Business Name", value=st.session_state.bp.get("name", ""))
st.title(name)

if st.button("Save"):
    save_bp()
st.download_button(label="Download Markdown", data=export_bp(), file_name=f"{st.session_state.bp['name']}.md")


# Example of using st.session_state.bp in a section
key1 = "company_purpose"
with st.expander(key1):
    st.write(sequoia_guideline.get(key1, ""))
st.text_area(
    label=key1,
    value=st.session_state.bp.get(key1, ""),
    label_visibility="collapsed",
    key=key1,
    on_change=lambda: st.session_state.bp.update({key1: st.session_state[key1]})
)

## Section 2: Problem
key2 = "problem"    
with st.expander(key2):
    st.write(sequoia_guideline[key2])
st.text_area(
    label=key2,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key2, ""),
    key=key2,
)

## Section 3: Solution
key3 = "solution"
with st.expander(key3):
    st.write(sequoia_guideline[key3])
st.text_area(
    label=key3,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key3, ""),
    key=key3,
)

key4 = "why_now"
with st.expander(key4):
    st.write(sequoia_guideline[key4])
st.text_area(
    label=key4,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key4, ""),
    key=key4,
)      

key5 = "market_potential"
with st.expander(key5):
    st.write(sequoia_guideline[key5])
st.text_area(
    label=key5,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key5, ""),
    key=key5,
)      

key6 = "competition"
with st.expander(key6):
    st.write(sequoia_guideline[key6])
st.text_area(
    label=key6,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key6, ""),
    key=key6,
)      

key7 = "business_model"
with st.expander(key7):
    st.write(sequoia_guideline[key7])
st.text_area(
    label=key7,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key7, ""),
    key=key7,
)      

key8 = "team"
with st.expander(key8):
    st.write(sequoia_guideline[key8])
st.text_area(
    label=key8,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key8, ""),
    key=key8,
)   

key9 = "financials"
with st.expander(key9):
    st.write(sequoia_guideline[key9])
st.text_area(
    label=key9,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key9, ""),
    key=key9,
)      

key10 = "vision"
with st.expander(key10):
    st.write(sequoia_guideline[key10])
st.text_area(
    label=key10,
    label_visibility="collapsed",
    value=st.session_state.bp.get(key10, ""),
    key=key10,
)      




