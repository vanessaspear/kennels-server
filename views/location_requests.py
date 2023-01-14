import sqlite3
from models import Location

def get_all_locations():
    """Returns all location dictionaries"""
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name, 
            l.address 
        FROM location l
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return locations

def get_single_location(id):
    """Finds the matching location dictionary for the specified location id

    Args:
        id (int): location id

    Returns:
        object: location dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

    return location.__dict__

def delete_location(id):
    """Deletes a single location

    Args:
        id (int): id of location to be deleted
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            DELETE FROM location
            WHERE id = ?
            """, (id, ))

def update_location(id, new_location):
    """Iterate location list

    Args:
        id (int): Location id
        new_location (dictionary): Replacement location dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
        