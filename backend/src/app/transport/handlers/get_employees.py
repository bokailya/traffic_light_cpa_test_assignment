"""
HTTP Handler for getting page of department employees
"""
from http import HTTPStatus

from django.http import JsonResponse, QueryDict
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from rest_framework.fields import (
    UUIDField,
    IntegerField,
    DateField,
    CharField,
    DecimalField,
    ListField,
    BooleanField,
)
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from app.services.get_department_employees import get_department_employees
from app.transport.errors import BadRequest, ErrorSchema
from app.transport.validate_response_data import validate_response_data


class Employee(Serializer):  # pylint: disable=abstract-method
    """
    Class for validation employee in response
    """
    employmentDate = DateField(label='Date of employment')
    fullName = CharField(label='Employee full name', max_length=255)
    position = CharField(label='Employee position', max_length=255)
    salary = DecimalField(decimal_places=2, label='Employee salary', max_digits=20)


class GetDepartmentEmployeesRequest(Serializer):  # pylint: disable=abstract-method
    """
    Class for validation get department employees request
    """
    departmentID = UUIDField(label='Department identifier', required=True)
    pageNumber = IntegerField(label='Page number', required=True)


class GetDepartmentEmployeesResponse(Serializer):  # pylint: disable=abstract-method
    """
    Class for validation get department employees response
    """
    employees = ListField(child=Employee(), label='Page of employees')
    hasNextPage = BooleanField(label='True if and only if page has next')


class GetDepartmentEmployees(APIView):
    """
    View for getting department employees page
    """

    @staticmethod
    @swagger_auto_schema(
        query_serializer=GetDepartmentEmployeesRequest,
        response={
            HTTPStatus.BAD_REQUEST.value: ErrorSchema,
            HTTPStatus.INTERNAL_SERVER_ERROR.value: ErrorSchema,
            HTTPStatus.OK.value: GetDepartmentEmployeesResponse,
        },
        operation_summary='Get employees',
        operation_description='Get department employees page',
    )
    def get(request: Request) -> JsonResponse:
        """
        Handler for getting department employees page
        """

        request_data: QueryDict = request.query_params

        request_ser: GetDepartmentEmployeesRequest = (
            GetDepartmentEmployeesRequest(data=request_data)
        )
        if not request_ser.is_valid():
            raise BadRequest(detail=str(request_ser.errors))

        return JsonResponse(
            data=validate_response_data(
                response_data=get_department_employees(
                    department_id=request_ser.validated_data['departmentID'],
                    page_number=request_ser.validated_data['pageNumber'],
                ).dict(by_alias=True),
                serializer=GetDepartmentEmployeesResponse,
            ),
        )
