"""
HTTP handler for getting department tree
"""

from http import HTTPStatus

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from rest_framework.fields import JSONField, DictField, CharField
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from app.services.get_department_tree import get_department_tree
from app.transport.errors import ErrorSchema
from app.transport.validate_response_data import validate_response_data


class GetDepartmentTreeResponse(Serializer):  # pylint: disable=abstract-method
    """
    Class for validation get department tree method response
    """
    departments = JSONField(label='Departments tree')
    departmentIDToName = DictField(
        label='Mapping from department identifier to department name',
        child=CharField(max_length=128),
    )


class GetDepartmentTree(APIView):
    """
    View for getting department tree
    """

    @staticmethod
    @swagger_auto_schema(
        responses={
            HTTPStatus.INTERNAL_SERVER_ERROR.value: ErrorSchema,
            HTTPStatus.OK.value: GetDepartmentTreeResponse,
        },
        operation_summary='Get tree',
        operation_description=(
                'Getting departments tree with names and identifiers'
        ),
    )
    def get(_: Request) -> JsonResponse:
        """
        Handler for getting department tree
        """

        return JsonResponse(
            data=validate_response_data(
                response_data=get_department_tree().dict(by_alias=True),
                serializer=GetDepartmentTreeResponse,
            ),
        )
