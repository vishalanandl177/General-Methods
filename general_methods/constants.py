UNAUTHORIZED = 'Unauthorized'
FORBIDDEN = 'Forbidden'
CUSTOMER_NOT_FOUND = 'Customer not found'
SESSION_EXPIRED = 'Session Expired'
NOT_ACCEPTABLE = 'Not Acceptable'
UNSUPPORTED_DEVICE_TYPE = 'Unsupported Device Type'
BAD_REQUEST = 'Bad Request'
INTERNAL_SERVER_ERROR = 'Internal Server Error'
INTERNAL_SERVER_ERROR_CLIENT_MESSAGE = 'A server error occurred.'
INSUFFICIENT_PARAM = 'Required params missing or incorrect'
INSUFFICIENT_HEADERS = 'Required headers missing or incorrect'
BLOCKED_CLIENT_MESSAGE = 'The network administrator has prevented you from using the network.'
INVALID_AUTHORIZATION_HEADER = 'Invalid token header. No credentials provided.'


"""
    The code to sent as a part of response to web users and app users.
    If error occurs, ERROR_STATUS_CODE is responsible for identification of error status code.
    If success, SUCCESS_STATUS_CODE is responsible for identification of success status code.
"""

STATUS_KEY_NAME = 'status'
ERROR_STATUS_CODE = False
ERROR_MESSAGE = 'error'

ERROR_MESSAGE_KEY_NAME = 'message'

ERROR_KEY_NAME = 'errors'

RESULT_KEY_NAME = 'result'
SUCCESS_STATUS_CODE = True
SUCCESS_MESSAGE = 'success'
