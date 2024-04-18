import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Titanic App')
st.header('Titanic Graphs')
st.write('Graficas del dataset titanic')


titanic_link='titanic.csv'
titanic_data=pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots() 
ax.hist(titanic_data['Fare']) 
st.header("Histograma del Titanic") 
st.pyplot(fig)
