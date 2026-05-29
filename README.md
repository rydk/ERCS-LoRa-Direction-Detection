# 📡 ERCS-Informed LoRa Signal Modeling for Corner-Aware Human Direction Detection

![MATLAB](https://img.shields.io/badge/MATLAB-R2021a%2B-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> This repository provides the simulation codes associated with our study on **LoRa-based human direction detection in corner environments**.
> 
> The released materials are intended to support result reproducibility and facilitate the understanding of the amplitude-based direction sensing mechanism discussed in our paper.

---

## 📂 Repository Structure

```text
.
├── amp_code.m      # MATLAB script for amplitude extraction and analysis
├── los_mc.py       # Monte Carlo simulation for LOS propagation
├── nlos_mc.py      # Monte Carlo simulation for NLOS corner propagation
└── README.md       # Project documentation

📊 Experimental Dataset
Due to the large size of the experimental datasets, the released partial datasets are provided through Baidu Netdisk.
These datasets are used to analyze direction-dependent amplitude variations in LoRa signals.
📥 ResourceLink / DetailsDownload Link🔗 Baidu NetdiskExtraction Codebhq8
Dataset Content
After extraction, you will find two folders:
🚶 left/ : LoRa signal data collected when the target was located on the left side of the corner region.
🚶 right/ : LoRa signal data collected when the target was located on the right side of the corner region.
🚀 Code & Usage
1. MATLAB Signal Processing Code
File: amp_code.m
This MATLAB script is designed to:
Read the collected signal data from the dataset.
Extract LoRa signal amplitudes.
Process amplitude sequences for left/right direction analysis.
Usage:
Open MATLAB and run the script. It can be directly applied to the datasets stored in the left and right folders.
Matlab

amp_code
💡 Note: The data path inside the script may need to be modified according to your local directory configuration.
2. Monte Carlo Simulation Codes
Files: los_mc.py & nlos_mc.py
Line-of-Sight (LOS) Analysis
Used to study the amplitude formation characteristics under LOS conditions.
Bash

python los_mc.py
Non-Line-of-Sight (NLOS) Analysis
Used to investigate the influence of reflection and scattering mechanisms on received signal amplitudes in corner environments.
Bash

python nlos_mc.py
📌 Notes
📝 Partial Data: The released datasets are partial samples from the comprehensive experiments reported in the paper.
🎓 Academic Use: This repository is strictly intended for academic research and result verification.
⚙️ Configuration: Additional preprocessing or parameter configuration may be required depending on your local runtime environment and hardware.
