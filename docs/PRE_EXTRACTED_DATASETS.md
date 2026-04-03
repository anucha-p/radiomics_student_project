# Pre-Extracted Radiomics Datasets for Students

## 🎯 Quick Start: Ready-to-Use Datasets

For students who want to skip feature extraction and go straight to machine learning, here are datasets with **pre-extracted radiomics features** in CSV format.

---

## Option 1: radMLBench (Recommended)

The **radMLBench** collection contains 50+ datasets with pre-extracted radiomics features ready for machine learning.

### Website
- **GitHub**: https://github.com/aydindemircioglu/radMLBench
- **Datasets**: https://github.com/aydindemircioglu/radMLBench/tree/main/datasets

### Key Features
✅ Features already extracted using PyRadiomics (IBSI-compliant)  
✅ Binary classification tasks  
✅ CSV format (gzip compressed)  
✅ Includes ID and Target columns  
✅ Easy to load in Python/pandas

### How to Download

#### Method A: Direct Download from GitHub

1. Go to: https://github.com/aydindemircioglu/radMLBench/tree/main/datasets
2. Click on any dataset (e.g., `LNDb.csv.gz`, `HNSCC.csv.gz`)
3. Click "Download" or "Raw"
4. Extract: `gunzip filename.csv.gz`

#### Method B: Using Python

```python
import pandas as pd
import requests
import gzip
import io

# Download directly
def download_radmlbench_dataset(dataset_name):
    url = f"https://raw.githubusercontent.com/aydindemircioglu/radMLBench/main/datasets/{dataset_name}.csv.gz"
    
    response = requests.get(url)
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as f:
        df = pd.read_csv(f)
    
    return df

# Example
df = download_radmlbench_dataset("LNDb")
print(df.shape)  # (173, 107) - 173 samples, 105 features + ID + Target
```

#### Method C: Using radMLBench Python Package

```bash
pip install radMLBench
```

```python
from radMLBench import loadData

# Load dataset
df = loadData("LNDb")

# Or as numpy arrays
X, y = loadData("LNDb", return_X_y=True)
```

### Recommended Small Datasets for Students

| Dataset | Modality | Samples | Features | Task | Class Balance |
|---------|----------|---------|----------|------|---------------|
| **LNDb** | CT | 173 | 105 | Lung nodule type | 66% |
| **HNSCC** | CT | 93 | 105 | HPV status | 27% |
| **Head-Neck-Radiomics-HN1** | CT | 137 | 105 | Survival prediction | 45% |
| **NSCLC-Radiogenomics** | PET/CT | 144 | 105 | Mutation prediction | 16% |
| **QIN-HEADNECK** | PET/CT | 59 | 210 | Classification | 75% |
| **Ahn2021** | MRI | 114 | 108 | Breast cancer subtype | 55% |
| **C4KC-KiTS** | CT | 70 | 315 | Kidney tumor | 66% |
| **Meningioma-SEG-CLASS** | MRI | 88 | 2030 | Tumor grade | 43% |

**Best for beginners**: LNDb, HNSCC, or Head-Neck-Radiomics-HN1 (smaller feature sets)

---

## Option 2: Synthetic Sample Dataset (Included)

We've created a **synthetic radiomics dataset** that mimics real data for demonstration purposes.

### Location
```
radiomics_student_project/data/
├── radiomics_sample.csv           # 100 samples, 50 features
├── radiomics_small.csv            # 50 samples, 30 features
├── radiomics_medium.csv           # 100 samples, 50 features
├── radiomics_large.csv            # 200 samples, 100 features
└── lung_cancer_radiomics.csv      # 200 samples, 40 features
```

### Characteristics
- **ID column**: Patient identifier
- **Target column**: Binary label (0 = benign, 1 = malignant)
- **Feature columns**: Follow radiomics nomenclature
  - `original_firstorder_*` - First-order statistics
  - `original_shape_*` - Shape features
  - `original_glcm_*` - Texture features (GLCM)
  - `original_glrlm_*` - Texture features (GLRLM)
  - `original_glszm_*` - Texture features (GLSZM)

### To Use in Notebook 02

```python
import pandas as pd

# Load pre-extracted features
features_df = pd.read_csv('../data/radiomics_sample.csv')

# Extract feature columns
feature_cols = [col for col in features_df.columns 
                if col not in ['ID', 'Target']]

# Now proceed with ML pipeline!
X = features_df[feature_cols]
y = features_df['Target']
```

---

## Option 3: Create Your Own Synthetic Dataset

If you need a specific size or want to understand data structure:

