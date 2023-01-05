LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    """Returns all location dictionaries"""
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    """Finds the matching location dictionary for the specified location id

    Args:
        id (int): location id

    Returns:
        object: location dictionary
    """
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
