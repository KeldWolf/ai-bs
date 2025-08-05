import os
import sys
sys.path.append("..")
from config import *

def write_file(working_directory, file_path, content):
    try:
        working_dir = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(working_dir)
        if working_directory not in absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.exists(os.path.dirname(absolute_path)) == False:
            os.makedirs(os.path.dirname(absolute_path))
        with open(absolute_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: write file failed with the following exception."
    return f'Successfully wrote to "{absolute_path}" ({len(content)} characters written)'