from pathlib import Path
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path = os.path.expanduser(path)
    if not os.path.isdir(path):
        return "This doesn't appear to be a valid path"

    results = []
    dir_list = os.listdir(path)
  

    for subpath in Path(path).rglob('*.c'):
        results.append(os.path.join(path, subpath))
    return results