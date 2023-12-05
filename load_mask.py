import numpy as np
import os

# Directory where the .npy mask files are stored
directory = './result/mask/output_video'

# List to store the individual mask arrays
masks = []

# Iterate through each file in the directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.npy'):
        file_path = os.path.join(directory, filename)
        
        # Load the .npy file as a NumPy array and append to the list
        mask = np.load(file_path)
        masks.append(mask)

# Convert the list of 2D arrays to a single 3D array
masks_3d = np.stack(masks, axis=0)

# Print out the 3D array
print("3D Mask Array Shape:", masks_3d.shape)
print(masks_3d)

# Counting the masks that contain '1'
count_masks_with_ones = np.sum([np.any(mask == 1) for mask in masks_3d])

print(f"Number of masks containing '1': {count_masks_with_ones}")
