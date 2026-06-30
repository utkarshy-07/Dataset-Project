import pandas as pd

def analyze_data(df):
    average_marks = df["Marks"].mean()
    highest_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()

    average_attendance = df["Attendance"].mean()
    average_study_hours = df["StudyHours"].mean()

    # Pass percentage
    total_students = len(df)
    passed_students = len(df[df["Result"] == "Pass"])
    pass_percentage = (passed_students / total_students) * 100

    # Fail percentage
    failed_students = len(df[df["Result"] == "Fail"])
    fail_percentage = (failed_students / total_students) * 100

    # Grade distribution
    a = b = c = d = f = 0

    for grade in df["Grades"]:
        if grade == "A":
            a += 1
        elif grade == "B":
            b += 1
        elif grade == "C":
            c += 1
        elif grade == "D":
            d += 1
        else:
            f += 1

    grade_distribution = {
        "A": a,
        "B": b,
        "C": c,
        "D": d,
        "F": f
    }

    print(f"Average Marks: {average_marks}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Average Attendance: {average_attendance}")
    print(f"Average Study Hours: {average_study_hours}")
    print(f"Pass Percentage: {pass_percentage}")
    print(f"Fail Percentage: {fail_percentage}")
    print(f"Grade Distribution: {grade_distribution}")

    # Statistical Analysis
    mean = df.mean(numeric_only=True)
    median = df.median(numeric_only=True)
    mode = df.mode(numeric_only=True)
    standard_deviation = df.std(numeric_only=True)
    variance = df.var(numeric_only=True)
    correlation_matrix = df.corr(numeric_only=True)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard deviation: {standard_deviation}")
    print(f"Variance: {variance}")
    print(f"Correlation Matrix: {correlation_matrix}")

def sort_data(df):
    marks_sorted = df.sort_values(by="Marks", ascending=False)
    attendance_sorted = df.sort_values(by="Attendance", ascending=False)
    studyHours_sorted = df.sort_values(by="StudyHours", ascending=False)
    print(f"Students sorted by Marks: {marks_sorted}")
    print(f"Students sorted by Attendance: {attendance_sorted}")
    print(f"Students sorted by Study Hours: {studyHours_sorted}")


def group_data(df):
    print("Average Marks by Grade")
    print(df.groupby("Grades")["Marks"].mean())

    print("\nNumber of Students in Each Grade")
    print(df.groupby("Grades")["Grades"].count())

    print("\nAverage Attendance by Grade")
    print(df.groupby("Grades")["Attendance"].mean())
if __name__ == "__main__":
    from load_data import load_data
    from transform import transform_data
    df = load_data()
    df = transform_data(df)
    analyze_data(df)
    sort_data(df)
    group_data(df)
