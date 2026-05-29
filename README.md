# ERCS-Informed LoRa Signal Modeling for Corner-Aware Human Direction Detection

This repository provides the partial experimental datasets and simulation codes associated with our study on LoRa-based human direction detection in corner environments.

The released materials are intended to support result reproducibility and facilitate the understanding of the amplitude-based direction sensing mechanism discussed in the paper.

---

# Repository Structure

```text id="d6m0we"
.
├── data
│   ├── left
│   │   └── ...
│   ├── right
│   │   └── ...
│
├── amp_code.m
├── los_mc.py
├── nlos_mc.py
└── README.md
```

---

# Dataset Description

The `data` directory contains partial experimental datasets collected in corner scenarios.

## `data/left`

Contains LoRa signal data collected when the target was located on the left side of the corner region.

## `data/right`

Contains LoRa signal data collected when the target was located on the right side of the corner region.

These datasets are used to analyze direction-dependent amplitude variations in LoRa signals.

---

# MATLAB Signal Processing Code

## `amp_code.m`

This MATLAB script is used to:

* Read the collected signal data
* Extract LoRa signal amplitudes
* Process amplitude sequences for left/right direction analysis

The code can be directly applied to the datasets stored in the `left` and `right` folders.

## Usage

Open MATLAB and run:

```matlab id="c62vcr"
amp_code
```

The data path may need to be modified according to the local directory configuration.

---

# Monte Carlo Simulation Codes

## `los_mc.py`

Monte Carlo simulation code for LOS (Line-of-Sight) propagation analysis.

This script is mainly used to study the amplitude formation characteristics under LOS conditions.

Run:

```bash id="2s9ey6"
python los_mc.py
```

---

## `nlos_mc.py`

Monte Carlo simulation code for NLOS (Non-Line-of-Sight) corner propagation analysis.

This script is used to investigate the influence of reflection and scattering mechanisms on received signal amplitudes in corner environments.

Run:

```bash id="v1i1jk"
python nlos_mc.py
```

---

# Notes

* The released datasets are partial samples from the experiments reported in the paper.
* The repository is intended for academic research and result verification.
* Additional preprocessing or parameter configuration may be required depending on the local runtime environment.
