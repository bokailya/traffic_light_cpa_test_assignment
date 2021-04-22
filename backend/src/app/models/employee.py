"""
Employee ORM model
"""

from uuid import uuid4

from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    DecimalField,
    ForeignKey,
    Model,
    UUIDField,
)

from app.models.department import Department


class Employee(Model):
    """
    Employee ORM model
    """

    department: ForeignKey = ForeignKey(Department, on_delete=CASCADE)
    employee_id: UUIDField = UUIDField(default=uuid4, editable=False, primary_key=True)
    employment_date: DateField = DateField()
    full_name: CharField = CharField(max_length=255)
    position: CharField = CharField(max_length=255)
    salary: DecimalField = DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        """
        Generate string representation for django admin
        :param self: Department ORM-object
        :return: string representation for django admin
        """

        return self.full_name
