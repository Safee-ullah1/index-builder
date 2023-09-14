import os
import json

def create_index(directory, output):
    if not os.path.isdir(directory):
        raise Exception("Directory not found.")
    
    files = os.listdir(directory)
    print(files)
    index = {}
    for file in files:
        full_path = os.path.join(directory, file)
        if not os.path.isfile(full_path):
            continue
        with open(full_path, "r", encoding="utf-8") as input_file:
            file_text = input_file.read()
            words = file_text.split(" ")
            for word in words:
                if word not in index:
                    index[word] = []
                index[word].append(file)
                
    with open(output, "w+", encoding="utf-8") as output_file:
        output_file.write(json.dumps(index, sort_keys=True, indent=4))
    return index