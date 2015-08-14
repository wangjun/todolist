import base64, hashlib


def hash_password(password):
    """
    Hash the password.
    :param password: {str} The password.
    :return: {str}
    """
    return base64.b64encode(
        hashlib.sha384(password.encode('utf-8')).digest()
    ).decode('utf-8')
