from pathlib import Path


import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset


class MRNetDataser(Dataset):
    def __init__(self, data_dir, split, view, task):
        
    

