import streamlit as st
import pandas as pd

st.title("Excel File Row Counter")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("✅ File uploaded successfully!")
        st.write("Preview of uploaded data:")
        st.dataframe(df.head())
        st.write(f"📊 The uploaded Excel file has **{df.shape[0]}** rows.")
    except Exception as e:
        st.error(f"❌ Failed to read file: {e}")
else:
    st.info("Please upload an Excel (.xlsx) file to continue.")
