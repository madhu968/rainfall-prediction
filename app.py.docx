import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the data from the CSV file
    df = pd.read_csv('Rainfall.csv')
    
    # Display the first few rows of the dataframe
    print("First few rows of the dataset:")
    print(df.head())

    # Basic statistics of the dataset
    print("\nBasic statistics:")
    print(df.describe())

    # Check for any missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Plotting a simple graph - for example, rainfall over the days
    plt.figure(figsize=(10, 5))
    plt.plot(df['day'], df['rainfall'], marker='o')
    plt.title('Rainfall Over Days')
    plt.xlabel('Day')
    plt.ylabel('Rainfall')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()