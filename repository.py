DATABASE = {
    "animals":
        [
            {
                "id": 1,
                "name": "Snickers",
                "species": "Dog",
                "locationId": 1,
                "customerId": 4,
                "status": "Admitted"
            },
            {
                "id": 2,
                "name": "Roman",
                "species": "Dog",
                "locationId": 1,
                "customerId": 2,
                "status": "Admitted"
            },
            {
                "id": 3,
                "name": "Blue",
                "species": "Cat",
                "locationId": 2,
                "customerId": 1,
                "status": "Admitted"
            }
        ],
    "employees":
        [
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
        ],
    "customers":
        [
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
        ],
    "locations":
        [
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
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]

def retrieve(resource, id):
    """For GET requests to a single resource"""
    return DATABASE[resource][id]


def create(resource, post_body):
    """For POST requests to a collection"""
    
    # Get the id value of the last resource in the list
    max_id = DATABASE[resource][-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the resource dictionary
    post_body["id"] = new_id

    # Add the resource dictionary to the list
    DATABASE[resource].append(post_body)

    # Return the dictionary with `id` property added
    return post_body


def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    for index, dict in enumerate(DATABASE[resource]):
        if dict["id"] == id:
            # Found the dictionary. Update the value.
            DATABASE[resource][index] = post_body
            break

def delete(resource, id):
    """For DELETE requests to a single resource"""
    for index, dict in enumerate(DATABASE[resource]):
        if dict["id"] == id:
            # Found the dictionary. Update the value.
            DATABASE[resource].pop(index)
            break