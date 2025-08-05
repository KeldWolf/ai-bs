import os
import sys
import subprocess
sys.path.append("..")
from config import *

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_dir = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(working_dir)
        if working_directory not in absolute_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(absolute_path) == False:
            return f'Error: File "{file_path}" not found.'
        if file_path[-2:].lower() != "py":
            return f'Error: "{file_path}" is not a Python file.'
        command = absolute_path
        my_args = ""
        for arg in args:
            my_args += f'{arg} '
        print(my_args)
        if my_args == "":
            run_results = subprocess.run(["uv", "run", absolute_path], capture_output=True, timeout=30, cwd=working_directory)
        else:
            run_results = subprocess.run(["uv", "run", absolute_path, my_args], capture_output=True, timeout=30, cwd=working_directory)
        #if not run_results.stdout:
        #    return "No output produced"
        #print(run_results.stdout)
        #print("STDOUT: " + run_results.stdout)
        standard_out = f'STDOUT: {run_results.stdout}'
        standard_error = f'STDERR: {run_results.stderr}'
        output = f'{standard_out}\n{standard_error}'
        return output
    except Exception as e:
        return f"Error: process failed due to the following exception: {e}"
