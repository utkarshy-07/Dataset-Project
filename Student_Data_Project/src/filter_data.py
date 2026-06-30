import pandas as pd

def filter_data(df):
    toppers = df[df["Marks"] >= 90]

    failed = df[df["Result"] == "Fail"]

    low_attendance = df[df["Attendance"] < 75]

    study_more = df[df["StudyHours"] > 8]

    toppers.to_csv("output/toppers.csv", index=False)
    failed.to_csv("output/failed_students.csv", index=False)
    low_attendance.to_csv("output/low_attendance.csv", index=False)
    study_more.to_csv("output/study_more_than_8_hours.csv", index=False)