import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns

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
st.markdown("## Blood Pressure")

st.write(df["BloodPressure"].describe())

st.write(df["BloodPressure"].head())

st.write(df["BloodPressure"].tail())
