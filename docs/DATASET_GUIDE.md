# Dataset Guide for Radiomics Student Project

## Overview

This guide helps students download and prepare real medical imaging datasets for their radiomics classification project.

---

## 🏥 Recommended Dataset: TCIA Head-Neck Cancer

### About the Dataset

The **Head-Neck-PET-CT** collection from The Cancer Imaging Archive (TCIA) is ideal for radiomics classification projects.

**Collection Details:**
- **Modality**: CT and PET scans
- **Patients**: ~300+
- **Cancer Type**: Head and neck squamous cell carcinoma (HNSCC)
- **Clinical Data**: Treatment outcomes, survival data
- **Use Case**: Radiation therapy response prediction

### Why This Dataset?

✅ Publicly available (free)  
✅ Includes clinical labels for classification  
✅ Multiple modalities (CT, PET)  
✅ Suitable for radiomics analysis  
✅ Widely used in research

---

## 📥 Download Instructions

### Method 1: TCIA Website (Browser)

1. Visit: https://www.cancerimagingarchive.net/
2. Search for: "Head-Neck-PET-CT"
3. Click on the collection
4. Select subjects to download
5. Download requires registration (free)

### Method 2: NBIA Data Retriever (Recommended)

The NBIA Data Retriever is the official tool for bulk downloads.

**Step 1: Install NBIA Data Retriever**
- Download from: https://wiki.cancerimagingarchive.net/x/2QpRBQ
- Available for Windows, Mac, Linux

**Step 2: Get the List of Subjects**
1. Go to TCIA website
2. Find Head-Neck-PET-CT collection
3. Click "Download" → "Download with NBIA Data Retriever"
4. Save the `.tcia` file

**Step 3: Download**
1. Open NBIA Data Retriever
2. File → Open → Select your `.tcia` file
3. Choose download directory
4. Click "Start Download"

### Method 3: TCIA REST API (For Advanced Users)

```python
# Example using TCIA API
import requests

# Get series for a collection
base_url = "https://services.cancerimagingarchive.net/nbia-api/services/v1"
collection = "Head-Neck-PET-CT"

# Get patients in collection
response = requests.get(f"{base_url}/getPatient?Collection={collection}")
patients = response.json()

print(f"Found {len(patients)} patients")
```

---

## 🗂️ Data Organization

After downloading, organize your data like this:

```
data/
└── head_neck_cancer/
    ├── Patient_001/
    │   ├── CT/                       # CT DICOM series
    │   │   ├── image_001.dcm
    │   │   ├── image_002.dcm
    │   │   └── ...
    │   └── mask.nii.gz               # Segmentation mask (if available)
    ├── Patient_002/
    │   ├── CT/
    │   └── mask.nii.gz
    └── clinical_data.csv             # Labels and clinical info
```

### Clinical Data Format

Create a CSV file with patient labels:

```csv
patient_id,label,age,gender,survival_time
Patient_001,1,65,M,24
Patient_002,0,58,F,60
Patient_003,1,72,M,12
...
```

**Label meanings:**
- `0`: Good outcome / No recurrence
- `1`: Poor outcome / Recurrence

---

## 🔬 Alternative Datasets

### Option 2: BraTS (Brain Tumor Segmentation)

**Website**: https://www.med.upenn.edu/cbica/brats/

**Details:**
- Modality: MRI (T1, T1Gd, T2, FLAIR)
- Task: Glioma segmentation and classification
- Includes: Pre-operative scans with segmentation masks
- Size: ~2000+ cases

**Pros:**
- Includes segmentation masks (no need to create)
- Multiple MRI sequences
- Standardized format

**Cons:**
- Requires registration
- Competition dataset (deadlines)

### Option 3: LUNA16 (Lung Nodule Analysis)

**Website**: https://luna16.grand-challenge.org/

**Details:**
- Modality: CT
- Task: Lung nodule detection
- Size: 888 CT scans

**Pros:**
- Publicly available
- Well-documented

