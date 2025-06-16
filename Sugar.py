import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns
import plotly.express as px

st.title("DIABETES ANALYSIS")

#import my csv file
st.markdown("# FIRST FIVE")

df = pd.read_csv("diabetes.csv")
st.table(df.head())

st.markdown("# LAST FIVE")

df = pd.read_csv("diabetes.csv")
st.write(df.tail())

st.markdown("# DATA DESCRIPTION")
mum = df.describe()
st.write(mum)

st.markdown("# DATA SHAPE")
mum = df.shape
st.write(mum)

st.markdown("# DATA INFORMATION")
mum = df.info()
st.write(mum) 


st.markdown("# UNIVAFIATE ANALYSIS")
st.markdown("## Blood Pressure Description")

st.write(df["BloodPressure"].describe())

st.markdown("## Blood Pressure First Data")
st.write(df["BloodPressure"].head())

st.markdown("## Blood Pressure Last Data")
st.write(df["BloodPressure"].tail())

st.markdown("## Blood Pressure Graph")

fig = px.bar(df['BloodPressure'], y ='BloodPressure', title=("Blood Pressure Distribution Graph"))
st.plotly_chart(fig, use_containeer_width=True)



st.markdown("# BIVAFIATE ANALYSIS")
st.markdown("## Blood Pressure vs Pregnancies Description")

fig2 = px.bar(df, x ='Pregnancies', y ='BloodPressure', title=("Blood Pressure vs Pregnancies Distribution Graph"))
st.plotly_chart(fig2, use_containeer_width=True)


