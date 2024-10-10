# Introduction
This is a copy of Regularizing Visual Semantic Embedding with Contrastive Learning for Image-Text Matching, source code of [ConVSE](https://ieeexplore.ieee.org/abstract/document/9785732). This paper accepted by IEEE SPL. It is built on the top of the [VSE$\infty$](https://github.com/woodfrog/vse_infty/tree/bigru) in PyTorch.
# Requirements and Installation
Dependencies:
- Python3.6+
- Pytorch 1.9.0+

# Download data
Download the [dataset files](https://www.kaggle.com/datasets/kuanghueilee/scan-features).

# Train new models
Run `train.py`:
```
python3 train.py --data_path "$DATA_PATH" --data_name "$DATA_NAME" --vocab_path "$VOCAB_PATH" --model_name "runs/convse/model/" --use_contrastive
```

# Evaluate trained models 
```Python
from vocab import Vocabulary
import evalution
evalution.evalrank("$PATH/model_best.pth.tar", data_path="$DATA_PATH", split="test")
```
