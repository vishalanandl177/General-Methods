from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, \
    HTTP_500_INTERNAL_SERVER_ERROR
from general_methods.constants import *


class ServerException(APIException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_code = INTERNAL_SERVER_ERROR

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: {},
            ERROR_MESSAGE_KEY_NAME: INTERNAL_SERVER_ERROR
        }


class UnauthorizedException(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_code = UNAUTHORIZED

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: {},
            ERROR_MESSAGE_KEY_NAME: UNAUTHORIZED
        }


class SessionExpiredException(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_code = UNAUTHORIZED

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: {},
            ERROR_MESSAGE_KEY_NAME: SESSION_EXPIRED
        }


class MissingHeaderException(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_code = BAD_REQUEST

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: INSUFFICIENT_HEADERS,
            ERROR_MESSAGE_KEY_NAME: {}
        }


class BlockedClientException(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_code = UNAUTHORIZED

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: {},
            ERROR_MESSAGE_KEY_NAME: BLOCKED_CLIENT_MESSAGE
        }


class AuthenticationFailedException(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_code = UNAUTHORIZED

    def __init__(self):
        self.detail = {
            STATUS_KEY_NAME: ERROR_STATUS_CODE,
            RESULT_KEY_NAME: {},
            ERROR_MESSAGE_KEY_NAME: INVALID_AUTHORIZATION_HEADER
        }
