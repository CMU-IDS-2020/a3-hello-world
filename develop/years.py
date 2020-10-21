import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("Happiness Data Analysis For Each Year")

@st.cache  # add caching so we load the data only once
def load_data(year, path="../data"):
    return pd.read_csv(os.path.join(path, year) + "_map.csv")

def show_correlation(features, df):
    default_features = ['Rank', 'Score', 'GDP', 'Family', 'Health', 'Freedom', 'Generosity']
    chart = alt.Chart(df).mark_point().encode(
        x=alt.X(features[0], scale=alt.Scale(zero=True)),
        y=alt.Y(features[1], scale=alt.Scale(zero=True)),
        # show country name or region name and other attributes as tooltip
        tooltip=['Country or Region'] + [f for f in default_features if f not in features]
    ).properties(
        width=700, height=400
    ).interactive()
    st.write(chart)

year = st.selectbox(
    'Which year would you like to have a look?', 
    ('2015', '2016', '2017', '2018', '2019'))

if year:
    df = load_data(year)
    st.write("Let's look at happeniss data in the Pandas Data Frame for year " + year + ".")
    st.write(df)
    # TODO: show some basic information before going to attributes correlation?
    st.write("Interested in seeing attributes' correlations?")
    features = st.multiselect(
        "Select two attributes to see correlation",
        ('Rank', 'Score', 'GDP', 'Family', 'Health', 'Freedom', 'Generosity'))
    if (len(features) != 0) and (len(features) != 2):
        st.write("Please select two attributes.")
    elif len(features) == 2:
        show_correlation(features, df)