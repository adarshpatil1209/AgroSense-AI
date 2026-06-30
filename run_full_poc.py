import pandas as pd
import numpy as np
import os
import joblib

from generate_synthetic_data import generate_dataset
from train_classifier import train_and_evaluate
from phenology_stage_detector import detect_stage
from pgsif_engine import pgsif_stress_index
from fao56_water_balance import calculate_water_deficit

def main():
    print("Starting AgroSense AI Proof-of-Concept Pipeline\n")
    
    print("STEP 1: Generating Synthetic Data")
    generate_dataset(num_samples=300)
    
    print("\nSTEP 2: Training Random Forest Classifier")
    train_and_evaluate()
    
    print("\nSTEP 3-5: Running Phenology, PGSIF, and FAO-56 on Pilot Fields")
    # Load dataset for pilot village evaluation (first 100 fields)
    df = pd.read_csv('outputs/synthetic_features.csv')
    pilot_df = df.head(100).copy()
    
    # Load model to predict crop types for the pilot village
    clf = joblib.load('outputs/rf_model.joblib')
    feature_cols = [c for c in df.columns if c not in ['field_id', 'crop_type']]
    pilot_df['predicted_crop'] = clf.predict(pilot_df[feature_cols])
    
    # For PoC, let's assume we are in month 8 (August/September, 0-indexed month 7)
    current_month_idx = 7
    
    results = []
    
    for _, row in pilot_df.iterrows():
        field_id = row['field_id']
        crop = row['predicted_crop']
        
        # Extract NDVI time series
        ndvi_series = [row[f'ndvi_m{m+1}'] for m in range(12)]
        
        # Step 3: Detect stage
        stage = detect_stage(ndvi_series, current_month_idx)
        
        # Synthetic variables for PGSIF
        ndvi_anomaly = np.random.normal(0, 0.1)
        smi = np.random.uniform(0.1, 0.9)
        vci = np.random.uniform(0.1, 0.9)
        
        ndwi_current = row[f'ndwi_m{current_month_idx+1}']
        sar_vh_vv_current = row['sar_vh_vv'] # approximation
        
        # Step 4: PGSIF
        index_name, index_val, stress_level = pgsif_stress_index(
            stage, ndvi_anomaly, ndwi_current, sar_vh_vv_current, vci, smi
        )
        
        # Step 5: FAO-56
        deficit_mm, advisory = calculate_water_deficit(crop, stage)
        
        results.append({
            'Field ID': field_id,
            'Crop Type (predicted)': crop,
            'Growth Stage': stage,
            'Stress Index Used': index_name,
            'Index Value': round(index_val, 4),
            'Stress Level': stress_level,
            '8-Day Water Deficit (mm)': deficit_mm,
            'Irrigation Advisory': advisory
        })
        
    results_df = pd.DataFrame(results)
    
    print("\nSTEP 6: Final Summary Output")
    # Print first 15 for console demo
    print(results_df.head(15).to_string(index=False))
    
    results_df.to_csv('outputs/pilot_village_summary.csv', index=False)
    print(f"\nSaved comprehensive pilot village summary with {len(results_df)} fields to outputs/pilot_village_summary.csv")
    
    print("\nPipeline Complete!")

if __name__ == '__main__':
    main()
