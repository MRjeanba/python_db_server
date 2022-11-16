"""
Author: Jean-Baptiste Garibo
Date: 20 november 2022
COMP 348 Assignment 2

This file just make run the client applications, all the method used here are from the client_methods file

TO THINK ABOUT : DataBase is not sorted, ONLY the print is sorted to the user screen, should it stays like that ? or DB
should also be sorted ?
Test some more updates, maybe it can have some problems

"""
from client_methods import *


# Display the menu to the user
display_menu()
user_choice = input("Select: ")


# this while loop controls the flow of operations
while user_choice != "8":

    # Searching in the DB, asks for the name
    if user_choice == "1":
        search(user_choice)

    # Add customer to DB, asks name, age, address and phone number
    elif user_choice == "2":
        add_customer(user_choice)

    # Delete a customer, asks for a customer name
    elif user_choice == "3":
        delete_customer(user_choice)

    # Update option, asks for a customer name and a new value
    elif user_choice == "4":
        update_database(user_choice)

    # Update option, asks for a customer name and a new value
    elif user_choice == "5":
        update_database(user_choice)

    # Update option, asks for a customer name and a new value
    elif user_choice == "6":
        update_database(user_choice)

    # Print report option, we display the content of the database to the user
    elif user_choice == "7":
        print_report(user_choice)

    display_menu()
    user_choice = input("Select: ")

print("Thank you for using our DB server !")