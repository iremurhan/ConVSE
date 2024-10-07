#!/bin/bash
#SBATCH --container-image ghcr.io\#bouncmpe/cuda-python3
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G
#SBATCH --time=10000

source /opt/python3/venv/base/bin/activate
python3 train.py --data_path "$DATA_PATH" --data_name "$DATA_NAME" --vocab_paath "$VOCAB_PATH" --model_name "runs/convse/model/" --use_contrastive