import sqlite3
from models import Employee, Location

def get_employees_by_location(location):
    """Gets the employees at a specific location

    Arguments: 
        int: The location foreign key 

    Returns: 
        list: List of employee dictionaries
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name, 
            e.address, 
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( location, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees

def get_all_employees():
    """Returns all employee dictionaries"""
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name, 
            e.address, 
            e.location_id,
            l.id location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    """Finds the matching employee dictionary for the specified employee id

    Args:
        id (int): employee id

    Returns:
        object: employee dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.id location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        location = Location(data['location_id'], data['location_name'], data['location_address'])

        employee.location = location.__dict__

    return employee.__dict__

def delete_employee(id):
    """Deletes a single employee

    Args:
        id (int): id of employee to be deleted
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    """Iterate employee list

    Args:
        id (int): Employee id
        new_employee (dictionary): Replacement employee dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?,
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'], new_employee['location_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
        