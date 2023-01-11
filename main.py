import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob('diary/*.txt'))

analyzer = SentimentIntensityAnalyzer()
positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip('.txt').strip('diary/') for name in filepaths]
st.title('Diary Tone')
st.subheader('Positivity')
pos_fig = px.line(x=dates, y=positivity, labels={'x': 'dates', 'y': 'Positivity'})
st.plotly_chart(pos_fig)
st.subheader('Negativity')
pos_fig = px.line(x=dates, y=negativity, labels={'x': 'dates', 'y': 'Negativity'})
st.plotly_chart(pos_fig)
