import pandas as pd

def transform_data(df):
    grades = []

    for marks in df["Marks"]:
        if marks >= 90:
            grades.append("A")
        elif marks >= 85:
            grades.append("B")
        elif marks >= 60:
            grades.append("C")
        elif marks >= 40:
            grades.append("D")
        else:
            grades.append("F")

    df["Grades"] = grades
    # Add new row result on the basis of grades
    result = []

    for grade in df["Grades"]:
        if grade == "F":
            result.append("Fail")
        else:
            result.append("Pass")

    df["Result"] = result


    # add new perfomance score row in dataset
    performance = []

    for i in range(len(df)):

        score = (
            df.loc[i, "Marks"] * 0.70 +
            df.loc[i, "Attendance"] * 0.10 +
            df.loc[i, "StudyHours"] * 0.20
        )

        performance.append(round(score, 1))

    df["PerformanceScore"] = performance

    df.to_csv("output/cleaned_data.csv", index=False)

    return df