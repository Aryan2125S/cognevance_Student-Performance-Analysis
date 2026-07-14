import os
from flask import Flask, render_template, request, abort
import pandas as pd

# Import our custom modules
from src.data_loader import load_and_preprocess, get_data_paths
from src.analyzer import run_analysis_pipeline

app = Flask(__name__)

# Ensure data is ready on startup
raw_path, processed_path = get_data_paths()
if not os.path.exists(raw_path):
    print("WARNING: Raw data not found. Run setup_dataset.py first.")

# Cache variables
cleaned_df = None
analysis_data = None
cleaning_log = None

def get_app_data():
    """Loads and caches data and analysis results."""
    global cleaned_df, analysis_data, cleaning_log
    
    # Check if raw data exists. If not, try to run setup_dataset
    if not os.path.exists(raw_path):
        try:
            print("Running dataset setup...")
            import setup_dataset
        except ImportError:
            pass
            
    # Clean data if processed dataset doesn't exist
    if not os.path.exists(processed_path) or cleaned_df is None:
        try:
            cleaned_df, cleaning_log = load_and_preprocess()
        except Exception as e:
            print(f"Error loading and preprocessing: {e}")
            # Fallback empty df
            cleaned_df = pd.DataFrame()
            cleaning_log = {}
            
    # Run analysis if results aren't cached
    if analysis_data is None:
        try:
            analysis_data = run_analysis_pipeline()
        except Exception as e:
            print(f"Error running analysis pipeline: {e}")
            analysis_data = {}
            
    return cleaned_df, analysis_data, cleaning_log

@app.route('/')
def home():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    return render_template(
        'home.html', 
        page='home', 
        stats=analysis_data.get('overall', {})
    )

@app.route('/preview')
def dataset_preview():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    
    # Paginate dataset preview to keep page light and interactive
    page_num = request.args.get('page', 1, type=int)
    per_page = 20
    
    # Choose between 'raw' and 'cleaned' view
    data_type = request.args.get('type', 'cleaned')
    
    if data_type == 'raw' and os.path.exists(raw_path):
        df_to_show = pd.read_csv(raw_path, sep=';')
    else:
        df_to_show = cleaned_df
        
    total_rows = len(df_to_show)
    total_pages = max(1, (total_rows + per_page - 1) // per_page)
    
    # Clamp page range
    page_num = max(1, min(page_num, total_pages))
    start_idx = (page_num - 1) * per_page
    end_idx = min(start_idx + per_page, total_rows)
    
    subset = df_to_show.iloc[start_idx:end_idx]
    
    # Convert subset to list of dicts and columns for custom rendering
    records = subset.to_dict(orient='records')
    columns = list(df_to_show.columns)
    
    return render_template(
        'dataset_preview.html',
        page='preview',
        records=records,
        columns=columns,
        current_page=page_num,
        total_pages=total_pages,
        total_rows=total_rows,
        start_idx=start_idx + 1,
        end_idx=end_idx,
        data_type=data_type
    )

@app.route('/cleaning')
def cleaning_summary():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    return render_template(
        'cleaning_summary.html',
        page='cleaning',
        log=cleaning_log
    )

@app.route('/analysis')
def data_analysis():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    return render_template(
        'analysis.html',
        page='analysis',
        analysis=analysis_data
    )

@app.route('/visualizations')
def visualizations():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    return render_template(
        'visualizations.html',
        page='visualizations'
    )

@app.route('/insights')
def insights():
    cleaned_df, analysis_data, cleaning_log = get_app_data()
    return render_template(
        'insights.html',
        page='insights',
        analysis=analysis_data
    )

if __name__ == '__main__':
    # Initialize cache on startup
    get_app_data()
    # Run the development server
    app.run(debug=True, port=5000)
