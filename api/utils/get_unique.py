import hashlib


def get_unique_value(*args: list[str]):
    args = list(map(str, args))
    args = sorted(args)
    unique = hashlib.md5("".join(args).encode()).hexdigest()
    return unique
