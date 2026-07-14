import os
import pandas as pd
import matplotlib
# Use non-interactive backend for server-side chart rendering
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def get_paths():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_path = os.path.join(base_dir, 'data', 'processed', 'student-cleaned.csv')
    img_dir = os.path.join(base_dir, 'static', 'images')
    return processed_path, img_dir

def generate_visualizations(df, img_dir):
    """Generates the four required charts with premium styling and saves them as PNGs."""
    os.makedirs(img_dir, exist_ok=True)
    
    # Set premium aesthetic styling
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16,
        'figure.facecolor': '#f8fafc',  # Matches light slate background
        'axes.facecolor': '#ffffff'
    })
    
    # Modern color palette
    colors = {
        'primary': '#4f46e5',   # Indigo
        'secondary': '#06b6d4', # Teal
        'accent': '#8b5cf6',    # Violet
        'success': '#10b981',   # Emerald
        'danger': '#f43f5e',    # Rose
        'dark': '#1e293b',      # Slate Dark
        'light': '#f8fafc'      # Slate Light
    }
    
    # --- CHART 1: Histogram (Grade Distribution) ---
    plt.figure(figsize=(8, 5))
    # We filter out G3 = 0 (exam absences) to show the true academic distribution of active participants,
    # but we can also show the original. Let's show active students' G3 scores.
    active_students = df[df['status'] == 'Active']
    sns.histplot(data=active_students, x='G3', bins=15, kde=True, color=colors['primary'], edgecolor='#ffffff')
    plt.title('Distribution of Final Grades (G3) for Active Students', pad=15, color=colors['dark'], weight='bold')
    plt.xlabel('Final Grade (0-20 scale)', labelpad=10)
    plt.ylabel('Number of Students', labelpad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'grade_distribution.png'), dpi=150)
    plt.close()
    
    # --- CHART 2: Pie Chart (Attendance Categories) ---
    plt.figure(figsize=(6, 6))
    attendance_counts = df['attendance_category'].value_counts()
    # Align category names nicely
    labels = attendance_counts.index
    sizes = attendance_counts.values
    # Clean colors for the categories: Good (Emerald), Average (Teal), Poor (Rose)
    pie_colors = [colors['success'], colors['secondary'], colors['danger']]
    
    plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=pie_colors,
        textprops={'fontsize': 11, 'color': colors['dark'], 'weight': 'semibold'},
        wedgeprops={'edgecolor': '#f8fafc', 'linewidth': 2}
    )
    plt.title('Breakdown of Student Attendance Categories', pad=15, color=colors['dark'], weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'attendance_pie.png'), dpi=150)
    plt.close()
    
    # --- CHART 3: Bar Chart (Average Final Grade by Study Time) ---
    plt.figure(figsize=(8, 5))
    # Define order of study hours
    study_order = ['<2 hours', '2-5 hours', '5-10 hours', '>10 hours']
    
    # Calculate means for error bar display or standard seaborn barplot
    sns.barplot(
        data=df, 
        x='study_hours', 
        y='G3', 
        order=study_order, 
        hue='study_hours',
        legend=False,
        palette=[colors['secondary'], colors['primary'], colors['accent'], '#ec4899'],
        edgecolor='#ffffff',
        errorbar=None
    )
    plt.title('Average Final Grade (G3) by Weekly Study Hours', pad=15, color=colors['dark'], weight='bold')
    plt.xlabel('Weekly Study Time', labelpad=10)
    plt.ylabel('Average Final Grade (0-20)', labelpad=10)
    plt.ylim(0, 20)
    
    # Add values on top of bars
    ax = plt.gca()
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(p.get_x() + p.get_width() / 2, height + 0.3),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, weight='bold', color=colors['dark'])
                    
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'study_vs_grade.png'), dpi=150)
    plt.close()
    
    # --- CHART 4: Scatter Plot (Attendance Rate vs Final Grade) ---
    plt.figure(figsize=(8, 5))
    # We will plot Active and Absent students separately to make the chart extremely professional
    sns.scatterplot(
        data=df, 
        x='attendance_rate', 
        y='G3', 
        hue='status',
        palette={'Active': colors['primary'], 'Absent/Dropout': colors['danger']},
        alpha=0.7,
        s=50
    )
    # Fit a regression line only for active students to show the actual learning relationship
    active_df = df[df['status'] == 'Active']
    sns.regplot(
        data=active_df, 
        x='attendance_rate', 
        y='G3', 
        scatter=False,
        ax=plt.gca(),
        line_kws={'color': colors['success'], 'linewidth': 2.5, 'label': 'Trend Line (Active Students)'}
    )
    plt.title('Relationship: Attendance Rate (%) vs. Final Grade (G3)', pad=15, color=colors['dark'], weight='bold')
    plt.xlabel('Attendance Rate (%)', labelpad=10)
    plt.ylabel('Final Grade (G3)', labelpad=10)
    plt.xlim(df['attendance_rate'].min() - 2, 102)
    plt.ylim(-1, 21)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'attendance_vs_grade.png'), dpi=150)
    plt.close()
    print("All visualizations generated and saved in static/images/.")

