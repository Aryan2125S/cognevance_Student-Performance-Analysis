# EduMetrics: Student Performance & Attendance Analytics Dashboard

## Project Overview
EduMetrics is a comprehensive data analytics and machine learning dashboard designed to present demographic, study habit, and attendance correlation insights for secondary school mathematics students. Developed as a **Level 1 Internship Project**, it empowers educational administrators with data-driven decision-making tools. The application has been fully upgraded to a modern, interactive **Streamlit** dashboard.

---

## Features
*   **KPI Overview:** Immediate overview of cohort size, dropout rates, and average class grades.
*   **Interactive Dataset Preview:** Explore original raw or preprocessed student data dynamically.
*   **Data Cleaning Timeline:** Clear breakdown of data imputation, calculations, and active student filtering.
*   **Data Analysis:** Correlation calculations identifying skew from dropout zeroes and group statistics tables.
*   **Dynamic Visualizations:** Beautiful, interactive Plotly distribution, donut, bar, and scatter charts styled with a premium pastel theme.
*   **Interactive Predictor:** A Machine Learning engine simulating final grades based on real-time parameters.
*   **Actionable Insights:** Targeted recommendations for school administrators, teachers, and parents.

---

## Technology Stack
*   **Frontend & Dashboard Framework:** Streamlit
*   **Data Manipulation & Analysis:** Pandas, NumPy
*   **Machine Learning (Regression):** NumPy (Least Squares Linear Regression)
*   **Interactive Data Visualization:** Plotly (Express & Graph Objects)
*   **Styling:** Custom CSS (Streamlit CSS overrides), Google Fonts (Outfit, Inter)

---

## Folder Structure
```text
student_performance_analysis/
│
├── data/
│   ├── raw/
│   │   └── student-mat.csv           # Raw UCI Student Performance data
│   └── processed/
│       └── student-cleaned.csv       # Preprocessed data with engineered columns
│
├── src/
│   ├── data_loader.py                # Preprocessing and cleaning module
│   └── analyzer.py                   # Calculations and analytical functions
│
├── app.py                            # Streamlit application entry point (Dashboard)
├── setup_dataset.py                  # Downloads and unzips raw data files
├── report.md                         # Printable short academic project report
└── requirements.txt                  # Python dependencies
```

---

## Installation

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
*Note: This script will try to download the UCI zip file directly. If offline, it will automatically generate a highly realistic synthetic copy matching the exact schema and statistics of the UCI student dataset.*

---

## Usage

Launch the Streamlit Web Application:
```bash
streamlit run app.py
```
Open your browser and navigate to the Local URL provided in your terminal (typically `http://localhost:8501/`).

---

## Dashboard Features

The dashboard is structured into 7 core analytical tabs:
1.  **📊 Dashboard Overview:** High-level KPIs, executive summaries, and cohort demographics.
2.  **📂 Dataset Explorer:** Pagination-enabled raw and cleaned data viewing with export capabilities.
3.  **🧹 Preprocessing & Cleaning:** Transparency logs documenting dataset transformation steps.
4.  **📈 Statistical Analysis:** Deep dive into Pearson correlations, attendance brackets, and study hour impacts.
5.  **🖼️ Visualizations:** Interactive Plotly charts (histograms, donut charts, scatter plots with OLS trendlines).
6.  **🧠 Interactive Predictor:** Machine learning simulation playground.
7.  **💡 Insights & Recommendations:** Actionable data-backed recommendations for early warning systems.

---

## Machine Learning

The application integrates a Multiple Linear Regression model built from scratch using Ordinary Least Squares (`np.linalg.lstsq`).
*   **Features:** Attendance Rate, Weekly Study Time, Past Class Failures, Remedial Support Status, Mother's Education Level.
*   **Target ($y$):** Final Mathematics Grade (G3).
*   **Functionality:** Real-time prediction rendering within the UI, classifying outcomes as PASSING ($\ge 10$) or FAILING ($< 10$).

---

## Results

*   **Linear Correlation:** Calculated using the Pearson Correlation Coefficient ($r$) between attendance percentage and final grade ($G3$).
*   **Data Cleaning Impact:** Highlights how isolating students who missed the final exam (G3 = 0) shifts the correlation from a flat, negligible value to a definitive positive trend, proving attendance contributes directly to higher academic scores.
*   **Study Time Economics:** Demonstrates that shifting a student from "<2 hours" to "2-5 hours" of weekly study yields the highest immediate return on academic performance.

---

## Screenshots placeholders

![Dashboard Overview](placeholder_overview.png)
![Interactive Visualizations](placeholder_visualizations.png)
![ML Grade Predictor](placeholder_predictor.png)

*(Add screenshots of your local application here)*

---

## Live Streamlit Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cognevancestudent-performance-analysis-kst3ljfamigvxqgxyzikwr.streamlit.app/)

---

## GitHub Repository
[Student Performance Analysis Repository](https://github.com/Aryan2125S/cognevance_Student-Performance-Analysis)

---

## Future Improvements
*   Implement advanced regression models (e.g., Random Forest, XGBoost) to capture non-linear relationships.
*   Expand the dataset to include multi-subject data (e.g., Portuguese class scores) to track cross-disciplinary performance.
*   Add student-level longitudinal tracking (Semester 1 vs. Semester 2 attendance dropping rates).
*   Implement automated PDF report generation directly from the Streamlit UI.

---

## Author
**Aryan Sagar**
*2nd-Year Computer Science (AI) Student*
