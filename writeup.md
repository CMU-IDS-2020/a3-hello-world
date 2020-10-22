# What makes you happy?

**Team members**:

- Liyun Tu (Andrew ID: liyunt)
- Xiaoyu Sun (Andrew ID: seansun)

**Data source**: https://www.kaggle.com/unsdsn/world-happiness

[![A screenshot of the application](https://github.com/CMU-IDS-2020/a3-hello-world/raw/master/demo.gif)](https://github.com/CMU-IDS-2020/a3-hello-world/blob/master/demo.gif)



## Project Goals

Happiness is an important status for most of us, but it is hard to say what makes people happy. Understanding what brings people happiness is the key to improve people’s happiness level and overall life satisfaction. The main goal of this app is to explore how different features contribute to happy score by using "The World Happiness Report" dataset, a landmark survey of the state of global happiness to help with the exploration. The dataset includes reports from 2015-2019, each is made up of happiness rank and happiness score of around 155 countries (participant countries change slightly over years) around the world based on six features including economic production (GDP), social support (family), health, freedom, government corruption, and generosity. Generally, this app provides various interactive visualizations to show the relationship between happiness score and the six features.



## Design

For our first draft of prototype design as below, we followed the trend of homework 2 during which we designed a series of plots including: scatter plot for basic attribute distribution, spatial heatmap for country scores, interactive plot for attribute change over time, and scatter plot with regression line indicating ML prediction.

[![The initial draft prototype](https://github.com/CMU-IDS-2020/a3-hello-world/raw/master/prototype_old.JPG)](https://github.com/CMU-IDS-2020/a3-hello-world/blob/master/prototype_old.JPG)

Later we realized the app should be tightly-focused on exploring the relationship between happiness score and features. We decided to remove some less important sections such as map visualization and ML insight, and focus on scatter plots and line plots using interactive visualziation techniques to build a tightly-focused and efficient interactive visualization app.

[![The final draft prototype](https://github.com/CMU-IDS-2020/a3-hello-world/raw/master/prototype_final.JPG)](https://github.com/CMU-IDS-2020/a3-hello-world/blob/master/prototype_final.JPG)



**General Selection**

We use a multi-selection box to enable users to select one or more features among GDP, family, health, freedom, generosity, and corruption to visualize. This enables users to focus specific features as well as to compare different features. Besides, a slide bar is used for selecting year of data. By smoothly switching between years, users can gain an impression of how country's happiness rank and feature scores change over time.

**Plots**

First we have a strip plot for happiness score sorted in **descending order**. This plot could represent the distribution of happiness scores. More importantly, users could take it as a filter/minimap for selecting corresponding points in other two plots.

Second plot is a multi-line chart. The x-axis refers to the country/region names sorted in **descending** order of happiness rank while the y-axis includes scores of user selected features. Since those points are soretd in descending order of happiness score, this plot shows the rough relationship between happiness score and different features as well as the related country information. Also, users could investigate how country happiness rank changes over years by sliding the year selection bar.

As the multi-line plot showing the rough relationship, we use another scatter plot with regression line to more directly show relationhip between feature scores and happiness scores. Users could flexibly select regression type to investigate optimal relationship. Besides, hovering a data point will trigger its tooltip showing country name, happiness score, feature type and feature score.

In additon, out plots are closely binded with interactions. Lines and circles are colored. By choosing the interactive legend on the right, multi-line chart and scatter plot will highlight the selected features, which eables user to focus on a specific feature at a time. Besides, selecting the strip plot will simultaneously filter data in other plots and change their axis domain. We hope the flexible interactivity of these plots could insipre users' insights into relationship between the six features and happiness.



## Development

**Dataset Selection and Cleaning** We chose dataset from assignment 2 datasets as well as public datasets on Kaggle. And we decided to use "The World Happiness Report" from Kaggle for its significnace in indicating key to people's happiness. Then Xiaoyu implemented data cleaning process. The two issues to be taken care of during this task were (1)missing value and (2) country name mismatch. The dataset was pretty clean with only one missing value which we decided to evict it. Ideally, each country should correspond to one data line per year and have five in total. By printing out countries with less data entries, we found multiple names for one country and then manually corrected them to be consistent. Also, we modified the column names to make it more precise while maintaining their original meaning. We also modified "Country" column to "Country or Region" to avoid any possible inconvenience (3 hours/person)

**Initial Design** As is mentioned before, our first protype followed the trend of homework 2. Xiaoyu worked on the interactive plot for feature correlations while Liyun implemented the spatial heatmap for happiness score distribution. (6 hours/person)

**Second Round Brain Storming** As mentioned in the introduction before, we rethough about our app and did a second round brain storming to make our app more tightly-focused on showing the relationship rather than covering many different aspects. (4 hours/person)

**Final Design** Having learnt about the issue of initial design, we basically reimplemented everything based on our new design. For efficient coding, we worked in turn as a driver and navigator/researcher which is a popular team programming technique. (10 hours/person)

Overall, we roughly spent 26 per person on developing the app. The most time-consuming aspect should be figuring out efficient plots for dataset exploration.