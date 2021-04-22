"""
Getting department tree
"""
from collections import defaultdict
from typing import Optional

from pydantic import BaseModel, Field

from app.models import Department


class DepartmentTree(BaseModel):
    """
    Pydantic model for get department tree response
    """

    departments: dict[str, dict]
    department_id_to_name: dict[str, str] = Field(
        ...,
        alias='departmentIDToName',
    )

    class Config:  # pylint: disable=too-few-public-methods
        """
        Pydantic model config
        """

        allow_population_by_field_name: bool = True


def get_department_tree() -> DepartmentTree:
    """
    Method for getting department tree
    :return:
        Object with department tree dictionary and department names dictionary
    """

    children: defaultdict[Optional[str], list[str]] = defaultdict(list)

    department_id_to_name: dict[str, str] = {}

    for department in Department.objects.values(
        'department_id',
        'department_name',
        'parent',
    ):
        children[
            str(department['parent']) if department['parent'] else None
        ].append(str(department['department_id']))

        department_id_to_name[str(department['department_id'])] = (
            department['department_name']
        )

    return DepartmentTree(
        departments=_build_subtree(childs=children, root=None),
        department_id_to_name=department_id_to_name,
    )


def _build_subtree(
    childs: defaultdict[Optional[str], list[str]],
    root: Optional[str],
) -> dict[str, dict]:
    """
    Build department subtree
    :param root: subtree root department_id
    :param childs: Mapping for getting child department ids
    :return: Department subtree
    """

    return {
        child: _build_subtree(childs=childs, root=child)
        for child in childs[root]
    }
