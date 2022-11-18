import random
import string


def get_random_name(size=10):
    """Generate random string

    Args:
        size (int, optional): String length. Defaults to 10.

    Returns:
        string: Random string
    """
    return "".join(random.choice(string.ascii_lowercase) for i in range(size))
