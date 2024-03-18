import streamlit as st
import pandas as pd
import numpy as np
import time
from streamlit_calendar import calendar

st.set_page_config(page_title="supply chain management", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




st.title("Dashboard")

name=""
st.session_state.name="Shreya"
with st.container():
    st.write("Congratulations User, you have reached your monthly target! ")




col1, col2, col3 = st.columns(3)
col1.metric("Monthly Sales", "20K", "-1.2%")
col2.metric("Annual Sales", "50K", "8%")
col3.metric("Predicted Sales", "86K", "4%")
# #--------------------------------------

overallSales_df = pd.read_csv("SalesData.csv")
selected_columns = ['SalesPrice','SalesDate']  
Sales1_df = overallSales_df[selected_columns].copy()

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        # Add more resource entries as needed
    ],
}

calendar_events = [
    {"title": "Event 1", "start": "2023-07-31T08:30:00", "end": "2023-07-31T10:30:00", "resourceId": "a"},
    # Add more event entries as needed
]

custom_css = """
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""



col1,col2=st.columns([2,1])
with col1:
    st.line_chart(Sales1_df, x="SalesDate", y="SalesPrice", color=["#FF0000"], width=100)
with col2:
    calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
    st.write(calendar)


