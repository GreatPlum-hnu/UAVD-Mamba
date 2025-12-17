# UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection
<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv%20paper-2404.17360-b31b1b.svg)](https://arxiv.org/abs/2507.00849)&nbsp;

</div>
1. The core of Deformable Token
![teaser](assets/AdaptivePatch.png)

2. The overview of UAVD-Mamba
![teaser](assets/Overview.png)

3. UAVD-Mamba detection neck
![teaser](assets/DetectionNeck.png)

4. Detection results on DroneVehicle dataset
![teaser](assets/Results.png)

This repository contains the code for the paper [UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection](https://ieeexplore.ieee.org/document/11097442).
>  - [2025 IEEE Intelligent Vehicles Symposium (IV) Paper](https://ieeexplore.ieee.org/abstract/document/11097569), IEEE IV 2025 

## Setup
1. Clone the repository:
  ```bash
  git clone https://github.com/GreatPlum-hnu/UAVD-Mamba.git
  ```

2. Create and activate the Conda environment:
  ```bash
  conda env create -f environment.yml
  ```

3. Navigate to the `ultralytics/Vim/` directory:
  ```bash
  cd ultralytics/Vim/
  ```

  - Install requirements from `vim_requirements.txt`:
    ```bash
    pip install -r vim/vim_requirements.txt
    ```

  - Install `causal_conv1d` and `mamba`:
    ```bash
    pip install -e causal_conv1d>=1.1.0
    pip install -e mamba-1p1p1
    ```

4. Train the model:
  ```bash
  python train.py
  ```

5. Validate the model:
  ```bash
  python val.py
  ```


This project is based on  
1.https://github.com/ultralytics/ultralytics.git
2.https://github.com/hustvl/Vim.git
3.https://github.com/PSRben/FusionMamba.git
4.https://github.com/yjh0410/PyTorch_DCNv2.git
Thanks for their wonderful works.