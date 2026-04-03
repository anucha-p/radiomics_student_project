#!/usr/bin/env python3
"""
Create sample radiomics datasets for student projects
These are synthetic datasets that mimic real radiomics features
"""

import pandas as pd
import numpy as np
import os

def create_radiomics_dataset(
    n_samples=100,
    n_features=50,
    output_path="sample_radiomics.csv",
    random_state=42
):
    """
    Create a synthetic radiomics dataset for classification
    
    Args:
        n_samples: Number of samples
        n_features: Number of radiomic features
        output_path: Path to save CSV
        random_state: Random seed
    
    Returns:
        DataFrame with radiomics features
    """
    np.random.seed(random_state)
    
    n_benign = n_samples // 2
    n_malignant = n_samples - n_benign
    
    # Generate feature names following radiomics nomenclature
    feature_names = []
    
    # First-order statistics (10 features)
    firstorder = ['Mean', 'Median', 'Variance', 'Skewness', 'Kurtosis', 
                  'Minimum', 'Maximum', 'Range', 'Entropy', 'Energy',
                  'TotalEnergy', 'Uniformity', 'InterquartileRange', 
                  'MeanAbsoluteDeviation', 'RobustMeanAbsoluteDeviation',
                  'RootMeanSquared', 'StandardDeviation', '10Percentile', '90Percentile']
    for name in firstorder[:10]:
        feature_names.append(f'original_firstorder_{name}')
    
    # Shape features (14 features)
    shape = ['VoxelVolume', 'MeshVolume', 'SurfaceArea', 'SurfaceVolumeRatio',
             'Compactness1', 'Compactness2', 'Sphericity', 'Maximum3DDiameter',
             'Maximum2DDiameterSlice', 'Maximum2DDiameterColumn', 'Maximum2DDiameterRow',
             'MajorAxisLength', 'MinorAxisLength', 'LeastAxisLength', 'Elongation',
             'Flatness', 'Roundness']
    for name in shape[:12]:
        feature_names.append(f'original_shape_{name}')
    
    # GLCM features (24 features)
    glcm = ['Contrast', 'Correlation', 'Energy', 'Homogeneity', 'Entropy',
            'Autocorrelation', 'ClusterProminence', 'ClusterShade', 'ClusterTendency',
            'DifferenceAverage', 'DifferenceEntropy', 'DifferenceVariance',
            'Id', 'Idm', 'Idmn', 'Idn', 'Imc1', 'Imc2', 'InverseVariance',
            'JointAverage', 'JointEnergy', 'JointEntropy', 'MCC', 'MaximumProbability',
            'SumAverage', 'SumEntropy', 'SumSquares']
    for name in glcm[:12]:
        feature_names.append(f'original_glcm_{name}')
    
    # GLRLM features (16 features)
    glrlm = ['GrayLevelNonUniformity', 'GrayLevelNonUniformityNormalized',
             'RunLengthNonUniformity', 'RunLengthNonUniformityNormalized',
             'RunPercentage', 'RunVariance', 'GrayLevelVariance',
             'LongRunEmphasis', 'LongRunHighGrayLevelEmphasis',
             'LongRunLowGrayLevelEmphasis', 'ShortRunEmphasis',
             'ShortRunHighGrayLevelEmphasis', 'ShortRunLowGrayLevelEmphasis',
             'LowGrayLevelRunEmphasis', 'HighGrayLevelRunEmphasis']
    for name in glrlm[:8]:
        feature_names.append(f'original_glrlm_{name}')
    
    # GLSZM features (16 features)
    glszm = ['GrayLevelNonUniformity', 'GrayLevelNonUniformityNormalized',
             'SizeZoneNonUniformity', 'SizeZoneNonUniformityNormalized',
             'ZonePercentage', 'ZoneVariance', 'GrayLevelVariance',
             'LargeAreaEmphasis', 'LargeAreaHighGrayLevelEmphasis',
             'LargeAreaLowGrayLevelEmphasis', 'SmallAreaEmphasis',
             'SmallAreaHighGrayLevelEmphasis', 'SmallAreaLowGrayLevelEmphasis',
             'LowGrayLevelZoneEmphasis', 'HighGrayLevelZoneEmphasis']
    for name in glszm[:8]:
        feature_names.append(f'original_glszm_{name}')
    
    # Fill to desired number
    while len(feature_names) < n_features:
        feature_names.append(f'original_feature_{len(feature_names)}')
    
    feature_names = feature_names[:n_features]
    
    # Generate data for benign tumors (class 0)
    benign_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            benign_data[feat] = np.random.lognormal(7, 0.5, n_benign)  # ~1000 voxels
        elif 'Sphericity' in feat:
            benign_data[feat] = np.random.beta(7, 2, n_benign)  # High sphericity (0.8)
        elif 'Compactness' in feat:
            benign_data[feat] = np.random.beta(3, 4, n_benign)  # More compact
        elif 'Mean' in feat or 'Median' in feat:
            benign_data[feat] = np.random.normal(50, 15, n_benign)
        elif 'Variance' in feat or 'StandardDeviation' in feat:
            benign_data[feat] = np.random.lognormal(3, 0.3, n_benign)
        elif 'Skewness' in feat:
            benign_data[feat] = np.random.normal(0, 0.5, n_benign)
        elif 'Kurtosis' in feat:
            benign_data[feat] = np.random.normal(3, 0.5, n_benign)
        elif 'Entropy' in feat:
            benign_data[feat] = np.random.normal(3.5, 0.5, n_benign)
        elif 'Energy' in feat or 'TotalEnergy' in feat:
            benign_data[feat] = np.random.lognormal(10, 0.5, n_benign)
        elif 'SurfaceArea' in feat:
            benign_data[feat] = np.random.lognormal(7, 0.5, n_benign)
        elif 'Contrast' in feat:
            benign_data[feat] = np.random.lognormal(3, 0.5, n_benign)
        elif 'Correlation' in feat:
            benign_data[feat] = np.random.beta(7, 3, n_benign)  # High correlation
        elif 'Homogeneity' in feat:
            benign_data[feat] = np.random.beta(6, 2, n_benign)
        elif 'GrayLevelNonUniformity' in feat or 'SizeZoneNonUniformity' in feat:
            benign_data[feat] = np.random.lognormal(8, 0.4, n_benign)
        elif 'Elongation' in feat or 'Flatness' in feat:
            benign_data[feat] = np.random.beta(4, 4, n_benign)
        elif 'Maximum3DDiameter' in feat or 'AxisLength' in feat:
            benign_data[feat] = np.random.lognormal(4, 0.3, n_benign)
        else:
            # Generic feature
            benign_data[feat] = np.random.normal(0, 1, n_benign)
    
    # Generate data for malignant tumors (class 1)
    malignant_data = {}
    for feat in feature_names:
        if 'Volume' in feat:
            malignant_data[feat] = np.random.lognormal(7.7, 0.6, n_malignant)  # ~2200 voxels
        elif 'Sphericity' in feat:
            malignant_data[feat] = np.random.beta(4, 4, n_malignant)  # Lower sphericity (0.5)
        elif 'Compactness' in feat:
            malignant_data[feat] = np.random.beta(4, 3, n_malignant)  # Less compact
        elif 'Mean' in feat or 'Median' in feat:
            malignant_data[feat] = np.random.normal(75, 20, n_malignant)
        elif 'Variance' in feat or 'StandardDeviation' in feat:
            malignant_data[feat] = np.random.lognormal(3.5, 0.4, n_malignant)  # Higher variance
        elif 'Skewness' in feat:
            malignant_data[feat] = np.random.normal(0.3, 0.7, n_malignant)
        elif 'Kurtosis' in feat:
            malignant_data[feat] = np.random.normal(3.5, 0.7, n_malignant)
        elif 'Entropy' in feat:
            malignant_data[feat] = np.random.normal(4.5, 0.6, n_malignant)  # Higher entropy
        elif 'Energy' in feat or 'TotalEnergy' in feat:
            malignant_data[feat] = np.random.lognormal(11, 0.6, n_malignant)  # Higher energy
        elif 'SurfaceArea' in feat:
            malignant_data[feat] = np.random.lognormal(7.7, 0.6, n_malignant)
        elif 'Contrast' in feat:
            malignant_data[feat] = np.random.lognormal(4, 0.5, n_malignant)  # Higher contrast
        elif 'Correlation' in feat:
            malignant_data[feat] = np.random.beta(5, 5, n_malignant)  # Lower correlation
        elif 'Homogeneity' in feat:
            malignant_data[feat] = np.random.beta(4, 4, n_malignant)
        elif 'GrayLevelNonUniformity' in feat or 'SizeZoneNonUniformity' in feat:
            malignant_data[feat] = np.random.lognormal(9, 0.5, n_malignant)  # Less uniform
        elif 'Elongation' in feat or 'Flatness' in feat:
            malignant_data[feat] = np.random.beta(3, 3, n_malignant)  # More irregular
        elif 'Maximum3DDiameter' in feat or 'AxisLength' in feat:
            malignant_data[feat] = np.random.lognormal(4.5, 0.4, n_malignant)
        else:
            # Generic feature - slight shift
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
    
    print(f"✓ Created radiomics dataset: {output_path}")
    print(f"  Samples: {df.shape[0]}")
    print(f"  Features: {df.shape[1] - 2} (excluding ID and Target)")
    print(f"  Class distribution:")
    print(f"    Benign (0): {n_benign} samples")
    print(f"    Malignant (1): {n_malignant} samples")
    
    return df


