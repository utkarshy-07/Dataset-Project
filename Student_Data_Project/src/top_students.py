import pandas as pd
# Display the Top 10 students based on the Performance Score.
def top_students(df):
    top_10 = df.sort_values(
        by="PerformanceScore",
        ascending=False
    ).head(10)

    print("\nTop 10 Students")
    print(top_10)

    top_10.to_csv("output/top_10_students.csv", index=False)