def perform_analysis(df):
    """Calculates all key analytical insights and returns them in a structured dictionary."""
    # 1. Overall Statistics
    total_students = len(df)
    active_students_df = df[df['status'] == 'Active']
    absent_students_count = len(df) - len(active_students_df)
    
    overall_stats = {
        "total_students": total_students,
        "active_students": len(active_students_df),
        "absent_students": absent_students_count,
        "mean_g3_all": round(df['G3'].mean(), 2),
        "mean_g3_active": round(active_students_df['G3'].mean(), 2),
        "median_g3": int(df['G3'].median()),
        "max_g3": int(df['G3'].max()),
        "min_g3": int(df['G3'].min()),
        "mean_attendance": round(df['attendance_rate'].mean(), 2),
        "median_attendance": round(df['attendance_rate'].median(), 2)
    }
    
    # 2. Correlation between Attendance Rate and Academic Scores
    # We check G3 (Final Score) and Average Grade
    corr_attendance_g3_all = round(df['attendance_rate'].corr(df['G3']), 4)
    corr_attendance_g3_active = round(active_students_df['attendance_rate'].corr(active_students_df['G3']), 4)
    corr_attendance_avg = round(df['attendance_rate'].corr(df['average_grade']), 4)
    
    correlation_results = {
        "corr_attendance_g3_all": corr_attendance_g3_all,
        "corr_attendance_g3_active": corr_attendance_g3_active,
        "corr_attendance_avg": corr_attendance_avg,
        # Interpret strength of correlation
        "interpretation_all": get_correlation_interpretation(corr_attendance_g3_all),
        "interpretation_active": get_correlation_interpretation(corr_attendance_g3_active)
    }
    
    # 3. Attendance Category Breakdown
    att_cat_means = df.groupby('attendance_category', as_index=False).agg(
        student_count=('G3', 'count'),
        average_final_grade=('G3', 'mean'),
        average_attendance=('attendance_rate', 'mean')
    ).round(2).to_dict(orient='records')
    
    # 4. Study Hours Group Analysis
    study_order = ['<2 hours', '2-5 hours', '5-10 hours', '>10 hours']
    study_grouped = df.groupby('study_hours').agg(
        student_count=('G3', 'count'),
        average_final_grade=('G3', 'mean')
    ).reindex(study_order).round(2)
    study_grouped['hours_label'] = study_grouped.index
    study_grouped_dict = study_grouped.to_dict(orient='records')
    
    # 5. Parental Education Impact
    mother_edu = df.groupby('mother_education').agg(
        student_count=('G3', 'count'),
        average_final_grade=('G3', 'mean')
    ).round(2).to_dict(orient='index')
    
    father_edu = df.groupby('father_education').agg(
        student_count=('G3', 'count'),
        average_final_grade=('G3', 'mean')
    ).round(2).to_dict(orient='index')
    
    # 6. School Support Impact
    school_support = df.groupby('schoolsup').agg(
        student_count=('G3', 'count'),
        average_final_grade=('G3', 'mean')
    ).round(2).to_dict(orient='index')

    return {
        "overall": overall_stats,
        "correlation": correlation_results,
        "attendance_groups": att_cat_means,
        "study_groups": study_grouped_dict,
        "mother_education": mother_edu,
        "father_education": father_edu,
        "school_support": school_support
    }

def get_correlation_interpretation(val):
    abs_val = abs(val)
    direction = "positive" if val > 0 else "negative"
    if abs_val < 0.1:
        strength = "negligible"
    elif abs_val < 0.3:
        strength = "weak"
    elif abs_val < 0.5:
        strength = "moderate"
    else:
        strength = "strong"
        
    return f"There is a {strength} {direction} linear relationship ({val}) between attendance rate and final grade."

def run_analysis_pipeline():
    processed_path, img_dir = get_paths()
    if not os.path.exists(processed_path):
        raise FileNotFoundError(f"Processed dataset not found at {processed_path}. Please run src/data_loader.py first.")
        
    df = pd.read_csv(processed_path)
    generate_visualizations(df, img_dir)
    analysis_results = perform_analysis(df)
    return analysis_results

if __name__ == "__main__":
    results = run_analysis_pipeline()
    print("\n--- ANALYSIS RESULTS PREVIEW ---")
    print(f"Overall Class Size: {results['overall']['total_students']} students")
    print(f"Mean Final Grade: {results['overall']['mean_g3_all']} / 20")
    print(f"Attendance-Grade Correlation (All): {results['correlation']['corr_attendance_g3_all']}")
    print(f"Attendance-Grade Correlation (Active): {results['correlation']['corr_attendance_g3_active']}")
    print(f"Correlation Interpretation (Active): {results['correlation']['interpretation_active']}")
