import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    working_dir = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(working_dir)
    if working_directory not in absolute_path:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if os.path.isdir(absolute_path) == False:
        return(f'Error: "{directory}" is not a directory')
    dir_contents = os.listdir(absolute_path)
    return dir_string_builder(absolute_path, dir_contents)

def dir_string_builder(absolute_path, dir_list):
    dir_string = ""
    for item in dir_list:
        try:
            file_size = os.path.getsize(os.path.join(absolute_path, item))
            is_dir = os.path.isdir(os.path.join(absolute_path, item))
            dir_string += f" - {item}: file_size={file_size} bytes, is_dir={is_dir}\n"
        except Exception as e:
            return(f'Error: operation failed with {e}')
    return dir_string

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)