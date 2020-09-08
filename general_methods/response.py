from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, \
    HTTP_405_METHOD_NOT_ALLOWED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_406_NOT_ACCEPTABLE, HTTP_403_FORBIDDEN
from general_methods.constants import *

"""
    Informational:            100 <= http status code <= 199 
    Success:                  200 <= http status code <= 299 
    Redirect:                 300 <= http status code <= 399 
    Client Error:             400 <= http status code <= 499 
    Server Error:             500 <= http status code <= 599  
"""


def bad_request(result):
    """
    :param result: any
    :return: dict

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 400
    """
    message = None
    if type(result) is not str:
        keys = list(dict(result).keys())
        if len(keys) > 0:
            try:
                message = '%s: ' % keys[0] + str(dict(result).get(keys[0])[0])
            except:
                result = result
    elif type(result) is str:
        message = result
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = result
    response[ERROR_MESSAGE_KEY_NAME] = message
    return Response(response, status=HTTP_400_BAD_REQUEST)


def success(result):
    """
    :param result: any
    :return: dict

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 200
    """
    response = dict()
    response[STATUS_KEY_NAME] = SUCCESS_STATUS_CODE
    response[RESULT_KEY_NAME] = result
    response[ERROR_MESSAGE_KEY_NAME] = SUCCESS_MESSAGE
    return Response(response, status=HTTP_200_OK)


def server_error(result=INTERNAL_SERVER_ERROR_CLIENT_MESSAGE):
    """
    :param result: str
    :return: dict

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: dict
    }

    Response code: 500
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = result
    return Response(response, status=HTTP_500_INTERNAL_SERVER_ERROR)


def no_data_found():
    """
    :return: dict

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 200
    """
    response = dict()
    response[STATUS_KEY_NAME] = SUCCESS_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = 'No Data Found'
    return Response(response, status=HTTP_200_OK)


def param_missing(key, message):
    """
    :param key:
    :param message:
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 400
    """
    response = dict()
    result = dict()
    errors = list()
    errors.append(message)
    result.update({
        key: errors
    })
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = result
    return Response(response, status=HTTP_400_BAD_REQUEST)


def unauthorized():
    """
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 401
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = 'Unauthorized'
    return Response(response, status=HTTP_401_UNAUTHORIZED)


def forbidden():
    """
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 403
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = 'Forbidden'
    return Response(response, status=HTTP_403_FORBIDDEN)


def method_not_allowed():
    """
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 405
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = 'Method Not Allowed'
    return Response(response, status=HTTP_405_METHOD_NOT_ALLOWED)


def not_acceptable():
    """
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: 406
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = 'Request Not Acceptable'
    return Response(response, status=HTTP_406_NOT_ACCEPTABLE)


def custom_error(status_code: int, result):
    """
    :param status_code:
    :param result:
    :return:

    Returns dictionary
    {
        status: boolean,
        message: str,
        result: any
    }

    Response code: status_code
    """
    response = dict()
    response[STATUS_KEY_NAME] = ERROR_STATUS_CODE
    response[RESULT_KEY_NAME] = dict()
    response[ERROR_MESSAGE_KEY_NAME] = result
    return Response(response, status=status_code)
