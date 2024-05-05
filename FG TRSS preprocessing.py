import os
import pydicom as dic
import pandas as pd
import numpy as np

data_dir = "./data/2021_FG_RTSS/"
dcm_files = [f for f in os.listdir(data_dir) if f.endswith(".dcm")]

preprocessed_data = []

for file in dcm_files:
  # Full path to the DICOM file
  dcm_path = os.path.join(data_dir, file)

  # Load the DICOM file
  ds = dic.dcmread(dcm_path)

  # Extract features
  

  # Additional preprocessing steps (e.g., normalization, rescaling)
  # TO DO: add specific preprocessing steps here

  # Preprocess the data
  #preprocessed_data.append(hu_values)  # Append preprocessed data to the list