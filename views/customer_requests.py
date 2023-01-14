import sqlite3
from models import Customer

def get_customer_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers

def get_all_customers():
    """Returns all customer dictionaries"""

    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    return customers

# Function with a single parameter
def get_single_customer(id):
    """Finds the matching customer dictionary for the specified customer id

    Args:
        id (int): customer id

    Returns:
        object: customer dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])

        return customer.__dict__

def delete_customer(id):
    """Deletes a single customer

    Args:
        id (int): id of customer to be deleted
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

def update_customer(id, new_customer):
    """Iterate customer list

    Args:
        id (int): Customer id
        new_customer (dictionary): Replacement customer dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            UPDATE Customer
                SET
                    name = ?,
                    address = ?,
                    email = ?,
                    password = ?
            WHERE id = ?
            """, (new_customer['name'], new_customer['address'],
                new_customer['email'], new_customer['password'], id, ))

            rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
        