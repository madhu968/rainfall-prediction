import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
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

        # Handle missing values by filling them with the mean (or any other strategy)
        df.fillna(df.mean(), inplace=True)

        # Ensure 'day' is in the correct format
        if df['day'].dtype != 'int64':
            df['day'] = pd.to_numeric(df['day'], errors='coerce')

        # Plotting a simple graph - for example, rainfall over the days
        plt.figure(figsize=(10, 5))
        plt.plot(df['day'], df['rainfall'], marker='o')
        plt.title('Rainfall Over Days')
        plt.xlabel('Day')
        plt.ylabel('Rainfall')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Error: The file 'Rainfall.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
