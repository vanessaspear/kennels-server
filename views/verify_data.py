def verify_data(resource, post_body):
    """Verifies that post body includes all properties required by resource

    Args:
        resource (string): Name of database dictionary
        post_body (dict): Data to be posted by client

    Returns:
        (string): A message with required dict properties
    """
    if resource == "animals":
        animal_keys = ["name", "species", "locationId", "customerId", "status"]
        post_keys = []
        count = 0

        for post_key in post_body:
            post_keys.append(post_key)

        for animal_key in animal_keys:
            for post_key in post_keys:
                if animal_key == post_key:
                    count = count + 1

        if count != len(animal_keys) or len(post_keys) > len(animal_keys):
            return {"message": f"The animal resource is required to have the following properties: {animal_keys}. Please re-post your data with these properties."}
        return True

    if resource == "locations":
        location_keys = ["name", "address"]
        post_keys = []
        count = 0

        for post_key in post_body:
            post_keys.append(post_key)

        for location_key in location_keys:
            for post_key in post_keys:
                if location_key == post_key:
                    count = count + 1

        if count != len(location_keys) or len(post_keys) > len(location_keys):
            return {"message": f"The location resource is required to have the following properties: {location_keys}. Please re-post your data with these properties."}
        return True

    if resource == "customers":
        customer_keys = ["name"]
        post_keys = []
        count = 0

        for post_key in post_body:
            post_keys.append(post_key)

        for customer_key in customer_keys:
            for post_key in post_keys:
                if customer_key == post_key:
                    count = count + 1

        if count != len(customer_keys) or len(post_keys) > len(customer_keys):
            return {"message": f"The customer resource is required to have the following properties: {customer_keys}. Please re-post your data with these properties."}
        return True

    if resource == "employees":
        employee_keys = ["name"]
        post_keys = []
        count = 0

        for post_key in post_body:
            post_keys.append(post_key)

        for employee_key in employee_keys:
            for post_key in post_keys:
                if employee_key == post_key:
                    count = count + 1

        if count != len(employee_keys) or len(post_keys) > len(employee_keys):
            return {"message": f"The employee resource is required to have the following properties: {employee_keys}. Please re-post your data with these properties."}
        return True