function departmentTreeHTML(departmentIDToName, subtreeRoot, tree) {
    let hasChildren = false;
    let ul = document.createElement('ul');
    ul.setAttribute('class', 'list-group nested');
    for (const department in tree) {
        hasChildren = true;
        let li = document.createElement('li');
        li.setAttribute('class', 'list-group-item list-group-item-action')
        li.appendChild(departmentTreeHTML(departmentIDToName, department, tree[department]));
        ul.appendChild(li);
    }

    let frag = document.createDocumentFragment();
    if (hasChildren) {
        let caretSpan = document.createElement('span');
        caretSpan.setAttribute('class', 'caret');
        caretSpan.addEventListener(
            "click",
            function () {
                this.parentElement.querySelector(".nested").classList.toggle("active");
                this.classList.toggle("caret-down");
            },
        );
        frag.appendChild(caretSpan);
    }

    if (subtreeRoot === 'Departments')
        frag.appendChild(document.createTextNode('Departments'));
    else {
        let subtreeRootSpan = document.createElement('span');
        subtreeRootSpan.appendChild(document.createTextNode(departmentIDToName[subtreeRoot]));
        subtreeRootSpan.departmentID = subtreeRoot;
        subtreeRootSpan.addEventListener(
            "click",
            function () {
                Array.prototype.forEach.call(
                    document.getElementsByTagName('li'),
                    function (li) {
                        li.classList.toggle("active", false);
                    },
                );
                this.parentElement.classList.toggle("active");
                updateTable(this.departmentID, 1);
            },
        );
        frag.appendChild(subtreeRootSpan);
    }
    if (hasChildren)
        frag.appendChild(ul);
    return frag;
}


function updateTable(departmentID, pageNumber) {
    fetch(new Request('/api/department-employees?departmentID=' + departmentID + '&pageNumber=' + pageNumber))
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error('Something went wrong on api server!');
        }
    })
    .then(response => {
        let departmentEmployeesTableBody = document.getElementById('department-employees-table-body');
        departmentEmployeesTableBody.departmentID = departmentID;
        departmentEmployeesTableBody.pageNumber = pageNumber;

        departmentEmployeesTableBody.innerHTML = '';
        Array.prototype.forEach.call(
            response.employees,
            function (employee) {
                let fullName = document.createElement('td');
                fullName.appendChild(document.createTextNode(employee.fullName));
                let position = document.createElement('td');
                position.appendChild(document.createTextNode(employee.position));
                let employmentDate = document.createElement('td');
                employmentDate.appendChild(document.createTextNode(employee.employmentDate));
                let salary = document.createElement('td');
                salary.appendChild(document.createTextNode(employee.salary));

                let tr = document.createElement('tr');
                tr.appendChild(fullName);
                tr.appendChild(position);
                tr.appendChild(employmentDate);
                tr.appendChild(salary);
                departmentEmployeesTableBody.appendChild(tr);
            },
        )

        document.getElementById('previous-page-button').disabled = pageNumber === 1;
        document.getElementById('next-page-button').disabled = !response.hasNextPage;
    }).catch(error => {
        console.error(error);
    });
}

document.getElementById('next-page-button').addEventListener(
    'click',
    function () {
        const departmentEmployeesTableBody = document.getElementById('department-employees-table-body');
        updateTable(departmentEmployeesTableBody.departmentID, departmentEmployeesTableBody.pageNumber + 1);
    },
)

document.getElementById('previous-page-button').addEventListener(
    'click',
    function () {
        const departmentEmployeesTableBody = document.getElementById('department-employees-table-body');
        updateTable(departmentEmployeesTableBody.departmentID, departmentEmployeesTableBody.pageNumber - 1);
    },
)

fetch(new Request('/api/department-tree'))
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error('Something went wrong on api server!');
        }
    })
    .then(response => {
        document.getElementById('department-tree').appendChild(
            departmentTreeHTML(response.departmentIDToName, 'Departments', response.departments),
        );
    }).catch(error => {
        console.error(error);
    });
