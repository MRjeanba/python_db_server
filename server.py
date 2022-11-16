"""
Author: Jean-Baptiste Garibo
Date: 20 november 2022
COMP 348 Assignment 2

This file is maybe too big for what it should do, it contains the class MyTCPHandler
responsible for listening to request,Since I don't really know networking,
I didn't really touch to this class and just added the things that I needed

All the methods used here are contained in the server_methods.py file

"""
from server_methods import *


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    # listening to requests
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        # case finding a customer in the DB
        if self.data.decode()[0] == "1":
            # the next step is done to get off the number in front of the first name
            name_to_find = self.data.decode()[1:]
            match = search_customer(name_to_find)
            # if match is False, then we send back an error message to the user
            if match is False:
                self.data = "{} not found in database".format(name_to_find)
                self.request.sendall(self.data.encode())
            else:  # if we reach the else, match is true, so we send info to the client
                customer_info = ""
                for items in dic[name_to_find]:
                    if items.__contains__("\n"):  # We only add the "|" if the line is not finished
                        customer_info += items
                    else:
                        customer_info += items + "|"
                self.data = customer_info
                self.request.sendall(self.data.encode())

        # Add a customer to the database
        elif self.data.decode()[0] == "2":
            # the next step is done to get off the number in front of the first name
            entry_to_add = self.data.decode()[1:]

            # Since the data that we receive is formatted for the database,
            # we have to take the first index after split to get the name and search if the customer already exists
            name_of_customer = entry_to_add.split("|")[0]
            match = search_customer(name_of_customer)

            # Match is true means that the customer already exists
            if match is True:
                self.data = "{} already exists".format(name_of_customer)
                self.request.sendall(self.data.encode())
            else:
                add_customer(entry_to_add, name_of_customer)
                self.data = "{} added in database".format(name_of_customer)
                self.request.sendall(self.data.encode())

        # Delete a customer from the database
        elif self.data.decode()[0] == "3":
            customer_name = self.data.decode()[1:]
            # match is a boolean value, if it is true, it means that we found the customer in the DB
            match = search_customer(customer_name)
            # match false = we did not find the customer in DB
            if match is False:
                self.data = "{} does not exist".format(customer_name)
                self.request.sendall(self.data.encode())
            else:
                delete_customer(customer_name)
                self.data = "{} has been deleted".format(customer_name)
                self.request.sendall(self.data.encode())

        # Update age field
        elif self.data.decode()[0] == "4":
            # get rid of the code option,
            # we should have the number corresponding to the field to modify and the name of the customer
            field_number = self.data.decode()[0]
            customer_name = self.data.decode()[1:]
            name = customer_name.split("|")
            new_value = name[1]
            name = name[0]

            # To save time, we can check if the customer is in the DB and if yes we will update
            if search_customer(name) is False:
                self.data = "{} does not exist so cannot be updated".format(name)
                self.request.sendall(self.data.encode())
            else:
                update_db(name, new_value, field_number)
                self.data = "{} has been updated".format(name)
                self.request.sendall(self.data.encode())
        # Update address field
        elif self.data.decode()[0] == "5":
            # get rid of the code option,
            # we should have the number corresponding to the field to modify and the name of the customer
            field_number = self.data.decode()[0]
            customer_name = self.data.decode()[1:]
            name = customer_name.split("|")
            new_value = name[1]
            name = name[0]

            # To save time, we can check if the customer is in the DB and if yes we will update
            if search_customer(name) is False:
                self.data = "{} does not exist so cannot be updated".format(name)
                self.request.sendall(self.data.encode())
            else:
                update_db(name, new_value, field_number)
                self.data = "{} has been updated".format(name)
                self.request.sendall(self.data.encode())
        # Update phone field
        elif self.data.decode()[0] == "6":
            # get rid of the code option,
            # we should have the number corresponding to the field to modify and the name of the customer
            field_number = self.data.decode()[0]
            customer_name = self.data.decode()[1:]
            name = customer_name.split("|")
            new_value = name[1]
            name = name[0]

            # To save time, we can check if the customer is in the DB and if yes we will update
            if search_customer(name) is False:
                self.data = "{} does not exist so cannot be updated".format(name)
                self.request.sendall(self.data.encode())
            else:
                update_db(name, new_value, field_number)
                self.data = "{} has been updated".format(name)
                self.request.sendall(self.data.encode())
        # Print report
        elif self.data.decode() == "7":
            self.data = build_report(dic)
            self.request.sendall(self.data.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
