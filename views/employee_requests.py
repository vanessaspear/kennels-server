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
