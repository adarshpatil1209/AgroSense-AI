def calculate_water_deficit(crop_type, stage):
    """
    Calculates the 8-day water deficit using FAO-56.
    etc = kc * et0
    deficit = etc - (effective_rainfall + soil_storage)
    """
    # Marathwada kharif representative values
    et0 = 4.8  # mm/day
    effective_rainfall = 2.57  # mm/day
    soil_storage = 0.6  # mm/day
    
    # FAO-56 Table 12 simplified lookup
    # Format: {crop: {stage: kc}}
    kc_lookup = {
        'Paddy': {'sowing': 1.05, 'vegetative': 1.10, 'reproductive': 1.20, 'maturity': 0.90},
        'Cotton': {'sowing': 0.35, 'vegetative': 0.85, 'reproductive': 1.15, 'maturity': 0.70},
        'Sugarcane': {'sowing': 0.40, 'vegetative': 0.80, 'reproductive': 1.25, 'maturity': 0.75},
        'Soybean': {'sowing': 0.40, 'vegetative': 0.80, 'reproductive': 1.15, 'maturity': 0.50},
        'Fallow': {'sowing': 0.20, 'vegetative': 0.20, 'reproductive': 0.20, 'maturity': 0.20}
    }
    
    # Default to fallow/sowing if not found
    kc = kc_lookup.get(crop_type, kc_lookup['Fallow']).get(stage, 0.5)
    
    etc = kc * et0
    daily_deficit = etc - (effective_rainfall + soil_storage)
    
    # 8-day deficit
    eight_day_deficit = max(0, daily_deficit * 8)
    
    if eight_day_deficit > 15:
        advisory = "Urgent irrigation"
    elif eight_day_deficit > 5:
        advisory = "Light irrigation"
    else:
        advisory = "No action"
        
    return round(eight_day_deficit, 2), advisory
