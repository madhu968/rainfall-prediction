import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Rainfall Data Visualization")

# Load the PKL file directly from the local directory
try:
    df = pd.read_pickle('Rainfall.pkl')
    
    # Display the first few rows of the dataframe
    st.subheader("First few rows of the dataset:")
    

    # Basic statistics of the dataset
    st.subheader("Basic statistics:")
    st.write(df.describe())

    # Check for any missing values
    st.subheader("Missing values in each column:")
    st.write(df.isnull().sum())

    # Handle missing values by filling them with the mean
    df.fillna(df.mean(), inplace=True)

    # Ensure 'day' is in the correct format
    if df['day'].dtype != 'int64':
        df['day'] = pd.to_numeric(df['day'], errors='coerce')

    # Plotting rainfall over the days
    plt.figure(figsize=(10, 5))
    plt.plot(df['day'], df['rainfall'], marker='o')
    plt.title('Rainfall Over Days')
    plt.xlabel('Day')
    plt.ylabel('Rainfall')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

except FileNotFoundError:
    st.error("Error: The file 'Rainfall.pkl' was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
