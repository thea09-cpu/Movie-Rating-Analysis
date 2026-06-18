import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df=pd.read_excel("Data/Cleaned/final_netflix_dataset.xlsx")

#Page Setup
st.set_page_config(page_title="Netflix Movie Rating Analysis", page_icon=":bar_chart:", layout="wide")
# Custom Theme Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2&family=Inter:wght@400;600&family=JetBrains+Mono:wght@500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #1B1F3B;  /* dark navy background */
    color: #F5F5F5;             /* off-white text */
}

h1, h2, h3 {
    font-family: 'Baloo 2', cursive;
    color: #FFB6C1;             /* pastel pink titles */
}

[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace;
    color: #98FF98;             /* mint green KPI values */
    font-size: 1.5rem;
}

[data-testid="stSidebar"] {
    background-color: #0F1126;  /* sidebar dark background */
    color: #C8A2C8;             /* lilac accents */
}
</style>
""", unsafe_allow_html=True)


#Sidebar Setup
st.sidebar.header("Netflix Movie Rating Analysis")
genre_filter = st.sidebar.multiselect("Select Genre", options=df["genre_group"].unique(), default=df["genre_group"].unique())
age_filter = st.sidebar.multiselect("Select Age Group", options=df["age_group"].unique(), default=df["age_group"].unique())
fdf=df[(df["genre_group"].isin(genre_filter)) & (df["age_group"].isin(age_filter))]

#Main Page Setup
st.title("Netflix Movie Rating Analysis")
st.write("This is a simple dashboard to analyze Netflix movie ratings.")
st.write("You can filter the data by genre and age group using the sidebar.")
st.write("The data is based on a dataset of Netflix movies and their ratings across different age groups and genres.")

#KPIs
total_movies = fdf.shape[0]
st.subheader("Key Performance Indicators")
st.metric("Total Movies", total_movies)
st.metric("Average Completion Rate", f"{fdf['avg_completion_rate'].mean():.2f}%")
st.metric("Average Rating", f"{fdf['imdb_rating'].mean():.2f}/5")    
st.metric("Average Engagement Score", f"{fdf['engagement_score'].mean():.2f}/10")

#Charts
#Titles by genre
titles_by_genre = fdf.groupby("genre_group").size()
st.subheader("Titles by Genre")
fig1 = px.bar(titles_by_genre, x=titles_by_genre.index, y=titles_by_genre.values, labels={"x": "Genre", "y": "Count"}, title="Number of Titles by Genre")
st.plotly_chart(fig1)

#Views by age group
views_by_age_group = fdf.groupby("age_group")["views"].sum()
st.subheader("Views by Age Group")
fig2 = px.bar(views_by_age_group, x=views_by_age_group.index, y=views_by_age_group.values, labels={"x": "Age Group", "y": "Views"}, title="Total Views by Age Group")
st.plotly_chart(fig2)   

#Views per genre category
views_by_genre_age = fdf.groupby(["genre_group", "age_group"])["views"].sum().reset_index()
st.subheader("Views by Genre and Age Group")
fig3 = px.bar(views_by_genre_age, x="genre_group", y="views", color="age_group", labels={"genre_group": "Genre", "views": "Views"}, title="Views by Genre and Age Group")
st.plotly_chart(fig3)

#Engagement Score by Churn Rate
st.write("Engagement Score is a proxy for how actively users interact with content while Churn Impact Score measures how much losing those users hurts retention. A higher engagement score indicates that users are more engaged with the content, while a higher churn impact score indicates that losing those users would have a greater negative impact on retention.")
engagement_by_churn = fdf.groupby("churn_impact_score")["engagement_score"].mean().reset_index()
st.subheader("Engagement Score by Churn Impact Score")  
fig4 = px.line(engagement_by_churn, x="churn_impact_score", y="engagement_score", labels={"churn_impact_score": "Churn Impact Score", "engagement_score": "Engagement Score"}, title="Engagement Score by Churn Impact Score")
st.plotly_chart(fig4)

# Scatter plot of Engagement Score vs Churn Impact Score
st.subheader("Engagement Score vs Churn Impact Score")
st.write("This chart shows whether higher engagement reduces churn risk. A downward trend would suggest that more engaged viewers are less likely to churn.")

fig5 = px.scatter(
    fdf,
    x="engagement_score",
    y="churn_impact_score",
    color="genre_group",
    opacity=0.6,
    labels={"engagement_score": "Engagement Score", "churn_impact_score": "Churn Impact Score"},
    title="Engagement vs Churn Impact"
)

#Add a trend line
x = fdf["engagement_score"].values
y = fdf["churn_impact_score"].values
if len(x) > 1:
    m, b = np.polyfit(x, y, 1)
    fig5.add_scatter(x=x, y=m*x+b, mode="lines", name="Trend", line=dict(color="black", dash="dot"))

st.plotly_chart(fig5)

