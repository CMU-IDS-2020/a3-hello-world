import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data
import plotly.offline as py
import json



@st.cache  # add caching so we load the data only once
def load_data(year, path="../data"):
    return pd.read_csv(os.path.join(path, year) + "_map.csv")

st.title("What makes you happy? 📊😄")

@st.cache  # add caching so we load the data only once
def load_data():
    # Load the happiness data
    happy_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-hello-world/liyun/data/happy_map_code.csv"
    df = pd.read_csv(happy_url, index_col=0)
    df['Year'] = df['Year'].astype(str)
    return df

df = load_data()

st.write("Let's look at raw data in the Pandas Data Frame.")

if st.checkbox("Show raw data"):
    st.write(df)

st.write("Hmm 🤔, is there some correlation between country economics and happiness score? Let's make a scatterplot with [Altair](https://altair-viz.github.io/) to find.")


# picked = alt.selection_single()
# picked = alt.selection_single(on = "mouseover", empty = "none")
picked = alt.selection_multi()
# picked = alt.selection_interval(encodings=["x"])
# picked = alt.selection_single(encodings=["color"])
# picked = alt.selection_single(fields = ["Species", "Island"])
chart = alt.Chart(df).mark_circle(size = 100).encode(
    x=alt.X("GDP", scale=alt.Scale(zero=False)),
    y=alt.Y("Score", scale=alt.Scale(zero=False)),
    color=alt.Y("Year")
).properties(
    width=600, height=400
)

st.write(chart.add_selection(picked))
# year = st.slider("Select Year", 2015, 2015, 2020, 1)

# World score map
countries = alt.topo_feature(data.world_110m.url, 'countries')

alt.Chart(countries).mark_geoshape(
    fill='#666666',
    stroke='white'
).properties(
    width=750,
    height=450
).project('equirectangular')

base = alt.Chart(countries).mark_geoshape(
).encode(tooltip=['Country or Region:N','Score:Q','GDP:Q','Family:Q','Health:Q','Freedom:Q','Generosity:Q','Corruption:Q'],
         color=alt.Color('Score:Q', scale=alt.Scale(scheme="oranges"))
).transform_lookup( # your code here
    lookup='id',
    from_=alt.LookupData(df, 'CodeNum', ['Score','Country or Region','GDP','Family','Health','Freedom','Generosity','Corruption','Year'])
).properties(
    width=750,
    height=450
).project('equirectangular')

st.write(base)

input_dropdown = alt.binding_select(options = [2015, 2016, 2017,2018,2019], 
name = "'Which year would you like to have a look?' ")
picked = alt.selection_single(encodings = ["color"], bind = input_dropdown)






