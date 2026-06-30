import numpy as np
import pandas as pd
import os

def generate_crop_curve(crop_type, num_months=12):
    # Base baseline
    nir = np.full(num_months, 0.2)
    red = np.full(num_months, 0.1)
    green = np.full(num_months, 0.08)
    blue = np.full(num_months, 0.05)
    vh_vv = np.full(num_months, 0.5)

    if crop_type == 'Paddy':
        # June(5) to Nov(10)
        growth_months = [5, 6, 7, 8, 9, 10]
        for m in growth_months:
            nir[m] = 0.4 + np.sin((m-5)/5 * np.pi) * 0.3
            red[m] = 0.1 - np.sin((m-5)/5 * np.pi) * 0.05
            green[m] = 0.1 + np.sin((m-5)/5 * np.pi) * 0.05
            vh_vv[m] = 0.5 - np.sin((m-5)/5 * np.pi) * 0.2  # lower during reproductive
    elif crop_type == 'Cotton':
        # May(4) to Dec(11)
        growth_months = list(range(4, 12))
        for m in growth_months:
            nir[m] = 0.3 + np.sin((m-4)/7 * np.pi) * 0.25
            red[m] = 0.1 - np.sin((m-4)/7 * np.pi) * 0.04
            green[m] = 0.08 + np.sin((m-4)/7 * np.pi) * 0.04
            vh_vv[m] = 0.6 - np.sin((m-4)/7 * np.pi) * 0.15
    elif crop_type == 'Sugarcane':
        # Year round, peak in Oct(9)
        for m in range(12):
            nir[m] = 0.35 + np.sin(m/11 * np.pi) * 0.2
            red[m] = 0.08 - np.sin(m/11 * np.pi) * 0.03
            green[m] = 0.1 + np.sin(m/11 * np.pi) * 0.05
            vh_vv[m] = 0.4 - np.sin(m/11 * np.pi) * 0.1
    elif crop_type == 'Soybean':
        # June(5) to Sep(8)
        growth_months = [5, 6, 7, 8]
        for m in growth_months:
            nir[m] = 0.3 + np.sin((m-5)/3 * np.pi) * 0.35
            red[m] = 0.1 - np.sin((m-5)/3 * np.pi) * 0.06
            green[m] = 0.09 + np.sin((m-5)/3 * np.pi) * 0.06
            vh_vv[m] = 0.5 - np.sin((m-5)/3 * np.pi) * 0.15
    elif crop_type == 'Fallow':
        # Flat mostly
        nir += np.random.normal(0, 0.02, num_months)
        red += np.random.normal(0, 0.02, num_months)
        green += np.random.normal(0, 0.02, num_months)
        vh_vv += np.random.normal(0, 0.05, num_months)
        
    return nir, red, green, blue, vh_vv

def generate_dataset(num_samples=300):
    np.random.seed(42)
    crops = ['Paddy', 'Cotton', 'Sugarcane', 'Soybean', 'Fallow']
    
    data = []
    
    for i in range(num_samples):
        crop = np.random.choice(crops)
        nir, red, green, blue, vh_vv = generate_crop_curve(crop)
        
        # Add noise
        nir += np.random.normal(0, 0.03, 12)
        red += np.random.normal(0, 0.02, 12)
        green += np.random.normal(0, 0.02, 12)
        blue += np.random.normal(0, 0.01, 12)
        vh_vv += np.random.normal(0, 0.05, 12)
        
        # Compute indices
        ndvi = (nir - red) / (nir + red + 1e-8)
        ndwi = (green - nir) / (green + nir + 1e-8)
        evi = 2.5 * ((nir - red) / (nir + 6 * red - 7.5 * blue + 1))
        
        row = {'field_id': f'F_{i:03d}', 'crop_type': crop}
        for m in range(12):
            row[f'ndvi_m{m+1}'] = ndvi[m]
            row[f'ndwi_m{m+1}'] = ndwi[m]
            row[f'evi_m{m+1}'] = evi[m]
            
        # Single SAR ratio feature for the season (e.g., minimum representing the reproductive peak)
        row['sar_vh_vv'] = np.min(vh_vv)
            
        data.append(row)
        
    df = pd.DataFrame(data)
    os.makedirs('outputs', exist_ok=True)
    df.to_csv('outputs/synthetic_features.csv', index=False)
    print(f"Generated synthetic dataset with {len(df)} samples: outputs/synthetic_features.csv")

if __name__ == '__main__':
    generate_dataset()
