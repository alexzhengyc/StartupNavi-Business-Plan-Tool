import streamlit as st

pages = {
    "Business Plan": [
        st.Page("apps/business_plan.py", title="Create your business plan", icon="💡"),
        st.Page("apps/startup_database.py", title="Startup Database Search", icon="🔍")
    ],
    "Resources": [
        st.Page("resources/welcome.py", title="Welcome", icon="👋"),
        st.Page("resources/list.py", title="Accelerator List", icon="🚀")
    ],
}

pg = st.navigation(pages)
pg.run()
