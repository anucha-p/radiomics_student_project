# Radiomics Machine Learning - Student Worksheet

## Project: Medical Image Classification using Radiomics Features

**Name:** _____________________ **Date:** _____________________

---

## Part 1: Understanding the Data

### 1.1 Dataset Information

| Property | Value |
|----------|-------|
| Dataset name | _____________________ |
| Number of samples | _______ |
| Number of features | _______ |
| Modality | _______ |
| Classification task | _____________________ |

### 1.2 Class Distribution

| Class | Count | Percentage |
|-------|-------|------------|
| Class 0 (______) | _______ | _______ % |
| Class 1 (______) | _______ | _______ % |

---

## Part 2: Advanced Image Processing (Notebook 01b)

### 2.1 Intensity Normalization
**Compare Z-score and Min-Max normalization.** 
Which one is more robust to outliers in a CT scan with metallic artifacts?
_________________________________________________

### 2.2 Gray-Level Discretization
**Observe the effect of `binWidth`.**
If you increase `binWidth` from 5 to 50, does the number of unique gray levels in the texture matrix increase or decrease?
_________________________________________________

How does this affect the computation time and the detail captured?
_________________________________________________

### 2.3 Filter Visualization
**Laplacian of Gaussian (LoG):**
Describe the visual difference between $\sigma=1.0$ and $\sigma=5.0$.
_________________________________________________

**Wavelets:**
Which wavelet decomposition (e.g., HLH, LHL) seems to highlight vertical edges best in your sample image?
_________________________________________________

---

## Part 3: Feature Exploration & Extraction

### 3.1 Feature Categories

Count how many features fall into each category:

| Category | Count | Examples |
|----------|-------|----------|
| First-order | _______ | original_firstorder_Mean |
| Shape | _______ | original_shape_Volume |
| Texture (GLCM+) | _______ | original_glcm_Contrast |
| Filtered | _______ | wavelet-LLH_glcm_* |

### 3.2 Feature Correlation

**Which features are highly correlated (|r| > 0.8)?**
_________________________________________________

**Why might this be a problem for certain ML models?**
_________________________________________________

---

## Part 4: Data Preprocessing & Selection

### 4.1 Preprocessing Steps Applied

☐ Missing value imputation  
☐ Feature standardization (z-score)  
☐ Feature selection (Method: _____________________)

### 4.2 Top Selected Features

List the top 3 selected features:

1. _____________________
2. _____________________
3. _____________________

**What do these features represent physically?**
_________________________________________________

---

## Part 5: Model Training & Evaluation

### 5.1 Models Compared

| Model | CV AUC Mean | CV AUC Std |
|-------|-------------|------------|
| Logistic Regression | _______ | _______ |
| Random Forest | _______ | _______ |
| SVM | _______ | _______ |

### 5.2 Test Set Results

| Metric | Value |
|--------|-------|
| Accuracy | _______ |
| F1-Score | _______ |
| AUC-ROC | _______ |

---

## Part 6: Critical Thinking & Clinical Impact

### 6.1 Clinical Plausibility
**Are your top features clinically meaningful?** (e.g., does a high entropy value correspond to a more "heterogeneous/messy" tumor?)
_________________________________________________

### 6.2 Trust and Validation
**Would you trust this model for clinical decision-making? Why or why not?**
_________________________________________________
_________________________________________________

---

## Summary Checklist

- [ ] Explored and justified image processing parameters (NB 01b)
- [ ] Extracted features (NB 01)
- [ ] Built and compared ML models (NB 02)
- [ ] Evaluated on held-out test set
- [ ] Documented findings in this worksheet

---

**Submission**: Completed notebook files + This worksheet + Summary report (1 page)
