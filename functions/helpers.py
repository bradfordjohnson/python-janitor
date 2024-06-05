import re


def normalize_string(s):
    cleaned = re.sub(r"[^\w\s]", "", s.lower())

    cleaned = re.sub(r"([a-zA-Z])(\d)", r"\1_\2", cleaned)
    cleaned = re.sub(r"(\d)([a-zA-Z])", r"\1_\2", cleaned)

    result = re.sub(r"\s+|_{2,}", "_", cleaned)

    return result
