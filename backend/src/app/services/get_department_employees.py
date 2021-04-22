"""
Get page of department employees
"""

from datetime import date
from decimal import Decimal

from django.core.paginator import Paginator, Page
from pydantic import BaseModel, Field

from app.models import Employee


PAGE_SIZE: int = 10


class EmployeeData(BaseModel):
    """
    Employee data for response
    """

    employment_date: date = Field(..., alias='employmentDate')
    full_name: str = Field(..., alias='fullName')
    position: str
    salary: Decimal

    class Config:  # pylint: disable=too-few-public-methods
        """
        Pydantic model config
        """

        allow_population_by_field_name: bool = True


class EmployeesPage(BaseModel):
    """
    Employees page for response
    """

    employees: list[EmployeeData]
    has_next_page: bool = Field(..., alias='hasNextPage')

    class Config:  # pylint: disable=too-few-public-methods
        """
        Pydantic model config
        """

        allow_population_by_field_name: bool = True


def get_department_employees(
    department_id: str,
    page_number: int,
) -> EmployeesPage:
    """
    Method for getting list of employees by department identifier
    :param department_id: Department identifier
    :param page_number: Number of page to get
    :return: Object containing list of employees
    """

    page: Page = Paginator(
        Employee.objects.filter(department_id=department_id).order_by(
            'employee_id',
        ),
        PAGE_SIZE,
    ).get_page(page_number)

    return EmployeesPage(
        employees=list(page.object_list.values()),
        has_next_page=page.has_next(),
    )
