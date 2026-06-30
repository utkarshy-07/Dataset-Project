import pandas as pd

def clean_data(df):
    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing values
    '''We check missing values types or handle with dropna or fillna'''
    # print(df.isnull().sum()) - 49 missing values in Marks column so we fill it with mean.
    mean_marks = round(df["Marks"].mean(), 1)
    df["Marks"] = df["Marks"].fillna(mean_marks)

    # Validate Attendance
    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

    # Validate Study Hours
    df = df[df["StudyHours"] >= 0]

    # Validate Marks
    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

    # Now save this clean data in cleaned_data.csv
    df.to_csv("output/cleaned_data.csv", index=False)

    return df
if __name__ == "__main__":
    from load_data import load_data
    df = load_data()
    df = clean_data(df)