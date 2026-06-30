import os
import matplotlib
# matplotlib.use('Agg')   # save charts as image files instead of popup windows
import matplotlib.pyplot as plt
def _get_column_name(df, *names):
    for name in names:
        if name in df.columns:
            return name
    return None
def generate_visualizations(df):
    """Bonus Module - Create visual charts and save them as images
       in the output/ folder."""
    print("\n========== BONUS: VISUALIZATIONS ==========")

    os.makedirs("output", exist_ok=True)

    grade_col = _get_column_name(df, "Grade", "Grades")
    result_col = _get_column_name(df, "Result")
    study_hours_col = _get_column_name(df, "Study Hours", "StudyHours")
    marks_col = _get_column_name(df, "Marks")

    if grade_col is None:
        print("No grade column available for visualization.")
        return
    if result_col is None:
        print("No result column available for visualization.")
        return
    if study_hours_col is None or marks_col is None:
        print("Required numeric columns are missing for visualization.")
        return

    # Chart 1 - Grade Distribution (Bar Chart)
    grade_counts = df[grade_col].value_counts().sort_index()
    plt.figure(figsize=(6, 4))
    plt.bar(grade_counts.index, grade_counts.values, color='#4C72B0')
    plt.title('Grade Distribution')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.tight_layout()
    plt.savefig('output/chart_grade_distribution.png')
    plt.close()

    # Chart 2 - Pass vs Fail (Pie Chart)
    result_counts = df[result_col].value_counts()
    plt.figure(figsize=(5, 5))
    plt.pie(result_counts.values, labels=result_counts.index, autopct='%1.1f%%',
            colors=['#55A868', '#C44E52'])
    plt.title('Pass vs Fail')
    plt.tight_layout()
    plt.savefig('output/chart_pass_fail.png')
    plt.close()

    # Chart 3 - Marks Distribution (Histogram)
    plt.figure(figsize=(6, 4))
    plt.hist(df[marks_col], bins=5, color='#DD8452', edgecolor='black')
    plt.title('Marks Distribution')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.tight_layout()
    plt.savefig('output/chart_marks_distribution.png')
    plt.close()

    # Chart 4 - Study Hours vs Marks (Scatter Plot)
    plt.figure(figsize=(6, 4))
    plt.scatter(df[study_hours_col], df[marks_col], color='#8172B2')
    plt.title('Study Hours vs Marks')
    plt.xlabel('Study Hours')
    plt.ylabel('Marks')
    plt.tight_layout()
    plt.savefig('output/chart_study_vs_marks.png')
    plt.close()

    # Chart 5 - Average Marks by Grade (Horizontal Bar)
    avg_marks_by_grade = df.groupby(grade_col)[marks_col].mean().sort_index()
    plt.figure(figsize=(6, 4))
    plt.barh(avg_marks_by_grade.index, avg_marks_by_grade.values, color='#64B5CD')
    plt.title('Average Marks by Grade')
    plt.xlabel('Average Marks')
    plt.ylabel('Grade')
    plt.tight_layout()
    plt.savefig('output/chart_avg_marks_by_grade.png')
    plt.close()

    print("5 charts saved to output/ folder:")
    print(" - chart_grade_distribution.png")
    print(" - chart_pass_fail.png")
    print(" - chart_marks_distribution.png")
    print(" - chart_study_vs_marks.png")
    print(" - chart_avg_marks_by_grade.png")


def visualize(df):
    """Backward-compatible wrapper for the visualization entry point."""
   
if __name__ == "__main__":
    from load_data import load_data
    from transform import transform_data
    df = load_data()
    df = transform_data(df)
    generate_visualizations(df)