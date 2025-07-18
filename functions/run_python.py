import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_file_path = os.path.join(working_directory,file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.realpath(full_file_path)
    

    if not abs_file_path.startswith(abs_working_directory + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    base_command = ['python3', abs_file_path, *args]


    try:
        
        completed_process = subprocess.run(
                base_command,
                timeout=30,
                capture_output=True,
                cwd=abs_working_directory
                )

        result_string = ''

        if completed_process.stdout:
            decoded_stdout = completed_process.stdout.decode('utf-8')
            result_string += f"STDOUT:\n{decoded_stdout}\n"


        if completed_process.stderr:
            decoded_stderr = completed_process.stderr.decode('utf-8')
            result_string += f"STDERR:\n{decoded_stderr}\n"


        if completed_process.returncode != 0:
            result_string += f"Process exited with code {completed_process.returncode}"

        if result_string == "":
            return 'No output produced.'


        return result_string

    except Exception as e:
        return f'Error: executing Python file: {e}'
