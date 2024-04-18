import streamlit as st
import pandas as pd

st.title('Titanic App')
st.header('Titanic Graphs')
st.write('Graficas del dataset titanic')


titanic_link='titanic.csv'
titanic_data=pd.read_csv(titanic_link)
st.dataframe(titanic_data)