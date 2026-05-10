import streamlit as st
import pandas as pd
import time

st.title("💳 Real-Time Fraud Detection Dashboard")

# Placeholder
placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("results.csv", header=None, names=["Result"])

        total = len(df)
        fraud = len(df[df["Result"] == "Fraud"])
        normal = len(df[df["Result"] == "Normal"])

        with placeholder.container():
            st.metric("Total Transactions", total)
            st.metric("Fraud Transactions", fraud)
            st.metric("Normal Transactions", normal)

            st.write("Latest Results:")
            st.dataframe(df.tail(10))

    except:
        st.write("Waiting for data...")

    time.sleep(2)