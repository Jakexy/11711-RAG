import json
import os

directory = 'data/parsed_data/papers'

for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)