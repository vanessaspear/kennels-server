CUSTOMERS = [
    {
        "id": 1,
        "name": "Halimah Yacob"
    },
    {
        "id": 2,
        "name": "Mahathir Mohamad"
    },
    {
        "id": 3,
        "name": "Prayut Chan-o-cha"
    }
]

def get_all_customers():
    """Returns all customer dictionaries"""
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """Finds the matching customer dictionary for the specified customer id

    Args:
        id (int): customer id

    Returns:
        object: customer dictionary
    """
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
