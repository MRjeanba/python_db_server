"""
Author: Jean-Baptiste Garibo
Date: 20 november 2022
COMP 348 Assignment 2

This file contains all the logic of the server side, it also contains the content of the database in a dictionary DS
All the CRUD operations are located in this file
"""
import socketserver
import collections
import operator


# Method that will take a list of string in parameters and returns a list of tuples split at each "|"
def modify_list(list_of_string):
    list_of_tuples = [tuple(map(str, sub.split("|"))) for sub in list_of_string]
    return list_of_tuples


# This method will take in param the list of tuples and create a dictionary with it
# each first entry in the tuples will be verified, if it is not empty, then it will be added to the dictionary
def create_dictionary(list_data):
    db_dictionary = {}
    for items in range(len(list_data)):
        if list_data[items][0] != "":
            db_dictionary.update({list_data[items][0]: list_data[items]})
    return db_dictionary


# loading the DB file:
f = open('data.txt', 'r')
dataList = f.readlines()  # store the content of the database into a string
f.close()

tuple_list = modify_list(dataList)
print(dataList)
dic = create_dictionary(tuple_list)


# Search a name in the dictionary, return true if found, false otherwise
def search_customer(customer_name):
    match = False
    # now that we only have the first name, we will process a search inside the dictionary
    for keys in dic:
        if customer_name == keys:
            match = True
    return match


# Add a customer in the Database (data.txt) and in the dictionary containing the customers
def add_customer(formatted_data, first_name):
    file = open('data.txt', 'a')
    formatted_data += "\n"
    file.writelines(formatted_data)
    file.close()
    formatted_data = tuple(formatted_data.split("|"))
    dic.update({first_name: formatted_data})


# Delete a customer from the database, the text file and also the dictionary
def delete_customer(name):
    del dic[name]
    file = open('data.txt', 'w')
    to_write = ""
    for keys in dic:
        for items in dic[keys]:
            if items.__contains__("\n"):  # We only add the "|" if the line is not finished
                to_write += items
            else:
                to_write += items + "|"
            # to_write += (''.join(dic[keys]).replace(",", "|"))
    print(to_write)
    file.writelines(to_write)
    file.close()


# this method updates a customer from the DB, and also from the txt file
def update_db(name, new_value, field):

    # 1 means update age
    if field == "4":
        list_to_change = list(dic[name])
        list_to_change[1] = new_value
        dic.update({name: tuple(list_to_change)})

    # 2 means update the address
    elif field == "5":
        list_to_change = list(dic[name])
        list_to_change[2] = new_value
        dic.update({name: tuple(list_to_change)})

    # 3 means update the address
    elif field == "6":
        list_to_change = list(dic[name])
        list_to_change[3] = new_value + "\n"
        dic.update({name: tuple(list_to_change)})

    # Now we have to write on the file in order to store the changes dones
    file = open('data.txt', 'w')
    to_write = ""
    for keys in dic:
        for items in dic[keys]:
            if items.__contains__("\n"):  # We only add the "|" if the line is not finished
                to_write += items
            else:
                to_write += items + "|"
            # to_write += (''.join(dic[keys]).replace(",", "|"))
    print(to_write)
    file.writelines(to_write)
    file.close()


# This method build the report string and send it back to the server that will process it to the client side
def build_report(db_dictionary):
    report = "** Python DB contents **\n"

    # Sort the dictionary db_dictionary by keys and return a list of tuples inside of db variable
    db = sorted(db_dictionary.items(), key=operator.itemgetter(0))
    sorted_db = collections.OrderedDict(db)  # here we transform our db variable into a dictionary now sorted by keys
    # loop in the sorted dictionary to display the report
    for keys in sorted_db:
        if keys == "":
            continue
        for items in sorted_db[keys]:
            if items.__contains__("\n"):  # We only add the "|" if the line is not finished
                report += items
            else:
                report += items + "|"
    return report

