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

def get_iso_format(date_time):
    """
    :param date_time: {datetime} The datetime.
    :return: {str} The iso format datetime "yyyy-MM-ddTHH:mm:ss.ssssssZ"
    """
    if not date_time:
        return None
    return date_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

def int_filter(value):
    """
    The int filter for wtforms.
    """
    try:
        return int(value)
    except:
        return 0
