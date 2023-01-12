import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from views import get_all_locations, get_single_location, create_location, delete_location, update_location
from views import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from views import get_all_customers, get_single_customer, create_customer, update_customer
from views import verify_data

# Method mapper for all resources
method_mapper = {
    "animals": {
        "single": get_single_animal,
        "all": get_all_animals
    },
    "customers": {
        "single": get_single_customer,
        "all": get_all_customers
    },
    "employees": {
        "single": get_single_employee,
        "all": get_all_employees
    },
    "locations": {
        "single": get_single_location,
        "all": get_all_locations
    },
}

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """Splits URL to determine if a client requested an entire resource or a single dictionary

        Args:
            path (string): URL to specific resource needed

        Returns:
            tuple: (resource, id)
        """

        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def get_all_or_single(self, resource, id):
        """Returns a single matching resource dictionary or an entire resource list

        Args:
            resource (string): The resource to be accessed
            id (int): The primary key of the requested resource dictionary

        Returns:
            dict: The matching resource dictionary
        """
        if id is not None:
            response = method_mapper[resource]["single"](id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = { "message": f"{id} can not be found.  Please enter a valid resource id." }
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"]()

        return response

    def do_GET(self):
        """Handles GET requests to the server
        """
        response = None
        (resource, id) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            # Verify post properties match resource properties
            verified_data = verify_data(resource, post_body)
            
            if verified_data is True:
                # Initialize new animal
                new_animal = None
                new_animal = create_animal(post_body)

                # Encode the new animal and send in response
                self.wfile.write(json.dumps(new_animal).encode())
            else:
                self._set_headers(400)
                # Encode the new animal and send in response
                self.wfile.write(json.dumps(verified_data).encode())

        #Add a new location to the list
        if resource == "locations":
            # Verify post properties match resource properties
            verified_data = verify_data(resource, post_body)

            if verified_data is True:
                # Initialize new location
                new_location = None
                new_location = create_location(post_body)

                # Encode the new location and send in response
                self.wfile.write(json.dumps(new_location).encode())
            else: 
                self._set_headers(400)
                # Encode the new location and send in response
                self.wfile.write(json.dumps(verified_data).encode())

        #Add a new employee to the list
        if resource == "employees":
            # Verify post properties match resource properties
            verified_data = verify_data(resource, post_body)
            
            if verified_data is True:
                # Initialize new employee
                new_employee = None
                new_employee = create_employee(post_body)

                # Encode the new employee and send in response
                self.wfile.write(json.dumps(new_employee).encode())
            else:
                self._set_headers(400)
                # Encode the new employee and send in response
                self.wfile.write(json.dumps(verified_data).encode())

        #Add a new customer to the list
        if resource == "customers":
            # Verify post properties match resource properties
            verified_data = verify_data(resource, post_body)
            
            if verified_data is True:
                # Initialize new customer
                new_customer = None
                new_customer = create_customer(post_body)

                # Encode the new customer and send in response
                self.wfile.write(json.dumps(new_customer).encode())
            else: 
                self._set_headers(400)
                # Encode the new customer and send in response
                self.wfile.write(json.dumps(verified_data).encode())

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
        
        # Delete a single location from the list
        if resource == "locations":
            update_location(id, post_body)

        # Delete a single employee from the list
        if resource == "employees":
            update_employee(id, post_body)

        # Delete a single customer from the list
        if resource == "customers":
            update_customer(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        """Deletes dictionary from database
        """

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Prevent client from deleting customer data
        if resource == "customers":
            self._set_headers(405)

            # Encode the new item and send in response
            self.wfile.write("".encode())
        else:
            # Set a 204 response code
            self._set_headers(204)

            # Delete a single animal from the list
            if resource == "animals":
                delete_animal(id)

            # Delete a single location from the list
            if resource == "locations":
                delete_location(id)

            # Delete a single location from the list
            if resource == "employees":
                delete_employee(id)

            # Encode the new item and send in response
            self.wfile.write("".encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
