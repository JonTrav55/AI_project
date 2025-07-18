from .config import MAX_CHARS
import os

def get_file_content(working_directory, file_path):

    full_path_to_file_on_disk = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path_to_file_on_disk)
    abs_working_directory = os.path.abspath(working_directory)
    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path_to_file_on_disk):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    
    try:
        with open(full_path_to_file_on_disk, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: {e}"

        
