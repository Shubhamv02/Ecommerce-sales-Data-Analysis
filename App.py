import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-commerce Sales Dashboard", layout="wide")

st.title("E-commerce Sales Data Analysis Dashboard")
st.write("Analyze sales trends, revenue, and customer behavior from your dataset.")

# Upload CSV file
###uploaded_file = st.file_uploader("📂 Upload your E-commerce Sales Data (CSV)", type=["csv"])
uploaded_file = 'EDA_Report.csv'


if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")
    
    # Ensure correct data types
    if 'Sales' in df.columns:
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0)
    
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    

category_selection = st.sidebar.multiselect("Select Category", df['title'].unique())
platform_selection = st.sidebar.multiselect("Select Platform", df['platform'].unique())
gender_selection = st.sidebar.radio("Select Gender", df['maincateg'].dropna().unique(), index=0)


    # Sidebar Filters
    # Category Filter
if 'Category' in df.columns:
    if st.sidebar.button("Filter by Category"):
        category_selection = True

# Platform Filter
if 'Platform' in df.columns:
    if st.sidebar.button("Filter by Platform"):
        apply_platform = True

# Gender Filter
if 'Gender' in df.columns:
    if st.sidebar.button("Filter by Gender"):
        apply_gender = True

# Submit button to apply all selected filters
if st.sidebar.button("Submit"):
    filtered_df = df.copy()  # Start with the original dataframe

    # Apply filters only if the respective button was clicked
    if category_selection:
        filtered_df = filtered_df[filtered_df['title'].isin(category_selection)]
    
    if platform_selection:
        filtered_df = filtered_df[filtered_df['platform'].isin(platform_selection)]
    
    if gender_selection:
        filtered_df = filtered_df[filtered_df['maincateg'] == gender_selection]

    # Show the final filtered dataset
    st.write("**Filtered Data:**")
    st.write(filtered_df)

    st.write(f"**Total Count Of Filtered Data:{len(filtered_df)}**")
