import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header("🚗 Car Sales Data Explorer")

# Histogram
st.subheader("Histogram: Vehicle Types by Manufacturer")
fig1 = px.histogram(df, x='manufacturer', color='type')
st.plotly_chart(fig1)

# Scatter plot
st.subheader("Scatter Plot: Price vs. Model Year")
fig2 = px.scatter(df, x='model_year', y='price', color='condition', hover_data=['model'])
st.plotly_chart(fig2)

# Interactive: Manufacturer comparison
st.subheader("Price Distribution Comparison")
manufac_list = sorted(df['manufacturer'].unique())
m1 = st.selectbox("Select Manufacturer 1", manufac_list, index=manufac_list.index("chevrolet"))
m2 = st.selectbox("Select Manufacturer 2", manufac_list, index=manufac_list.index("hyundai"))
normalize = st.checkbox("Normalize Histogram", value=True)
histnorm = 'percent' if normalize else None

mask = (df['manufacturer'].isin([m1, m2]))
fig3 = px.histogram(df[mask], x='price', nbins=30, color='manufacturer', histnorm=histnorm, barmode='overlay')
st.plotly_chart(fig3)