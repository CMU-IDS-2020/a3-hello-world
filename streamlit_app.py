import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("Happiness Data Analysis")

@st.cache  # add caching so we load the data only once
def load_data(year, path="./data"):
    return pd.read_csv(os.path.join(path, str(year)) + "_map.csv")

features = st.multiselect(
    'Select features you are interested in', 
    ('Rank', 'Score', 'GDP', 'Family', 'Health', 'Freedom', 'Generosity'))

if features:
    year = st.slider("Select Year", 2015, 2015, 2019, 1)
    df = load_data(year)
    
    brush = alt.selection_interval()  # selection of type "interval"
    if st.checkbox("Show raw data"):
        st.write(df)
    

    line_plot = alt.Chart(df).mark_line().encode(
        x="Country or Region",
        y="GDP"
    ).properties(
        width=700,
        height = 100
    ).interactive()
    st.write(line_plot)

    score_tick = alt.Chart(df).mark_tick().encode(
        x='Score:Q',
    ).encode(
        color=alt.Color('Score:Q', scale=alt.Scale(scheme="oranges"))
    ).properties(
        width=700,
        height = 100
    ).add_selection(
        brush
    )
    st.write(score_tick)

