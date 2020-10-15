import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data
import plotly.offline as py
import json

st.title("What makes you happy? 📊😄")

@st.cache  # add caching so we load the data only once
def load_data():
    # Load the happiness data
    happy_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-hello-world/master/data/happy_map_filled.csv"
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
year = st.slider("Select Year", 2015, 2015, 2020, 1)


def gen_map(geodata, color_column, title, tooltip, color_scheme='bluegreen'):
    '''
    Generates Toronto neighbourhoods map with building count choropleth
    '''
    
    # Add Base Layer
    base = alt.Chart(geodata, title = title).mark_geoshape(
        fill='#666666',
        stroke='white'
    ).encode(
    ).properties(
        width=800,
        height=800
    )
    # Add Choropleth Layer
    choro = alt.Chart(geodata).mark_geoshape(
        fill='lightgray',
        stroke='black'
    ).encode(
        alt.Color(color_column, 
                  type='quantitative', 
                  scale=alt.Scale(scheme=color_scheme),
                  title = "Building Counts"),
         tooltip=tooltip
    )
    return base + choro

# World score map
source = alt.topo_feature(data.world_110m.url, 'countries')


# base = alt.Chart(source).mark_geoshape(
#     fill='#666666',
#     stroke='white'
# ).properties(
#     width=600, 
#     height=400
# )
# charts = base.project("equirectangular").properties(
#     title="equirectangular"
# )
# st.write(charts)
# st.map(df)

choro_json = json.loads(df.to_json())
choro_data = alt.Data(values = choro_json['features'])
happy_map = gen_map(geodata=choro_data, color_column='properties.Score', title="World happiness map", tooltip=['properties.Country:O','properties.Score:Q'], color_scheme='yelloworangered')




