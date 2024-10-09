#!/bin/bash
#SBATCH --container-image ghcr.io\#bouncmpe/cuda-python3
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G
#SBATCH --time=10000

# Activate Python virtual environment
source /opt/python3/venv/base/bin/activate

# Define environment variables
DATA_PATH="data/coco_precomp"  # Path to original dataset directory
OUTPUT_PATH="data/coco_precomp_small"  # Path to save subsampled dataset
NUM_SAMPLES=1000  # Number of samples to take from each dataset (e.g., train, dev, test)

# Run the downsampling script
cd /users/beyza.urhan/ConVSE-base
python3 subsample_data.py --input_dir "$DATA_PATH" --output_dir "$OUTPUT_PATH" --num_samples "$NUM_SAMPLES"
