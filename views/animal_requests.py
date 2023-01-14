import sqlite3
from models import Animal, Location, Customer

def get_animals_by_location(location):
    """Gets the animals at a specific location

    Arguments: 
        int: The location foreign key 

    Returns: 
        list: List of animal dictionaries
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.location_id = ?
        """, ( location, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'] , row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return animals

def get_animals_by_status(status):
    """Gets the animals at a specific status

    Arguments: 
        int: The status foreign key 

    Returns: 
        list: List of animal dictionaries
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'] , row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return animals

def get_all_animals():
    """Gets all animals
    Returns:
        dict: All animal dictionaries"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.id customer_id,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c 
            ON c.id = a.customer_id
        """)

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            animal.location = location.__dict__

            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password'])

            animal.customer = customer.__dict__

            animals.append(animal.__dict__)

    return animals

# Function with a single parameter
def get_single_animal(id):
    """Finds the matching animal dictionary for the specified animal id

    Args:
        id (int): animal id

    Returns:
        object: animal dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.id customer_id,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c 
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        location = Location(data['location_id'], data['location_name'], data['location_address'])

        animal.location = location.__dict__

        customer = Customer(data['customer_id'], data['customer_name'], data['customer_address'], data['customer_email'], data['customer_password'])

        animal.customer = customer.__dict__

        return animal.__dict__

def create_animal(new_animal):
    """Adds a new animal dictionary

    Args:
        animal (dictionary): Information about the animal

    Returns:
        dictionary: Returns the animal dictionary with an ANIMAL id
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['locationId'],
              new_animal['customerId'], ))
        
        id = db_cursor.lastrowid

        new_animal['id'] = id
    
    return new_animal


def delete_animal(id):
    """Deletes a single animal

    Args:
        id (int): Animal id
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

def update_animal(id, new_animal):
    """Updates the animal dictionary with the new values

    Args:
        id (int): Animal id
        new_animal (dict): Animal dictionary with updated values
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
