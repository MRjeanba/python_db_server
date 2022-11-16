"""
Author: Jean-Baptiste Garibo
Date: 20 november 2022
COMP 348 Assignment 2

This file contains all the client-side logic of the program, we send and receive the data from here
"""
import socket
HOST, PORT = "localhost", 9999
data = ""


# method to display the menu to the user
def display_menu():
    print("""Python DB Menu
    1. Find customer
    2. Add customer
    3. Delete customer
    4. Update customer age
    5. Update customer address
    6. Update customer phone
    7. Print report
    8. Exit
    """)


# Process the search in the database
def search(choice):
    name = input("Customer Name: ")
    # concatenate string in order to process the request in the server side
    choice = choice + name

    # creates a socket to send and receive information
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(choice, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("DB response:: {}".format(received))


# Add a customer to the database
def add_customer(choice):
    name = input("Name of the customer to add: ")
    age = input("age of the customer to add: ")
    address = input("address of the customer: ")
    phone_num = input("phone num of the customer: ")
    formatted_data = choice + name + "|" + age + "|" + address + "|" + phone_num

    # send the data to the server side
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(formatted_data, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("DB response: {}".format(received))


# Delete a customer from the database
def delete_customer(choice):
    name = input("Customer Name to delete: ")
    # concatenate string in order to process the request in the server side
    choice = choice + name

    # creates a socket to send and receive information
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(choice, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("DB response:: {}".format(received))


# Asks for a name and for the field that we want to update
def update_database(choice):
    name = input("Customer Name to update: ")
    # concatenate string in order to process the request in the server side
    choice = choice + name
    choice = choice + "|"  # here we just add a separation to add after that the new value
    new_value = input("Now, what should be the new value ? :")
    choice += new_value

    # creates a socket to send and receive information
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(choice, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print(received)


# Print the report to the screen
def print_report(choice):

    # creates a socket to send and receive information
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(choice, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(2048), "utf-8")
        print(received)