```python
# Generate synthetic radiomics data
import numpy as np
import pandas as pd

def create_synthetic_radiomics(n_samples=100, n_features=50, random_state=42):
    np.random.seed(random_state)
    
    # Generate feature names
    feature_names = []
    
    # First-order features
    for name in ['Mean', 'Median', 'Variance', 'Skewness', 'Kurtosis', 
                 'Entropy', 'Energy', 'Minimum', 'Maximum']:
        feature_names.append(f'original_firstorder_{name}')
    
    # Shape features
    for name in ['Volume', 'SurfaceArea', 'Sphericity', 'Compactness1', 
                 'Elongation', 'Flatness']:
        feature_names.append(f'original_shape_{name}')
    
    # Texture features
    for name in ['Contrast', 'Correlation', 'Energy', 'Homogeneity']:
        feature_names.append(f'original_glcm_{name}')
    
    # Fill remaining
    while len(feature_names) < n_features:
        feature_names.append(f'original_feature_{len(feature_names)}')
    
    feature_names = feature_names[:n_features]
    
    # Generate data with class differences
    n_benign = n_samples // 2
    n_malignant = n_samples - n_benign
    
    # Benign - smaller, more uniform
    benign_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            benign_data[feat] = np.random.lognormal(7, 0.5, n_benign)
        elif 'Sphericity' in feat:
            benign_data[feat] = np.random.beta(8, 2, n_benign)
        elif 'Entropy' in feat:
            benign_data[feat] = np.random.normal(3.5, 0.5, n_benign)
        else:
            benign_data[feat] = np.random.normal(0, 1, n_benign)
    
    # Malignant - larger, irregular
    malignant_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            malignant_data[feat] = np.random.lognormal(7.7, 0.6, n_malignant)
        elif 'Sphericity' in feat:
            malignant_data[feat] = np.random.beta(4, 4, n_malignant)
        elif 'Entropy' in feat:
            malignant_data[feat] = np.random.normal(4.5, 0.6, n_malignant)
        else:
            malignant_data[feat] = np.random.normal(0.5, 1.2, n_malignant)
    
    # Combine
    benign_df = pd.DataFrame(benign_data)
    benign_df['ID'] = [f'Benign_{i+1:03d}' for i in range(n_benign)]
    benign_df['Target'] = 0
    
    malignant_df = pd.DataFrame(malignant_data)
    malignant_df['ID'] = [f'Malignant_{i+1:03d}' for i in range(n_malignant)]
    malignant_df['Target'] = 1
    
    df = pd.concat([benign_df, malignant_df], ignore_index=True)
    
    # Reorder
    cols = ['ID', 'Target'] + feature_names
    df = df[cols]
    
    return df

# Create and save
df = create_synthetic_radiomics(n_samples=100, n_features=50)
df.to_csv('my_synthetic_radiomics.csv', index=False)
```

---

## Option 4: Other Public Datasets

### UCI Machine Learning Repository
Some medical datasets available:
- https://archive.ics.uci.edu/ml/datasets.php
- Search for "cancer" or "diagnosis"

### Kaggle
- https://www.kaggle.com/datasets
- Search for "cancer classification" or "medical imaging"

### Papers with Code
- https://paperswithcode.com/datasets
- Filter by "Medical Imaging"

---

## 📋 Dataset Format Reference

### Standard Format for Notebook 02

Your CSV should have these columns:

| Column | Description |
|--------|-------------|
| `ID` | Unique patient identifier (string) |
| `Target` | Binary label: 0 or 1 |
| `feature_1` ... `feature_n` | Radiomics features (numeric) |

### Example

```csv
ID,Target,original_firstorder_Mean,original_shape_Sphericity,...
Patient_001,0,45.3,0.82,...
Patient_002,1,78.5,0.54,...
Patient_003,0,52.1,0.79,...
```

---

## 🔗 Quick Links

| Resource | URL |
|----------|-----|
| radMLBench GitHub | https://github.com/aydindemircioglu/radMLBench |
| radMLBench Datasets | https://github.com/aydindemircioglu/radMLBench/tree/main/datasets |
| PyRadiomics | https://pyradiomics.readthedocs.io/ |
| TCIA (real images) | https://www.cancerimagingarchive.net/ |

---

## ⚡ Recommendation for Your Class

Suggested approach for teaching:

1. **For Demo**: Use the included `radiomics_sample.csv` (100 samples)
   - Load instantly
   - No external downloads needed
   - Balanced classes

2. **For Student Practice**: radMLBench `LNDb` or `HNSCC`
   - Real pre-extracted features
   - 100-200 samples (manageable)
   - ~100 features

3. **For Advanced Students**: Larger datasets like `Meningioma-SEG-CLASS`
   - 88 samples, 2030 features
   - Challenge: high dimensionality
   - Opportunity to teach feature selection

---

**Last Updated**: March 2026
