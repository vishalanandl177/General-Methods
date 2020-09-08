import json
import re
import os
import binascii
import hashlib
import base64
import uuid
from django.conf import settings


def get_headers(request):
    """
    :param request: request
    :return: dict:

    To get all the headers from request as dictionary
    """
    regex = re.compile('^HTTP_')
    return dict((regex.sub('', header), value) for (header, value)
                in request.META.items() if header.startswith('HTTP_'))


def get_client_ip_address(request):
    """
    :param request: request
    :return: Client IP Address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def generate_token(length: int = 20):
    """
    :param length: int
    :return: str

    To generate random alpha-numeric string.
    Default string length is 20.
    """
    return binascii.hexlify(os.urandom(length)).decode()


def get_uuid():
    """
    :return: UUID string
    """
    return uuid.uuid4()


'''
Hash algorithms.
The available algorithms are : 'sha256', 'sha384', 'sha224', 'sha512', 'sha1', 'md5'
'''


def sha1(token: str):
    return hashlib.sha1(token.encode()).hexdigest()


def sha224(token: str):
    return hashlib.sha224(token.encode()).hexdigest()


def sha256(token: str):
    return hashlib.sha256(token.encode()).hexdigest()


def sha384(token: str):
    return hashlib.sha384(token.encode()).hexdigest()


def sha512(token: str):
    return hashlib.sha512(token.encode()).hexdigest()


def md5(token: str):
    return hashlib.md5(token.encode()).hexdigest()


def encode(text: str):
    """
    :param text: str
    :return: encoded string
    """
    secret_key = settings.SECRET_KEY
    enc = []
    for i in range(len(text)):
        key_c = secret_key[i % len(secret_key)]
        enc_c = (ord(text[i]) + ord(key_c)) % 256
        enc.append(enc_c)
    return base64.urlsafe_b64encode(bytes(enc)).decode('utf-8')


def decode(text: str):
    """
    :param text: str
    :return: decoded string
    """
    secret_key = settings.SECRET_KEY
    dec = []
    enc = base64.urlsafe_b64decode(text)
    for i in range(len(enc)):
        key_c = secret_key[i % len(secret_key)]
        dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def is_valid_json(data):
    """
    :param data: string data
    :return: boolean
    If valid, returning True else False
    """
    try:
        json.loads(data)
        return True
    except:
        return False


def is_valid_email(email: str):
    """
    :param email: str
    :return: boolean
    Identify the string is email id or not.
    If valid, returning True else False
    """
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
        return False
    return True
