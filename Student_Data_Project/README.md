# Student Performance Data Handling and Analysis System

A complete data handling and analysis project built using **Python** and **Pandas**.
This project covers the full data lifecycle — loading, cleaning, transforming, analyzing, and exporting student performance data, with bonus visualizations using Matplotlib.

## Dataset
`data/student_dataset_v2.csv` — Student ID, Student Name, Study Hours, Attendance (%), Marks

## Project Structure
```
Student_Data_Project/
├── data/
│   └── student_dataset_v2.csv
├── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   ├── low_attendance.csv
│   ├── high_study_hours.csv
│   ├── report.csv
│   └── chart_*.png (5 visualizations)
├── src/
│   ├── load_data.py      # Module 1 & 2 - Load & inspect
│   ├── clean_data.py     # Module 3 - Cleaning
│   ├── transform.py      # Module 4 - Transformation
│   ├── analyze.py        # Module 5-9 - Filter, analyze, sort, group, stats
│   ├── report.py         # Module 10 & 11 - Report & export
│   └── visualize.py      # Bonus - Matplotlib charts
├── main.py
└── README.md
```

## How to Run
```bash
pip install pandas matplotlib
python main.py
```

## Output
All CSV reports and PNG charts are generated inside the `output/` folder automatically.

## Grading Logic
| Marks | Grade | Result |
|-------|-------|--------|
| 80+ | A | Pass |
| 65-79 | B | Pass |
| 50-64 | C | Pass |
| 35-49 | D | Pass |
| Below 35 | F | Fail |

## Author
**Name:** [Utkarsh Yadav]
**Course:** [Btech (CSE)]
**College:** [MPEC]
