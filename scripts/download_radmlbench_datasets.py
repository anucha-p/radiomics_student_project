#!/usr/bin/env python3
"""
Download radiomics datasets from radMLBench repository
These datasets have pre-extracted radiomics features ready for ML

Source: https://github.com/aydindemircioglu/radMLBench
Paper: radMLBench: A radiomics dataset collection for benchmarking in radiomics
        Computers in Biology and Medicine, Volume 182, 2024
"""

import os
import pandas as pd
import requests
import gzip
import shutil

# Base URL for raw files on GitHub
GITHUB_RAW_URL = "https://raw.githubusercontent.com/aydindemircioglu/radMLBench/main/datasets"

# Recommended small-to-medium datasets for students
RECOMMENDED_DATASETS = {
    "LNDb": {
        "description": "Lung nodule detection (CT)",
        "n_samples": 173,
        "n_features": 105,
        "modality": "CT",
        "task": "Binary classification (nodule type)",
        "class_balance": "66%"
    },
    "HNSCC": {
        "description": "Head and neck squamous cell carcinoma (CT)",
        "n_samples": 93,
        "n_features": 105,
        "modality": "CT",
        "task": "Binary classification (HPV status)",
        "class_balance": "27%"
    },
    "Head-Neck-Radiomics-HN1": {
        "description": "Head and neck cancer outcome prediction",
        "n_samples": 137,
        "n_features": 105,
        "modality": "CT",
        "task": "Binary classification (survival)",
        "class_balance": "45%"
    },
    "NSCLC-Radiogenomics": {
        "description": "Non-small cell lung cancer (PET/CT)",
        "n_samples": 144,
        "n_features": 105,
        "modality": "PET/CT",
        "task": "Binary classification (mutation)",
        "class_balance": "16%"
    },
    "QIN-HEADNECK": {
        "description": "Head and neck cancer (PET/CT)",
        "n_samples": 59,
        "n_features": 210,
        "modality": "PET/CT",
        "task": "Binary classification",
        "class_balance": "75%"
    },
    "Ahn2021": {
        "description": "Breast cancer (MRI)",
        "n_samples": 114,
        "n_features": 108,
        "modality": "MRI",
        "task": "Binary classification (molecular subtype)",
        "class_balance": "55%"
    },
    "C4KC-KiTS": {
        "description": "Kidney tumor segmentation (CT)",
        "n_samples": 70,
        "n_features": 315,
        "modality": "CT",
        "task": "Binary classification",
        "class_balance": "66%"
    },
    "Meningioma-SEG-CLASS": {
        "description": "Meningioma brain tumors (MRI)",
        "n_samples": 88,
        "n_features": 2030,
        "modality": "MRI",
        "task": "Binary classification (grade)",
        "class_balance": "43%"
    }
}


