# EduMetrics: Student Performance & Attendance Analytics Dashboard

An interactive Flask web dashboard designed to present demographic, study habit, and attendance correlation insights for secondary school mathematics students. Developed as a **Level 1 Internship Project** by a **2nd-Year Computer Science (AI) Student**.

---

## 🚀 Features

*   **KPI Overview:** Immediate overview of cohort size, dropout rates, and average class grades.
*   **Interactive Dataset Preview:** Explore original raw or preprocessed student data.
*   **Data Cleaning Timeline:** Clear breakdown of data imputation, calculations, and active student filtering.
*   **Data Analysis:** Correlation calculations (identifying skew from dropout zeroes) and group statistics tables.
*   **Dynamic Visualizations:** Beautiful pre-rendered Matplotlib/Seaborn distribution, pie, bar, and scatter charts.
*   **Actionable Insights:** Targeted recommendations for school administrators, teachers, and parents.

---

## 📂 Folder Structure

```text
student_performance_analysis/
│
├── data/
│   ├── raw/
│   │   └── student-mat.csv           # Raw UCI Student Performance data
│   └── processed/
│       └── student-cleaned.csv        # Preprocessed data with engineered columns
│
├── src/
│   ├── data_loader.py                # Preprocessing and cleaning script
│   └── analyzer.py                   # Calculations and chart rendering script
│
├── static/
│   ├── css/
│   │   └── style.css                 # Premium custom dashboard stylesheet
│   ├── js/
│   │   └── main.js                   # Interactivity, light/dark theme toggle
│   └── images/                       # Generated analysis charts
│
├── templates/                        # Jinja2 HTML layout pages
│   ├── base.html, home.html, dataset_preview.html, 
│   ├── cleaning_summary.html, analysis.html, 
│   └── visualizations.html, insights.html
│
├── app.py                            # Flask application entry point
├── setup_dataset.py                  # Downloads and unzips raw data files
├── report.md                         # Printable short academic project report
└── requirements.txt                  # Python dependencies
```

---

## 🛠️ Setup & Running Instructions

### 1. Prerequisites
Ensure you have **Python 3.8+** installed.

### 2. Install Dependencies
Navigate to the project root directory and run:
```bash
pip install -r requirements.txt
```

### 3. Setup Dataset
Ensure the raw data is loaded and preprocessing steps run:
```bash
python setup_dataset.py
```
This script will try to download the UCI zip file directly. If offline, it will automatically generate a highly realistic synthetic copy matching the exact schema and statistics of the UCI student dataset.

### 4. Run the Flask Web Application
Launch the server:
```bash
python app.py
```
Open your browser and navigate to:  
👉 **`http://127.0.0.1:5000/`**

---

## 📊 Analytical Methodology
This project implements standard descriptive analytics:
*   **Linear Correlation:** Calculated using the Pearson Correlation Coefficient ($r$) between attendance percentage and final grade ($G3$).
*   **Data Cleaning Impact:** Highlights how isolating students who missed the final exam (G3 = 0) shifts the correlation from a flat **-0.03** to a weak-moderate positive **0.21**, proving attendance contributes to higher academic scores.
*   **Strict Scope Constraints:** Strict avoidance of Machine Learning models, SQL databases, external dashboarding tools (Power BI/Tableau), and authentication layers, matching the Level 1 internship standard.
