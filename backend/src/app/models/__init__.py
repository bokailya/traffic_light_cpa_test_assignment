"""
Package containing all ORM models
"""

from app.models.department import Department
from app.models.employee import Employee


__all__ = [
    'Department',
    'Employee',
]
