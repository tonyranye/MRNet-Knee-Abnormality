# MRNet-Knee-Abnormality Detection

A computer vision project that classifies knee MRI exams for three conditions - General abnormality, ACL tear, and meniscus tear - using the [MRNet dataset](https://stanfordmlgroup.github.io/competitions/mrnet/) from
the Stanford ML Group.

Each Exam incudes three MRI views (axial, coronal, sagittal), each a variable length stack of 2D slices. A CNN backbone will process each slice, pooled across the stack per view, then combined into a a final prediction model per label.

## Project structure

```
data/                # local only, never committed (see .gitignore)
├── train/{axial,coronal,sagittal}/*.npy
├── valid/{axial,coronal,sagittal}/*.npy
└── {train,valid}_{abnormal,acl,meniscus}.csv

src/
├── dataset.py        # MRNetDataset — loads one view/task/split at a time
├── model.py           # CNN backbone + slice pooling + classifier heads
├── train.py            # training loop
└── eval.py              # AUC-ROC evaluation
```

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate   # Git Bash on Windows
pip install -r requirements.txt
```

Data must be downloaded separately (Stanford Research Use Agreement
required) and placed under `data/` — see `.gitignore`, it's never committed.

## Status

- [x] Environment + repo scaffold
- [x] Dataset loading (`MRNetDataset`)
- [ ] Model architecture
- [ ] Training loop
- [ ] Evaluation vs. published baseline
