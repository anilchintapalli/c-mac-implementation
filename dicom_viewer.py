import pydicom as dicom
import matplotlib.pyplot as plt
import os

def view_dicom(patient, img_idx):
    """Opens and shows a single DICOM file."""
    file_path = f'/Users/riyamurugesan/Desktop/cocacoronarycalciumandchestcts-2/Gated_release_final/patient/{patient}/Pro_Gated_CS_3.0_I30f_3_70%'
    all_files = os.listdir(file_path)
    all_files = sorted(all_files)
    img_string = f"{all_files[img_idx]}"

    updated_path = f'/Users/riyamurugesan/Desktop/cocacoronarycalciumandchestcts-2/Gated_release_final/patient/{patient}/Pro_Gated_CS_3.0_I30f_3_70%/{img_string}'

    ds = dicom.dcmread(updated_path)
    image_array = ds.pixel_array
    
    plt.imshow(image_array, cmap='gray')
    plt.title(f"DICOM Image for Patient No. {patient}")
    plt.show()
