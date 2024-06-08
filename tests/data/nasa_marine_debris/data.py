#!/usr/bin/env python3

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

import numpy as np
from PIL import Image

DTYPE = np.float32
SIZE = 2

np.random.seed(0)

all_debris_types = (
    'type1',  # Placeholder for actual debris types
    'type2',
    'type3',
)

for sample in range(1):  # Assume one sample for simplicity
    directory = os.path.join('data', str(sample))
    os.makedirs(directory, exist_ok=True)

    # Simulate saving a random image for each debris type
    for debris_type in all_debris_types:
        arr = np.random.rand(SIZE, SIZE).astype(DTYPE) * np.finfo(DTYPE).max
        img = Image.fromarray(arr)
        img.save(os.path.join(directory, f'{sample}_{debris_type}.tif'))