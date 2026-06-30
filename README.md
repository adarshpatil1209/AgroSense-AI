
# AgroSense AI — Proof-of-Concept (Pilot Village Scale)

This project is an end-to-end proof-of-concept (PoC) for the AgroSense AI pipeline. It is designed to validate the core logic of our system, specifically the crop classification and the Phenology-Gated Stress Index Fusion (PGSIF) decision engine, on a small scale.

## What is Real vs. What is Simulated

To allow this PoC to run locally without external dependencies or heavy computation, we have clearly defined boundaries:

### 1. Simulated / Placeholders
* **Satellite Data**: No live Google Earth Engine (GEE) APIs are called. The input reflectance bands (NIR, Red, Green, Blue) and SAR VH/VV ratios are simulated using realistic, literature-based seasonal curves for a kharif season in Maharashtra.
* **1D-CNN Phenology Detector**: The current code uses a Phase 1 rule-based stage detector based on the shape of the NDVI trajectory. The 1D-CNN is documented as future work once labeled multi-season ground truth is gathered.

### 2. Real / Implemented Logic
* **Random Forest Classifier**: We train a real `scikit-learn` Random Forest classifier on 37 input features (12 months of NDVI, NDWI, EVI, plus a SAR ratio feature). The evaluation (Accuracy, Kappa, feature importances, and confusion matrix) uses real ML validation techniques.
* **PGSIF Engine**: The logic that selects which stress index to use based on the crop's current growth stage (e.g., NDWI for vegetative, SAR VH/VV for reproductive) is fully implemented.
* **FAO-56 Water Deficit**: The dual crop coefficient calculation is implemented using real FAO-56 Table 12 values and representative Marathwada environmental data (ET0, effective rainfall, soil storage).

## Pipeline Execution

Run the complete end-to-end pipeline using the following command:

```bash
python run_full_poc.py
```

This will run all steps and generate artifacts in the `outputs/` folder.

## Outputs
* `outputs/synthetic_features.csv`
* `outputs/confusion_matrix.png`
* `outputs/feature_importance.png`
* `outputs/pilot_village_summary.csv`

# AgroSense-AI
Phenology-Aware Satellite Intelligence for Precision Irrigation

