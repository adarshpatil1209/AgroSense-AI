def detect_stage(ndvi_series, current_month_idx):
    """
    Phase 1 rule-based stage detector — to be replaced by trained 1D-CNN 
    once labeled multi-season ground truth is available.
    
    ndvi_series: list or array of NDVI values up to the current month (or all 12 months)
    current_month_idx: integer 0-11 representing the current month
    """
    if current_month_idx < 1:
        return "sowing"
        
    current_ndvi = ndvi_series[current_month_idx]
    prev_ndvi = ndvi_series[current_month_idx - 1]
    
    # Basic logic to classify current week into Sowing/Vegetative/Reproductive/Maturity 
    # based on NDVI trajectory shape
    
    if current_ndvi < 0.2:
        return "sowing"  # near-zero = sowing/fallow
        
    delta = current_ndvi - prev_ndvi
    
    if delta > 0.05 and current_ndvi < 0.7:
        return "vegetative" # rising slope
    elif abs(delta) <= 0.05 and current_ndvi >= 0.5:
        return "reproductive" # peak plateau
    elif delta < -0.05 and current_ndvi > 0.3:
        return "maturity" # declining slope
    else:
        # fallback based on magnitude
        if current_ndvi > 0.6:
            return "reproductive"
        elif current_ndvi > 0.3:
            return "vegetative"
        else:
            return "sowing"
