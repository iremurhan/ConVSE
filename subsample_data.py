import numpy as np
import os
import shutil

def subsample_data(input_dir, output_dir, num_samples=1000):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List of data files to subsample
    # beyza.urhan@ultramarine:~/ConVSE-base/data/coco_precomp$ ls
        # dev_caps.txt  testall_caps.txt  test_caps.txt  train_caps.txt
        # dev_ids.txt   testall_ids.txt   test_ids.txt   train_ids.txt
        # dev_ims.npy   testall_ims.npy   test_ims.npy   train_ims.npy
    data_files = [
        ('train_caps.txt', 'train_caps_subsampled.txt'),
        ('train_ids.txt', 'train_ids_subsampled.txt'),
        ('train_ims.npy', 'train_ims_subsampled.npy'),
        ('dev_caps.txt', 'dev_caps_subsampled.txt'),
        ('dev_ids.txt', 'dev_ids_subsampled.txt'),
        ('dev_ims.npy', 'dev_ims_subsampled.npy'),
        ('test_caps.txt', 'test_caps_subsampled.txt'),
        ('test_ids.txt', 'test_ids_subsampled.txt'),
        ('test_ims.npy', 'test_ims_subsampled.npy'),
    ]

    for input_file, output_file in data_files:
        input_path = os.path.join(input_dir, input_file)
        output_path = os.path.join(output_dir, output_file)

        if input_file.endswith('.npy'):
            # Subsampling for numpy files
            data = np.load(input_path)
            subsampled_data = data[:num_samples]
            np.save(output_path, subsampled_data)
        elif input_file.endswith('.txt'):
            # Subsampling for text files (captions or IDs)
            with open(input_path, 'r') as f:
                lines = f.readlines()
                subsampled_lines = lines[:num_samples]

            with open(output_path, 'w') as f:
                f.writelines(subsampled_lines)

    print(f"Subsampling completed. Data saved to {output_dir}")

if __name__ == "__main__":
    input_directory = 'data/coco_precomp'  # Original data directory
    output_directory = 'data/coco_precomp_small'  # Directory to save subsampled data
    num_samples = 1000  # Number of samples to take from the original dataset

    subsample_data(input_directory, output_directory, num_samples)