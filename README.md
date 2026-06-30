# 🌱 AgroSense AI

> **Phenology-Aware Satellite Intelligence for Precision Irrigation**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-orange)

AgroSense AI is an AI-powered precision agriculture system that integrates machine learning, vegetation indices, SAR data, and FAO-56 water balance modeling to estimate crop stress and support irrigation decisions.

The project demonstrates an end-to-end pipeline for crop classification, phenology detection, stress estimation, and irrigation recommendation using synthetic satellite data that closely resembles real-world agricultural conditions.

---

# 📚 Table of Contents

- Overview
- Features
- Project Architecture
- Pipeline Workflow
- Project Structure
- Outputs
- Current Limitations
- Future Roadmap
- License
- Author

---

# 📖 Overview

Agriculture faces increasing challenges due to climate variability, water scarcity, and the need for efficient irrigation management.

AgroSense AI addresses these challenges by combining:

- Satellite-derived vegetation indices
- SAR-based crop monitoring
- Machine Learning
- FAO-56 crop water balance
- Phenology-aware stress estimation

Instead of relying on a single vegetation index throughout the crop lifecycle, AgroSense AI selects the most informative stress indicator according to the crop's current growth stage using the Phenology-Gated Stress Index Fusion (PGSIF) engine.

---

# 🚀 Features

✅ Random Forest Crop Classification

- Multi-feature classification
- 37 input features
- Scikit-learn implementation

---

✅ Phenology Stage Detection

- Rule-based stage detection
- Growth-stage estimation using NDVI trajectory

---

✅ PGSIF Decision Engine

- Vegetative stage → NDWI
- Reproductive stage → SAR VH/VV
- Maturity stage → Combined indicators

---

✅ FAO-56 Water Balance

- Dual crop coefficient method
- Water deficit estimation
- Representative environmental parameters

---

✅ End-to-End Pipeline

Synthetic Data

↓

Feature Engineering

↓

Crop Classification

↓

Phenology Detection

↓

PGSIF Engine

↓

FAO-56 Water Balance

↓

Pilot Village Summary

---

# 🏗️ System Architecture

> Replace this with your architecture diagram.

![Architecture](docs/architecture.png)

---

# 🔄 Pipeline Workflow

> Replace with your pipeline image.

![Pipeline](docs/pipeline.png)

---

# 📂 Project Structure

```text
AgroSense-AI/
│
├── data/
│
├── docs/
│   ├── architecture.png
│   ├── pipeline.png
│
├── outputs/
│
├── src/
│   ├── fao56_water_balance.py
│   ├── pgsif_engine.py
│   ├── phenology_stage_detector.py
│   ├── train_classifier.py
│   └── generate_synthetic_data.py
│
├── run_full_poc.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🧠 Machine Learning Pipeline

### Step 1

Generate synthetic satellite observations

↓

### Step 2

Extract features

- NDVI
- NDWI
- EVI
- SAR Ratio

↓

### Step 3

Train Random Forest classifier

↓

### Step 4

Detect crop phenology

↓

### Step 5

Apply PGSIF engine

↓

### Step 6

Estimate water deficit using FAO-56

↓

### Step 7

Generate irrigation insights

---

# 📊 Generated Outputs

The pipeline automatically generates:

- synthetic_features.csv
- confusion_matrix.png
- feature_importance.png
- pilot_village_summary.csv

Example:

```
outputs/
├── confusion_matrix.png
├── feature_importance.png
├── pilot_village_summary.csv
└── synthetic_features.csv
```

---



# ⚠️ Current Limitations

This repository is a Proof of Concept.

Current limitations include:

- Synthetic satellite data
- Rule-based phenology detection
- No Google Earth Engine integration
- No real Sentinel imagery
- No cloud deployment

---

# 🛣️ Future Roadmap

- Google Earth Engine integration
- Sentinel-2 imagery
- Sentinel-1 SAR integration
- 1D CNN phenology detector
- Deep Learning crop classifier
- Streamlit dashboard
- REST API
- Mobile application
- Docker support
- Cloud deployment
- Real-world validation

---


# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Adarsh Patil**

AI & Machine Learning Student


GitHub:
https://github.com/adarshpatil1209

---
