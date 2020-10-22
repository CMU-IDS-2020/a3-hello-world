import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("What makes you happy? 📊😄")

# @st.cache  # add caching so we load the data only once
def load_data(year, path="./data"):
    return pd.read_csv(os.path.join(path, str(year)) + ".csv")

features = st.sidebar.multiselect(
    'Select features you are interested in', 
    ('GDP', 'Family', 'Health', 'Freedom', 'Generosity', 'Corruption'))

if features:
    year = st.sidebar.slider("Select year", 2015, 2015, 2019, 1)
    df = load_data(year)
    df = df[features+["Country or Region", "Rank", "Score"]]
    df2 = df.melt(id_vars=["Country or Region", "Rank", "Score"], var_name="Feature", value_name="Value")
    df2 = df2.sort_values(by = "Score", ascending = False)

    if st.sidebar.checkbox("Show raw data"):
        st.write(df)
    
    st.write("Select score interval and legend type to filter data.")
    brush = alt.selection_interval(encodings=["x"])  # selection of type "interval"
    legend_selection = alt.selection_multi(fields=['Feature'], bind='legend')

    score_tick = alt.Chart(df2).mark_tick().encode(
        x=alt.X('Score:Q', scale = alt.Scale(zero=False)),
    ).properties(
        width=600
    ).add_selection(
        brush
    )


    line_plot = alt.Chart(df2).mark_line().encode(
        x= alt.X('Country or Region', type='nominal', sort=None),
        y= 'Value',
        color= alt.condition(legend_selection, 'Feature:N', alt.value('lightgray'))
    ).properties(
        width=600,
        height = 300
    ).add_selection(
        legend_selection
    ).transform_filter(brush)

    scatter_plot = alt.Chart(df2).mark_point().encode(
        x= alt.X('Score:Q', sort="descending", scale=alt.Scale(zero=False)),
        y='Value',
        color=alt.condition(legend_selection, 'Feature:N', alt.value('lightgray')),
        tooltip=['Country or Region:N','Score:Q',"Feature:N", "Value:Q"],
    ).properties(
        width=600,
        height = 300
    ).transform_filter(
        brush
    )
    regre_method = st.sidebar.selectbox(
        'Select regression type',
        ('linear', 'log', 'quad','poly'))

    regression_plot = scatter_plot.transform_regression("Score", 'Value', groupby=['Feature'], method = regre_method).mark_line()

    # st.write(regression_plot)

    st.write(score_tick.encode(x=alt.X('Score:Q', sort="descending")) & line_plot 
    & (scatter_plot+regression_plot).add_selection(legend_selection))