def download_dataset(dataset_name, output_dir="./radmlbench_datasets"):
    """
    Download a specific dataset from radMLBench
    
    Args:
        dataset_name: Name of the dataset (e.g., 'LNDb', 'HNSCC')
        output_dir: Directory to save the dataset
    
    Returns:
        Path to the downloaded CSV file
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # File names
    gz_filename = f"{dataset_name}.csv.gz"
    csv_filename = f"{dataset_name}.csv"
    
    gz_path = os.path.join(output_dir, gz_filename)
    csv_path = os.path.join(output_dir, csv_filename)
    
    # Skip if already exists
    if os.path.exists(csv_path):
        print(f"✓ {dataset_name} already exists at {csv_path}")
        return csv_path
    
    # Download from GitHub
    url = f"{GITHUB_RAW_URL}/{gz_filename}"
    
    try:
        print(f"Downloading {dataset_name}...")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        # Save gz file
        with open(gz_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Extract gzip
        with gzip.open(gz_path, 'rb') as f_in:
            with open(csv_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        # Remove gz file
        os.remove(gz_path)
        
        print(f"✓ Downloaded {dataset_name} to {csv_path}")
        return csv_path
        
    except Exception as e:
        print(f"✗ Error downloading {dataset_name}: {str(e)}")
        return None


def download_all_recommended(output_dir="./radmlbench_datasets"):
    """Download all recommended datasets"""
    print("=" * 60)
    print("Downloading Recommended Radiomics Datasets")
    print("=" * 60)
    print()
    
    downloaded = []
    failed = []
    
    for name in RECOMMENDED_DATASETS.keys():
        path = download_dataset(name, output_dir)
        if path:
            downloaded.append(name)
        else:
            failed.append(name)
    
    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {len(downloaded)}/{len(RECOMMENDED_DATASETS)}")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    print()
    
    return downloaded


def inspect_dataset(csv_path):
    """Inspect a downloaded dataset"""
    df = pd.read_csv(csv_path)
    
    print(f"\nDataset: {os.path.basename(csv_path)}")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {df.shape[1]}")
    print(f"  Rows: {df.shape[0]}")
    
    if 'Target' in df.columns:
        print(f"  Class distribution:")
        print(f"    {df['Target'].value_counts().to_dict()}")
    
    # Check for ID column
    id_col = None
    for col in ['ID', 'id', 'Id']:
        if col in df.columns:
            id_col = col
            break
    
    if id_col:
        print(f"  ID column: {id_col}")
    
    # Feature columns (excluding ID and Target)
    feature_cols = [c for c in df.columns if c not in ['ID', 'id', 'Id', 'Target', 'target']]
    print(f"  Feature columns: {len(feature_cols)}")
    
    return df


def create_small_dataset(output_path="./sample_radiomics.csv", n_samples=100):
    """
    Create a small synthetic radiomics dataset for testing
    Uses similar feature structure to real radiomics data
    """
    np.random.seed(42)
    
    n_features = 50
    n_benign = n_samples // 2
    n_malignant = n_samples - n_benign
    
    # Generate feature names similar to radiomics
    feature_names = []
    
    # First-order features
    firstorder = ['Mean', 'Median', 'Variance', 'Skewness', 'Kurtosis', 
                  'Minimum', 'Maximum', 'Entropy', 'Energy']
    for name in firstorder:
        feature_names.append(f'original_firstorder_{name}')
    
    # Shape features
    shape = ['Volume', 'SurfaceArea', 'Sphericity', 'Compactness1', 'Compactness2',
             'Elongation', 'Flatness', 'Roundness']
    for name in shape[:8]:
        feature_names.append(f'original_shape_{name}')
    
    # GLCM features
    glcm = ['Contrast', 'Correlation', 'Energy', 'Homogeneity', 'Entropy',
            'Autocorrelation', 'ClusterProminence', 'ClusterShade']
    for name in glcm[:8]:
        feature_names.append(f'original_glcm_{name}')
    
    # GLRLM features
    glrlm = ['GrayLevelNonUniformity', 'RunLengthNonUniformity', 'RunPercentage',
             'LowGrayLevelRunEmphasis', 'HighGrayLevelRunEmphasis']
    for name in glrlm[:5]:
        feature_names.append(f'original_glrlm_{name}')
    
    # Fill remaining with generic features
    while len(feature_names) < n_features:
        feature_names.append(f'original_feature_{len(feature_names)}')
    
    feature_names = feature_names[:n_features]
    
    # Generate data
    # Benign - smaller values, more uniform
    benign_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            benign_data[feat] = np.random.normal(1000, 200, n_benign)
        elif 'Sphericity' in feat:
            benign_data[feat] = np.random.beta(8, 2, n_benign)  # High sphericity
        elif 'Mean' in feat or 'Median' in feat:
            benign_data[feat] = np.random.normal(100, 20, n_benign)
        elif 'Entropy' in feat:
            benign_data[feat] = np.random.normal(3.5, 0.5, n_benign)
        else:
            benign_data[feat] = np.random.normal(0, 1, n_benign)
    
    # Malignant - larger values, more irregular
    malignant_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            malignant_data[feat] = np.random.normal(2000, 400, n_malignant)
        elif 'Sphericity' in feat:
            malignant_data[feat] = np.random.beta(4, 4, n_malignant)  # Lower sphericity
        elif 'Mean' in feat or 'Median' in feat:
            malignant_data[feat] = np.random.normal(150, 30, n_malignant)
        elif 'Entropy' in feat:
            malignant_data[feat] = np.random.normal(4.5, 0.7, n_malignant)
        else:
            malignant_data[feat] = np.random.normal(0.5, 1.2, n_malignant)
    
    # Create DataFrames
    benign_df = pd.DataFrame(benign_data)
    benign_df['ID'] = [f'Benign_{i+1:03d}' for i in range(n_benign)]
    benign_df['Target'] = 0
    
    malignant_df = pd.DataFrame(malignant_data)
    malignant_df['ID'] = [f'Malignant_{i+1:03d}' for i in range(n_malignant)]
    malignant_df['Target'] = 1
    
    # Combine
    df = pd.concat([benign_df, malignant_df], ignore_index=True)
    
    # Reorder columns
    cols = ['ID', 'Target'] + feature_names
    df = df[cols]
    
    # Save
    df.to_csv(output_path, index=False)
    print(f"✓ Created synthetic dataset: {output_path}")
    print(f"  Shape: {df.shape}")
    print(f"  Class distribution: {dict(df['Target'].value_counts())}")
    
    return df


if __name__ == "__main__":
    import argparse
    import numpy as np
    
    parser = argparse.ArgumentParser(description="Download radiomics datasets from radMLBench")
    parser.add_argument(
        "--dataset", 
        type=str, 
        default="all",
        help="Dataset name to download (default: all recommended)"
    )
    parser.add_argument(
        "--output-dir", 
        type=str, 
        default="./radmlbench_datasets",
        help="Output directory for downloaded datasets"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available datasets"
    )
    parser.add_argument(
        "--create-sample",
        action="store_true",
        help="Create a small synthetic sample dataset"
    )
    parser.add_argument(
        "--inspect",
        type=str,
        help="Inspect a downloaded dataset"
    )
    
    args = parser.parse_args()
    
    if args.list:
        print("=" * 70)
        print("Recommended Datasets for Students")
        print("=" * 70)
        print()
        for name, info in RECOMMENDED_DATASETS.items():
            print(f"{name}")
            print(f"  Description: {info['description']}")
            print(f"  Samples: {info['n_samples']}, Features: {info['n_features']}")
            print(f"  Modality: {info['modality']}, Task: {info['task']}")
            print(f"  Class balance: {info['class_balance']}")
            print()
    
    elif args.create_sample:
        create_small_dataset()
    
    elif args.inspect:
        if os.path.exists(args.inspect):
            inspect_dataset(args.inspect)
        else:
            print(f"File not found: {args.inspect}")
    
    elif args.dataset == "all":
        download_all_recommended(args.output_dir)
    else:
        download_dataset(args.dataset, args.output_dir)
