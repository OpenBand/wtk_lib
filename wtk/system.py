import os


def get_bool_environ(env_name: str):
    r = os.environ.get(env_name)
    if not r or r.lower() == 'false':
        return False
    for val_char in r:
        if val_char != '0':
            return True
    return False