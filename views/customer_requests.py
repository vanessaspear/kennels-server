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

def create_customer(customer):
    """Adds a new customer dictionary

    Args:
        customer (dictionary): Information about the customer

    Returns:
        dictionary: Returns the customer dictionary with an CUSTOMER id
    """
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """Deletes a single customer

    Args:
        id (int): id of customer to be deleted
    """
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """Iterate customer list

    Args:
        id (int): Customer id
        new_customer (dictionary): Replacement customer dictionary
    """
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
        