# General-Methods
![version](https://img.shields.io/badge/version-0.0.2-blue.svg)

A general utility for your Django Rest Framework project.

## Installation

Install or add general-methods.
```
pip install general-methods
```

## Utils functions
Import utils.
```
from general_methods import utils
```
### Get Headers
To get headers (Dictionary type) from request.

```
headers = utils.get_headers(request)
```

### Get Client IP Address
To get client IP Address.

```
client_ip_address = utils.get_client_ip_address(request)
```

### Generate Random Token
To generate random alpha-numeric string. Default string length is 20.

```
token = utils.generate_token()  // Default token length is 20 characters.
```
```
token = utils.generate_token(length=50)  // Token length is 50 characters.
```

### Get UUID
To get UUID string.

```
uuid = utils.get_uuid()
```

### Hash algorithms.
The available algorithms are : 'sha256', 'sha384', 'sha224', 'sha512', 'sha1', 'md5'
##### SHA1
```
hashed_string = utils.sha1('string_to_hash')
```
##### SHA224
```
hashed_string = utils.sha224('string_to_hash')
```
##### SHA256
```
hashed_string = utils.sha256('string_to_hash')
```
##### SHA384
```
hashed_string = utils.sha384('string_to_hash')
```
##### SHA512
```
hashed_string = utils.sha512('string_to_hash')
```
##### MD5
```
hashed_string = utils.md5('string_to_hash')
```
### Encode String Data
To encode string data using django SECRET_KEY (available in settings.py file) as key to encode.

Note: If you changed the secret key of you django application then decode won't be able to decode the sting back. Use only in run time use-cases for example encode user id before sending in to client side so client will never get to know the actual user id.
```
encoded_data = utils.encode('MY_DATA_TO_ENCODE')
```
### Decode String Data
To decode string data using django SECRET_KEY (available in settings.py file) as key to decode.
```
decoded_data = utils.decode('MY_DATA_TO_DECODE')
```

### Is Valid JSON
To identify JSON data is valid or not. If valid, returns True else False.

```
is_valid_json = utils.is_valid_json({'key': 'value'})
```
### Is Valid EMAIL ID
To identify email is valid or not. If valid, returns True else False.

```
is_valid_email = utils.is_valid_email('abc@mail.com')
```
## Response functions
Note: Returns application/json response.

Import response.
```
from general_methods import response
```

### Success Response 200
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 200

Function:
response.success('Any Type of Data')

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.success('Any Type of Data')  // returning response to client.
```
### Bad Request 400
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 400

Function:
response.bad_request('Username is required.')

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.bad_request('Username is required.')  // returning response to client.
```
### Server Error 500
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 500

Function:
response.server_error('Optional Message')

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.server_error()  // returning response to client.
```
### No Data Found 200
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 200

Function:
response.no_data_found()

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.no_data_found()  // returning response to client.
```
### Parameter Missing 400
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 400

Function:
response.param_missing(key, message)

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.param_missing('username', 'This field is required.')  // returning response to client.
```
### Unauthorized 401
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 401

Function:
response.unauthorized()

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.unauthorized()  // returning response to client.
```
### Forbidden 403
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 403

Function:
response.forbidden()

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.forbidden()  // returning response to client.
```
### Method Not Allowed 405
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 405

Function:
response.method_not_allowed()

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.method_not_allowed()  // returning response to client.
```
### Not Acceptable 406
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 406

Function:
response.not_acceptable()

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.not_acceptable()  // returning response to client.
```
### Custom Error
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: User Specified

Function:
response.custom_error(status_code: int, result)

```
class MyView(APIView):
    def get(self, request, *args, **kwargs):
        return response.custom_error(status_code=200, result='Login Successful.')  // returning response to client.
```

## Exception functions
Note: Returns application/json response. Can be used in API exceptions. for example in API authorization or permission classes.

Import exceptions.
```
from general_methods import exceptions
```
### Server Exception 500
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 500
```
raise exceptions.ServerException()
```
### Unauthorized Exception 401
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 401
```
raise exceptions.UnauthorizedException()
```
### Session Expired Exception 401
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 401
```
raise exceptions.SessionExpiredException()
```

### Missing Header Exception 400
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 400
```
raise exceptions.MissingHeaderException()
```

### Blocked Client Exception 401
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 401
```
raise exceptions.BlockedClientException()
```

### Authentication Failed Exception 401
Returns dictionary
{
    status: boolean,
    message: str,
    result: any
}

Response code: 401
```
raise exceptions.AuthenticationFailedException()
```

## Validators functions
Can be used in defining Models.

Import validators.
```
from general_methods import validators
```
### Email Validator
Function: email_validator
```
class MyModel(models.Model):
    email = models.CharField(max_length=100, validators=[validators.email_validator])
```
### Mobile Number Validator (10 Length)
Function: mobile_number_validator
```
class MyModel(models.Model):
    mobile = models.CharField(max_length=15, validators=[validators.mobile_number_validator])
```
### Country Code Validator (Example: +91, +1 etc.)
Function: country_code_validator
```
class MyModel(models.Model):
    mobile = models.CharField(max_length=15, validators=[validators.country_code_validator])
```
### String with Space Validator [ a-zA-Z]
Function: string_with_space_validator
```
class MyModel(models.Model):
    mobile = models.CharField(max_length=15, validators=[validators.string_with_space_validator])
```
## Country Codes
All country codes are available.

Array of Objects like:

{
    'country_code': "IN",
    'calling_code': "+91",
    'name': 'India (+91)'
}

Import country_codes.
```
from general_methods import country_codes
```
