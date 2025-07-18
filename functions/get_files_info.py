import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."
    
    full_path = os.path.join(working_directory,directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    items = os.listdir(full_path)
    lines = []

    for item in items:
        item_path = os.path.join(full_path, item)
        is_directory = os.path.isdir(item_path)
        file_size = os.path.getsize(item_path)
        line = f"- {item}: file_size={file_size} bytes, is_dir={is_directory}"
        lines.append(line)

    return "\n".join(lines)
