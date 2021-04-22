"""
Department ORM model
"""

from uuid import uuid4

from django.db.models import CASCADE, CharField, ForeignKey, Model, UUIDField


class Department(Model):
    """
    Department ORM model
    """

    department_id: UUIDField = UUIDField(default=uuid4, editable=False, primary_key=True)
    department_name: CharField = CharField(max_length=128)
    parent: ForeignKey = ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=CASCADE,
        related_name='children',
    )

    def __str__(self) -> str:
        """
        Generate string representation for django admin
        :param self: Department ORM-object
        :return: string representation for django admin
        """

        return self.department_name
