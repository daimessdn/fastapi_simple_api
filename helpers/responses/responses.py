from fastapi import status


class Response(Exception):
    def __init__(self, success, status_code, message, data=None):
        self.success = success
        self.status_code = status_code
        self.message = message

        print(data)

        if data is not None:
            self.data = data


# success responses
def get_success_response(message, data=None):
    return Response(True, status.HTTP_200_OK, message, data)


def get_success_created_response(message, data=None):
    return Response(True, status.HTTP_201_CREATED, message, data)


# error responses
def get_error_bad_request_response(message):
    return Response(False, status.HTTP_400_BAD_REQUEST, message, None)


def get_error_not_authorized_response(message):
    return Response(False, status.HTTP_401_UNAUTHORIZED, message, None)


def get_error_forbidden_response(message):
    return Response(False, status.HTTP_403_FORBIDDEN, message, None)


def get_error_not_found_response(message):
    return Response(False, status.HTTP_404_NOT_FOUND, message, None)
