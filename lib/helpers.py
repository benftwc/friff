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
    umask = os.umask(0o000)
    os.mkdir(dir_name, 0o766)
    os.umask(umask)
