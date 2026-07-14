import os
import pandas as pd
import numpy as np

def get_data_paths():
    """Returns absolute paths to raw and processed data directories."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, 'data', 'raw', 'student-mat.csv')
    processed_path = os.path.join(base_dir, 'data', 'processed', 'student-cleaned.csv')
    return raw_path, processed_path

def load_and_preprocess():
    """Loads raw dataset, cleans it, adds analytical columns, and saves the result."""
    raw_path, processed_path = get_data_paths()
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found at {raw_path}. Please run setup_dataset.py first.")
        
    print(f"Loading raw data from: {raw_path}")
    # Raw dataset is semicolon-separated
    df = pd.read_csv(raw_path, sep=';')
    
    # 1. Check for missing values (None in original, but good practice to verify)
    missing_counts = df.isnull().sum().sum()
    print(f"Checking for missing values: Found {missing_counts} missing cells.")
    
    # 2. Handle G3 = 0 (anomalous zeros that indicate exam absence or dropouts)
    # If G1 and G2 are reasonable (e.g. > 5) but G3 is 0, they likely did not take the final exam.
    df['status'] = np.where((df['G3'] == 0) & (df['G1'] > 0), 'Absent/Dropout', 'Active')
    
    # 3. Calculate Attendance Rate (%)
    # Assuming a standard school year of 180 days
    df['attendance_rate'] = ((180 - df['absences']) / 180 * 100).round(1)
    
    # 4. Categorize Attendance
    # Good: >=90%, Average: 75%-89%, Poor: <75%
    def categorize_attendance(rate):
        if rate >= 90.0:
            return 'Good (>=90%)'
        elif rate >= 75.0:
            return 'Average (75-89%)'
        else:
            return 'Poor (<75%)'
            
    df['attendance_category'] = df['attendance_rate'].apply(categorize_attendance)
    
    # 5. Calculate Average Academic Score (G1, G2, G3 average)
    df['average_grade'] = df[['G1', 'G2', 'G3']].mean(axis=1).round(2)
    
    # 6. Map studytime to descriptive labels for plotting and display
    studytime_map = {
        1: '<2 hours',
        2: '2-5 hours',
        3: '5-10 hours',
        4: '>10 hours'
    }
    df['study_hours'] = df['studytime'].map(studytime_map)
    
    # 7. Map parental education to descriptive labels
    edu_map = {
        0: 'None',
        1: 'Primary (4th Grade)',
        2: '5th - 9th Grade',
        3: 'Secondary',
        4: 'Higher Education'
    }
    df['mother_education'] = df['Medu'].map(edu_map)
    df['father_education'] = df['Fedu'].map(edu_map)
    
    # Save the processed, cleaned dataset as comma-separated
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Processed dataset successfully saved to: {processed_path} ({df.shape[0]} rows, {df.shape[1]} columns)")
    
    # Generate a brief data cleaning report dictionary for the UI
    cleaning_summary = {
        "raw_row_count": len(df),
        "missing_values_handled": int(missing_counts),
        "absent_final_exam_count": int((df['status'] == 'Absent/Dropout').sum()),
        "average_attendance_rate": float(df['attendance_rate'].mean()),
        "max_absences": int(df['absences'].max()),
        "columns_added": ["status", "attendance_rate", "attendance_category", "average_grade", "study_hours", "mother_education", "father_education"]
    }
    
    return df, cleaning_summary

if __name__ == "__main__":
    load_and_preprocess()
