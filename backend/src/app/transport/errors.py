"""
All HTTP errors used in application
"""

from http import HTTPStatus

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING  # type: ignore
from rest_framework.exceptions import APIException


class BadRequest(APIException):
    """
    Request Validation Error
    """
    default_detail = 'Bad Request'
    status_code = HTTPStatus.BAD_REQUEST


class InternalServerError(APIException):
    """
    Any server side error
    """
    default_detail = 'Internal Server Error'
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR


ErrorSchema = Schema(
    title='Generic API Error',
    type=TYPE_OBJECT,
    properties={
        'errors': Schema(
            type=TYPE_OBJECT,
            properties={
                'detail': Schema(
                    type=TYPE_STRING,
                    description='Error details',
                ),
                'code': Schema(type=TYPE_STRING, description='Error code'),
            },
        ),
      },
    required=['detail'],
)
