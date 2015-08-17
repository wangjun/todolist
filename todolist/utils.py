import base64, hashlib
from datetime import datetime


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
def parse_ios_format(iso_format):
    """
    :param iso_format: {str} The iso format datetime. "yyyy-MM-ddTHH:mm:ss.ssssssZ"
    :return: {datetime}
    """
    if not iso_format:
        return None
    try:
        return datetime.strptime(iso_format, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        try:
            return datetime.strptime(iso_format, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return None

def int_filter(value):
    """
    The int filter for wtforms.
    """
    try:
        return int(value)
    except:
        return 0
