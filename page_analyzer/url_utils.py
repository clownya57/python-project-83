from urllib.parse import urlparse

import validators

MAX_URL_LENGTH = 255
ALLOWED_SCHEMES = {"http", "https"}


def is_valid_url(value):
    if not value:
        return False

    if len(value) > MAX_URL_LENGTH:
        return False

    parsed_url = urlparse(value)

    if parsed_url.scheme not in ALLOWED_SCHEMES:
        return False

    if not parsed_url.netloc:
        return False

    return bool(validators.url(value))


def normalize_url(value):
    parsed_url = urlparse(value)

    return f"{parsed_url.scheme}://{parsed_url.netloc}"
