EMPLOYEES = [
    {
        "id": 1,
        "name": "Fumio Kishida"
    },
    {
        "id": 2,
        "name": "Tsai Ing-wen"
    },
    {
        "id": 3,
        "name": "Xi Jinping"
    }
]

def get_all_employees():
    """Returns all employee dictionaries"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """Finds the matching employee dictionary for the specified employee id

    Args:
        id (int): employee id

    Returns:
        object: employee dictionary
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    """Adds a new employee dictionary

    Args:
        employee (dictionary): Information about the employee

    Returns:
        dictionary: Returns the employee dictionary with an EMPLOYEE id
    """
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    """Deletes a single employee

    Args:
        id (int): id of employee to be deleted
    """
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """Iterate employee list

    Args:
        id (int): Employee id
        new_employee (dictionary): Replacement employee dictionary
    """
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break
        