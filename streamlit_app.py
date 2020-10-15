import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data
import plotly.offline as py
import json



# @st.cache  # add caching so we load the data only once
# def load_data(year, path="../data"):
#     return pd.read_csv(os.path.join(path, year) + "_map.csv")

st.title("What makes you happy? 📊😄")

@st.cache  # add caching so we load the data only once
def load_data():
    # Load the happiness data
    happy_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-hello-world/liyun/data/2016_map.csv"
    df = pd.read_csv(happy_url)
    df['Year'] = df['Year'].astype(str)
    return df

df = load_data()

st.write("Let's look at raw data in the Pandas Data Frame.")

if st.checkbox("Show raw data"):
    st.write(df)

st.write("Hmm 🤔, is there some correlation between country economics and happiness score? Let's make a scatterplot with [Altair](https://altair-viz.github.io/) to find.")

picked = alt.selection_multi()
chart = alt.Chart(df).mark_circle(size = 100).encode(
    x=alt.X("GDP", scale=alt.Scale(zero=False)),
    y=alt.Y("Score", scale=alt.Scale(zero=False)),
    color=alt.Y("Year")
).properties(
    width=600, height=400
)

st.write(chart.add_selection(picked))


# Feature distriburtion
st.write("## Explore feature distribution")

##Select feature to explore
feature = st.selectbox(
    'Select the feature', 
    ('Score','GDP','Family','Health','Freedom','Generosity','Corruption'))

##Histogram for score & selected feature
brush = alt.selection_interval(encodings = ["x"], resolve = "intersect")

hist = (
    alt.Chart()
    .mark_bar()
    .encode(
        alt.X(
            alt.repeat("row"),
            type = "quantitative",
            bin = alt.Bin(maxbins=100,minstep =0.05),
        ),
        alt.Y("count():Q", title = None),
    )
)

if feature == "Score":
    hisfeature = ['Score']
else:
    hisfeature = ['Score',feature]

multihist = alt.layer(
    hist.add_selection(brush).encode(color = alt.value("lightgrey")),
    hist.transform_filter(brush),
).properties(width = 650, height = 100).repeat(
    row = hisfeature, data = df
).configure_view(
    stroke = "transparent"
) 
st.write(multihist)



##Draw a black-white world map
countries = alt.topo_feature(data.world_110m.url, 'countries')
alt.Chart(countries).mark_geoshape(
    fill='#666666',
    stroke='white'
).properties(
    width=750,
    height=450
).project('equirectangular')

##Combine with data set and use color for selected feature
base = alt.Chart(countries).mark_geoshape(
).encode(tooltip=['Country or Region:N','Score:Q','GDP:Q','Family:Q','Health:Q','Freedom:Q','Generosity:Q','Corruption:Q'],
         color=alt.Color('Score:Q', scale=alt.Scale(scheme="oranges"))
).transform_lookup( # your code here
    lookup='id',
    from_=alt.LookupData(df, 'CodeNum', ['Score','Country or Region','GDP','Family','Health','Freedom','Generosity','Corruption','Year'])
).properties(
    width=730,
    height=450
).project('equirectangular')

picked = alt.selection_single(encodings=["color"])
st.write(base.encode(
    color = alt.condition(picked, alt.Color(feature+":Q", scale=alt.Scale(scheme="oranges")), alt.value("lightgray"))
).add_selection(picked))

















