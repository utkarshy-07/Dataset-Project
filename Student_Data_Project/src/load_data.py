import pandas as pd
def load_data():
    # Read the csv file
    df = pd.read_csv("../data/student_dataset_v2.csv")
    return df

def inspect_data(df):
    # Display the first five records
    print("First 5 elements: ")
    print(df.head())

    # Display the last five records
    print("\nLast 5 elements: ")
    print(df.tail())

    # Print the shape of the dataset
    print("\nShape of the dataset: ")
    print(df.shape)

    # Print columns names
    print("\nPrint column names: ")
    print(df.columns)

    # Display data types of each column
    print("\nData types of each column: ")
    print(df.dtypes)

    # Find missing values
    print("Number of missing values in each column: ")
    print(df.isnull().sum())

    # Find duplicate records
    print("\nDuplicated records")
    print(df.duplicated().sum())

    # Display descriptive statistics
    print("\nDescriptive statistics")
    print(df.describe())

    # Check memory usage
    print("\nMemory usage: ")
    print(df.memory_usage())

    # Display summary information
    print("\nSummary Information: ")
    print(df.info())
if __name__ == "__main__":
    df = load_data()
    inspect_data(df)