def create_multiple_datasets(output_dir="./sample_datasets"):
    """Create multiple sample datasets of different sizes"""
    os.makedirs(output_dir, exist_ok=True)
    
    datasets = [
        {"name": "small", "n_samples": 50, "n_features": 30},
        {"name": "medium", "n_samples": 100, "n_features": 50},
        {"name": "large", "n_samples": 200, "n_features": 100},
    ]
    
    created_files = []
    
    for ds in datasets:
        path = os.path.join(output_dir, f"radiomics_{ds['name']}.csv")
        df = create_radiomics_dataset(
            n_samples=ds['n_samples'],
            n_features=ds['n_features'],
            output_path=path
        )
        created_files.append(path)
    
    print()
    print(f"✓ Created {len(created_files)} sample datasets in {output_dir}")
    
    return created_files


def create_lung_cancer_dataset(output_path="lung_cancer_radiomics.csv"):
    """
    Create a synthetic dataset simulating lung cancer radiomics
    Based on typical radiomics studies for lung nodules
    """
    np.random.seed(42)
    
    n_benign = 120
    n_malignant = 80
    
    # Feature names
    feature_names = [
        # First-order
        'original_firstorder_Mean', 'original_firstorder_Median',
        'original_firstorder_Variance', 'original_firstorder_Skewness',
        'original_firstorder_Kurtosis', 'original_firstorder_Entropy',
        'original_firstorder_Energy', 'original_firstorder_Minimum',
        'original_firstorder_Maximum', 'original_firstorder_Range',
        
        # Shape
        'original_shape_VoxelVolume', 'original_shape_SurfaceArea',
        'original_shape_Sphericity', 'original_shape_Compactness1',
        'original_shape_Compactness2', 'original_shape_Elongation',
        'original_shape_Flatness', 'original_shape_Maximum3DDiameter',
        'original_shape_Roundness',
        
        # GLCM
        'original_glcm_Contrast', 'original_glcm_Correlation',
        'original_glcm_Energy', 'original_glcm_Homogeneity',
        'original_glcm_Entropy', 'original_glcm_Autocorrelation',
        'original_glcm_ClusterProminence', 'original_glcm_ClusterShade',
        
        # GLRLM
        'original_glrlm_GrayLevelNonUniformity', 'original_glrlm_RunLengthNonUniformity',
        'original_glrlm_RunPercentage', 'original_glrlm_LongRunEmphasis',
        'original_glrlm_ShortRunEmphasis', 'original_glrlm_LowGrayLevelRunEmphasis',
        
        # GLSZM
        'original_glszm_SizeZoneNonUniformity', 'original_glszm_ZonePercentage',
        'original_glszm_LargeAreaEmphasis', 'original_glszm_SmallAreaEmphasis',
        'original_glszm_GrayLevelNonUniformity'
    ]
    
    # Benign nodules
    benign_data = {}
    # Volume: ~100-500 mm³
    benign_data['original_shape_VoxelVolume'] = np.random.lognormal(5.5, 0.4, n_benign)
    # Sphericity: ~0.7-0.9 (round)
    benign_data['original_shape_Sphericity'] = np.random.beta(8, 2, n_benign)
    # Mean HU: ~20-80
    benign_data['original_firstorder_Mean'] = np.random.normal(50, 15, n_benign)
    # Entropy: ~3-4
    benign_data['original_firstorder_Entropy'] = np.random.normal(3.5, 0.4, n_benign)
    # Contrast: ~20-50
    benign_data['original_glcm_Contrast'] = np.random.lognormal(3.3, 0.3, n_benign)
    # Correlation: ~0.6-0.8
    benign_data['original_glcm_Correlation'] = np.random.beta(6, 3, n_benign)
    # Uniformity
    benign_data['original_glrlm_GrayLevelNonUniformity'] = np.random.lognormal(7.5, 0.3, n_benign)
    benign_data['original_glszm_SizeZoneNonUniformity'] = np.random.lognormal(7.5, 0.3, n_benign)
    
    # Fill remaining features
    for feat in feature_names:
        if feat not in benign_data:
            benign_data[feat] = np.random.normal(0, 1, n_benign)
    
    # Malignant nodules
    malignant_data = {}
    # Volume: ~300-1500 mm³ (larger)
    malignant_data['original_shape_VoxelVolume'] = np.random.lognormal(6.5, 0.5, n_malignant)
    # Sphericity: ~0.4-0.7 (irregular)
    malignant_data['original_shape_Sphericity'] = np.random.beta(4, 4, n_malignant)
    # Mean HU: ~40-120 (higher)
    malignant_data['original_firstorder_Mean'] = np.random.normal(80, 20, n_malignant)
    # Entropy: ~4-5.5 (more heterogeneous)
    malignant_data['original_firstorder_Entropy'] = np.random.normal(4.8, 0.5, n_malignant)
    # Contrast: ~40-100 (higher)
    malignant_data['original_glcm_Contrast'] = np.random.lognormal(4, 0.4, n_malignant)
    # Correlation: ~0.3-0.6 (lower)
    malignant_data['original_glcm_Correlation'] = np.random.beta(4, 4, n_malignant)
    # Less uniform
    malignant_data['original_glrlm_GrayLevelNonUniformity'] = np.random.lognormal(8.5, 0.4, n_malignant)
    malignant_data['original_glszm_SizeZoneNonUniformity'] = np.random.lognormal(8.5, 0.4, n_malignant)
    
    # Fill remaining features
    for feat in feature_names:
        if feat not in malignant_data:
            malignant_data[feat] = np.random.normal(0.5, 1.2, n_malignant)
    
    # Create DataFrames
    benign_df = pd.DataFrame(benign_data)
    benign_df['ID'] = [f'LungBenign_{i+1:03d}' for i in range(n_benign)]
    benign_df['Target'] = 0
    
    malignant_df = pd.DataFrame(malignant_data)
    malignant_df['ID'] = [f'LungMalignant_{i+1:03d}' for i in range(n_malignant)]
    malignant_df['Target'] = 1
    
    # Combine
    df = pd.concat([benign_df, malignant_df], ignore_index=True)
    
    # Reorder columns
    cols = ['ID', 'Target'] + sorted([c for c in df.columns if c not in ['ID', 'Target']])
    df = df[cols]
    
    # Save
    df.to_csv(output_path, index=False)
    
    print(f"✓ Created lung cancer dataset: {output_path}")
    print(f"  Benign nodules: {n_benign}")
    print(f"  Malignant nodules: {n_malignant}")
    print(f"  Total features: {len(feature_names)}")
    
    return df


if __name__ == "__main__":
    # Create default sample dataset
    create_radiomics_dataset(
        n_samples=100,
        n_features=50,
        output_path="radiomics_sample.csv"
    )
    
    # Create multiple datasets
    print("\n" + "="*60)
    create_multiple_datasets()
    
    # Create lung cancer specific dataset
    print("\n" + "="*60)
    create_lung_cancer_dataset()