**Cons:**
- No segmentation masks (detection task)
- May require more preprocessing

### Option 4: LiTS (Liver Tumor Segmentation)

**Website**: https://competitions.codalab.org/competitions/17094

**Details:**
- Modality: CT
- Task: Liver and tumor segmentation
- Size: 201 CT scans

**Pros:**
- Includes segmentation masks
- Single organ focus

---

## 🛠️ Data Preprocessing

### Converting DICOM to NIfTI

Most radiomics tools work better with NIfTI format:

```python
import SimpleITK as sitk
import os

def convert_dicom_to_nifti(dicom_dir, output_path):
    """Convert DICOM series to NIfTI"""
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    sitk.WriteImage(image, output_path)

# Example
convert_dicom_to_nifti(
    "data/Patient_001/CT",
    "data/Patient_001/image.nii.gz"
)
```

### Creating Segmentation Masks

If masks are not provided, you may need to:

1. **Use existing segmentations** from dataset
2. **Manual segmentation** using tools like:
   - 3D Slicer (free): https://www.slicer.org/
   - ITK-SNAP (free): http://www.itksnap.org/
3. **Semi-automatic segmentation** using tools

### Sample: Using 3D Slicer

1. Download and install 3D Slicer
2. Load your CT scan
3. Use "Segment Editor" module
4. Create new segmentation
5. Use tools (Paint, Draw, etc.) to segment tumor
6. Export as NIfTI

---

## 📊 Sample Data Description

The project includes synthetic data with these characteristics:

| Feature | Benign (0) | Malignant (1) |
|---------|-----------|---------------|
| Volume | ~1000 voxels | ~2000 voxels |
| Sphericity | ~0.8 | ~0.6 |
| Mean Intensity | ~100 | ~150 |
| Texture | More uniform | More heterogeneous |

This synthetic data demonstrates how radiomics features can distinguish between classes.

---

## ⚠️ Important Notes

### Ethics and Privacy

- **De-identified data**: All public datasets are de-identified
- **No HIPAA concerns**: Public datasets are cleared for research
- **Citation required**: Always cite the dataset source

### Data Quality

1. **Check image resolution**: Ensure consistent voxel spacing
2. **Verify segmentations**: Manual review of masks
3. **Handle missing data**: Some patients may have incomplete data
4. **Normalize intensities**: CT values should be in Hounsfield Units

### Computational Requirements

| Dataset | Images | Disk Space | Processing Time |
|---------|--------|-----------|-----------------|
| Synthetic (20) | 20 | ~10 MB | 1 min |
| TCIA (50 patients) | ~1500 slices | ~2 GB | 30 min |
| BraTS (100 cases) | ~40000 slices | ~50 GB | 2+ hours |

---

## 📝 Citation

If using TCIA Head-Neck-PET-CT:

```
Vallières, M. et al. (2017). 
"Radiomics strategies for risk assessment of tumour recurrence in 
early-stage lung and head & neck cancers."
Scientific Reports, 7(1), 1-14.
```

If using BraTS:

```
Menze, B.H. et al. (2015).
"The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)."
IEEE Transactions on Medical Imaging, 34(10), 1993-2024.
```

---

## 🔗 Quick Links

- **TCIA Home**: https://www.cancerimagingarchive.net/
- **NBIA Data Retriever**: https://wiki.cancerimagingarchive.net/x/2QpRBQ
- **3D Slicer**: https://www.slicer.org/
- **ITK-SNAP**: http://www.itksnap.org/

---

## ❓ FAQ

**Q: Do I need ethics approval?**  
A: No, for publicly available de-identified datasets.

**Q: Can I use these datasets for my thesis?**  
A: Yes, but check specific license terms for each dataset.

**Q: What if the download fails?**  
A: Try using the NBIA Data Retriever or contact TCIA support.

**Q: Can I use my own hospital data?**  
A: Only with proper ethics approval and de-identification.

---

**Last Updated**: March 2026
