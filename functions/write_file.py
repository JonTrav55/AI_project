import os

def write_file(working_directory, file_path, content):

    full_file_path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(full_file_path)
    file_dir = os.path.dirname(abs_file_path)

    if not (abs_file_path.startswith(abs_working_dir + os.sep) or abs_file_path == abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir, exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
       return(f'Error: {e}')
