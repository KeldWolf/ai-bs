import os
import sys
sys.path.append("..")
from config import *

def get_file_content(working_directory, file_path):
    working_dir = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(working_dir)
    try:
        if working_directory not in absolute_path:
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isfile(absolute_path) == False:
            return(f'Error: File not found or is not a regular file: "{file_path}"')
        
        with open(absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read()) > MAX_CHARS: 
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            else:
               return file_content_string
    except Exception as e:
        return(f"Error: file read failed with {e}")
    return file_content_string
    
    