import streamlit as st
from streamlit_calendar import calendar

config = CalendarConfig(
    lang='en',
    title='Yoga Class Schedule',
    dates='Mo - Fr',
    hours='8 - 22',
    mode=None,
    show_date=True,
    show_year=False,
    legend=True,
)

# you can validate your config
validate_config(config)