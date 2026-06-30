import pandas as pd

def generate_report(df):
    total_students = len(df)
    passed_students = len(df[df["Result"] == "Pass"])
    failed_students = len(df[df["Result"] == "Fail"])
    highest_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()
    average_marks = df["Marks"].mean()
    average_attendance = df["Attendance"].mean()

    grade_distribution = df["Grades"].value_counts()

    report = pd.DataFrame({
        "Matric":[
            "Total Students",
            "Pass Students",
            "Fail Students",
            "Highest Marks",
            "Lowest Marks",
            "Average Marks",
            "Average Attendance",
            "Grade-wise Distribution"
        ],

        "Values":[
            total_students,
            passed_students,
            failed_students,
            highest_marks,
            lowest_marks,
            average_marks,
            average_attendance,
            grade_distribution
        ]
    })

    report.to_csv("output/report.csv", index=False)