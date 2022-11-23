import os
import random
import string


def get_random_name(size=10):
    """Generate random string

    Args:
        size (int, optional): String length. Defaults to 10.

    Returns:
        string: Random string
    """
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(size)
    )


def create_writable_directory(dir_name):
    """Create writable directory to prepare render/temporary saves folder

    Args:
        dir_name (string): Folder path, relative or absolute
    """
    umask = os.umask(0o000)
    os.mkdir(dir_name, 0o766)
    os.umask(umask)

def init_render_folder(dirname):
    """Create the default render folder - Called on app init

    Args:
        dirname (string): Folder path, relative or absolute
    """
    if not os.path.exists(dirname):
        create_writable_directory(dirname)
