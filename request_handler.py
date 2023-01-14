import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animals_by_location, get_animals_by_status
from views import get_all_locations, get_single_location, create_location, delete_location, update_location
from views import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee, get_employees_by_location
from views import get_all_customers, get_single_customer, create_customer, update_customer, get_customer_by_email
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
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

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
        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path: 
            (resource, id) = parsed
            response = self.get_all_or_single(resource, id)
        else:
            (resource, query) = parsed
            self._set_headers(200)
            if query.get('email') and resource == 'customers':
                response = get_customer_by_email(query['email'][0])

            if query.get('location_id') and resource == 'animals':
                response = get_animals_by_location(query['location_id'][0])

            if query.get('status') and resource == 'animals':
                response = get_animals_by_status(query['status'][0])

            if query.get('location_id') and resource == 'employees':
                response = get_employees_by_location(query['location_id'][0])    
        
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        # Initialize new resource
        new_resource = None

        # Add a new animal to the list
        if resource == "animals":
            new_resource = create_animal(post_body)
        elif resource == "customers":
            new_resource = create_customer(post_body)
        elif resource == "locations":
            new_resource = create_location(post_body)
        elif resource == "employees":
            new_resource = create_employee(post_body)

        # Encode the new resource and send in response
        self.wfile.write(f"{new_resource}".encode())

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "animals":
            success = update_animal(id, post_body)
        elif resource == "locations":
            success = update_location(id, post_body)
        elif resource == "employees":
            success = update_employee(id, post_body)
        elif resource == "customers":
            success = update_customer(id, post_body)
       
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

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
