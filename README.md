# Radiomics for Medical Image Classification

Student project for learning radiomics feature extraction and machine learning classification on medical images.

### Open in Google Colab

| Notebook | Description | Colab |
|----------|-------------|-------|
| `00_data_exploration` | EDA & data quality checks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| `01_feature_extraction` | PyRadiomics feature extraction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| `01b_advanced_image_processing`| Manual preprocessing & filters | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| `02_machine_learning` | ML training & evaluation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |

> **Note:** Update the Colab URLs above once the notebooks are hosted on GitHub.

## 📚 Learning Objectives

1. **Radiomics Feature Extraction**
   - Understand first-order statistics
   - Learn shape features
   - Explore texture features (GLCM, GLRLM, GLSZM, GLDM, NGTDM)
   - Use PyRadiomics library

2. **Machine Learning Pipeline**
   - Data preprocessing and standardization
   - Feature selection techniques
   - Cross-validation strategy
   - Model training and evaluation
   - Performance metrics interpretation

3. **Medical Image Analysis**
   - **New**: Manual intensity normalization and discretization (binning)
   - **New**: Advanced filtering (LoG, Wavelets)
   - Work with DICOM/NIfTI formats
   - Understand ROI segmentation
   - Apply radiomics to clinical problems

## 📁 Project Structure

```
radiomics_student_project/
├── notebooks/
│   ├── 00_data_exploration.ipynb      # ⭐ Start here! EDA & data quality
│   ├── 01_feature_extraction.ipynb    # Feature extraction with PyRadiomics
│   ├── 01b_advanced_image_processing.ipynb # Advanced IP & Filter Viz
│   └── 02_machine_learning.ipynb      # ML training and evaluation
├── scripts/
│   ├── download_radmlbench_datasets.py # Download real datasets
│   └── sample_radiomics_dataset.py     # Generate sample data
├── data/                               # Download datasets here
├── docs/
│   ├── images/                        # Slide images (pipeline diagram)
│   ├── SLIDES.md                      # Marp presentation slides
│   ├── DATASET_GUIDE.md               # Guide to real datasets
│   ├── PRE_EXTRACTED_DATASETS.md      # Pre-extracted CSV datasets
│   └── STUDENT_WORKSHEET.md           # Student worksheet with rubric
├── outputs/                            # Results and figures
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🚀 Quick Start

### Option 1: Google Colab (Recommended for Students)

1. Upload the notebooks to Google Colab (or click the Colab badges above)
2. Start with `00_data_exploration.ipynb` to understand your data
3. Run `01_feature_extraction.ipynb` for feature extraction
4. Explore `01b_advanced_image_processing.ipynb` to understand the math
5. Continue with `02_machine_learning.ipynb` for ML

### Option 2: Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Clone or download this project
cd radiomics_student_project

# Run notebooks
jupyter notebook notebooks/
```

## 📊 Datasets

### Synthetic Data (Included)
- Auto-generated for demonstration
- 20 patients with CT-like images
- Binary classification (benign/malignant)

### Real Medical Datasets

#### 1. TCIA Head-Neck Cancer (Recommended)
- **Source**: [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/)
- **Collection**: Head-Neck-PET-CT
- **Size**: ~300+ patients
- **Modality**: CT, PET
- **Task**: Radiation therapy response prediction

#### 2. BraTS (Brain Tumor)
- **Source**: [ BraTS Challenge](https://www.med.upenn.edu/cbica/brats/)
- **Modality**: MRI (T1, T2, FLAIR)
- **Task**: Glioma segmentation and classification

#### 3. LUNA16 (Lung Nodules)
- **Source**: [LUNA16 Challenge](https://luna16.grand-challenge.org/)
- **Modality**: CT
- **Task**: Lung nodule detection

See [docs/DATASET_GUIDE.md](docs/DATASET_GUIDE.md) for download instructions.

## 🎓 Learning Path

### Part 1: Feature Extraction & Image Processing (Notebooks 01 & 01b)

**Duration**: 3-4 hours

**Topics**:
- What is radiomics?
- PyRadiomics configuration
- Image Preprocessing: Manual Z-score, Min-Max, and binning
- Filtering: Laplacian of Gaussian (LoG) and Wavelets
- Single and batch extraction
- Feature visualization

**Deliverable**: CSV file with extracted features + IP analysis report

### Part 2: Machine Learning (Notebook 02)

**Duration**: 3-4 hours

**Topics**:
- Data preprocessing
- Feature standardization
- Feature selection (F-test, mutual information)
- Cross-validation
- Model comparison (Logistic Regression, Random Forest, SVM)
- Performance evaluation
- Model interpretation

**Deliverable**: Trained model and evaluation report

## 🔬 Standard Radiomics Pipeline

```
Medical Images (CT/MRI)
    ↓
Segmentation Mask (ROI)
    ↓
Feature Extraction (PyRadiomics)
    ↓
Feature Matrix
    ↓
Preprocessing (Standardization)
    ↓
Feature Selection
    ↓
Machine Learning Model
    ↓
Performance Evaluation
```

## 📈 Expected Outcomes

Students will be able to:

1. Extract ~100+ radiomic features from medical images
2. Mathematically justify preprocessing and filtering choices
3. Build a classification model with AUC > 0.75
4. Interpret feature importance
5. Evaluate model performance using proper metrics
6. Understand clinical relevance of radiomics

## 📝 Assignment Ideas

1. **Basic**: Complete both notebooks with synthetic data
2. **Intermediate**: Apply to real dataset from TCIA
3. **Advanced**: Compare different feature selection methods and models

## 🔗 Resources

### Documentation
- [PyRadiomics Documentation](https://pyradiomics.readthedocs.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

### Tutorials
- [Radiomics for Beginners](https://pmc.ncbi.nlm.nih.gov/articles/PMC6837295/)
- [Medical Image Processing with Python](https://theaisummer.com/medical-image-python/)

### Papers
- Lambin et al. (2012) - Radiomics: extracting more information from medical images
- Zwanenburg et al. (2020) - The Image Biomarker Standardization Initiative

## 🐛 Troubleshooting

### Issue: PyRadiomics installation fails
**Solution**: Install build dependencies first
```bash
sudo apt-get install build-essential python3-dev
pip install pyradiomics
```

### Issue: Out of memory in Google Colab
**Solution**: Reduce batch size or number of images

### Issue: No real dataset available
**Solution**: Use synthetic data provided or download from TCIA

## 📧 Support

For questions about this project, contact your instructor.

For PyRadiomics issues, visit: https://github.com/Radiomics/pyradiomics

## 📄 License

This educational project is provided for academic use.

## 🙏 Acknowledgments

- PyRadiomics team
- TCIA for providing public datasets
- Scikit-learn community

---

**Last Updated**: March 2026
**Version**: 1.1 (Master's Special Edition)
