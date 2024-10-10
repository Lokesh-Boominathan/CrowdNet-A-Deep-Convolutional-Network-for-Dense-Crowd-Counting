#!/usr/bin/env python

import scipy.io
import json
import os
import glob

# Set the input/output path
dataset_path = 'dataset/UCF_CC_50'

# Find all annotation files with '_ann.mat' extension
annotation_files = glob.glob(os.path.join(dataset_path, '*_ann.mat'))

# Process each annotation file
for annotation_file in annotation_files:
    # Load the .mat file and extract the annotation points
    annotation_data = scipy.io.loadmat(annotation_file)['annPoints']
    
    # Convert the points to a list of dictionaries with 'x' and 'y' coordinates
    json_data = [{'x': pt[0], 'y': pt[1]} for pt in annotation_data]
    
    # Set the output JSON file name by replacing the '_ann.mat' extension
    output_json_file = annotation_file.replace('_ann.mat', '.json')
    
    # Write the data to the JSON file
    with open(output_json_file, 'w') as out_file:
        json.dump(json_data, out_file)
        print(f'{annotation_file} -> {output_json_file}')