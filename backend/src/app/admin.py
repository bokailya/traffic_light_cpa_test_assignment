"""
Model registration for Django admin
"""

from django.contrib.admin import site

from app.models import Department
from app.models import Employee


site.register(Department)
site.register(Employee)
