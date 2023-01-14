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
    
def create_location(location):
    """Adds a new location dictionary

    Args:
        location (dictionary): Information about the location

    Returns:
        dictionary: Returns the location dictionary with a LOCATION id
    """
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

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
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break
        