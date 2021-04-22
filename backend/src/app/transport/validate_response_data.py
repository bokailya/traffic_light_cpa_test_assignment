"""
Function for response data validation
"""

from typing import Any

from app.transport.errors import InternalServerError


def validate_response_data(response_data: dict[str, Any], serializer: Any) -> dict[str, Any]:
    """
    Response data validation
    :param response_data: Response data for validation
    :param serializer: Validator class
    :return: Validated response data
    :raises: InternalServerError
    """
    ser = serializer(data=response_data)
    if not ser.is_valid():
        raise InternalServerError(str(ser.errors))

    return ser.validated_data
