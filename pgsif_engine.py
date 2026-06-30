def pgsif_stress_index(stage, ndvi_anomaly, ndwi, sar_vh_vv, vci, smi):
    """
    Phenology-Gated Stress Index Fusion.
    Returns (index_name, index_value, stress_level) based on detected growth stage.
    """
    if stage == "sowing" or stage == "fallow":
        # combine NDVI anomaly + SMI
        value = 0.5 * abs(ndvi_anomaly) + 0.5 * smi
        index_name = "NDVI_anomaly + SMI"
        if value > 0.6: stress_level = "Severe"
        elif value > 0.3: stress_level = "Moderate"
        else: stress_level = "Low"
        
    elif stage == "vegetative":
        value = ndwi
        index_name = "NDWI"
        # For NDWI, lower means water stress
        if value < -0.1: stress_level = "Severe"
        elif value < 0.1: stress_level = "Moderate"
        else: stress_level = "Low"
        
    elif stage == "reproductive":
        value = sar_vh_vv
        index_name = "SAR VH/VV ratio"
        # lower VH/VV during reproductive stage water stress
        if value < 0.3: stress_level = "Severe"
        elif value < 0.45: stress_level = "Moderate"
        else: stress_level = "Low"
        
    elif stage == "maturity":
        value = vci
        index_name = "VCI"
        # VCI: < 40 is stress
        if value < 0.3: stress_level = "Severe"
        elif value < 0.5: stress_level = "Moderate"
        else: stress_level = "Low"
        
    else:
        value = 0
        index_name = "None"
        stress_level = "Low"
        
    return index_name, value, stress_level
