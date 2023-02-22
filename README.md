# python_db_server
This project was realized in the class COMP 348 : Principle of programming languages.
The purpose of this assignment was to make us learn a little bit about the Python ecosystem and data structures

# The project
The project is a sort of a backend API which process data after a fetch to a dummy database which is in our case a txt file.
After this fetch I was responsible to transform the data that was in a string format to a dictionnary that map a username to a complete user profile  
user_name : userName|age|address|phoneNumber  
Then, the user has the possibility to make some CRUD operations on the processed data  
The user should only have access to a client 'interface', each of its choice should generate a request handled by the backend API, the latter
process the data and send it back to the user.

# Run the project
After cloning the repo on your local machine, you have to create a data.txt file next to the .py files. Inside this data.txt file, you can generate
some dummy data by respecting the following syntax:

                                                  randomName|randomAge|randomAdress|randomPhoneNumber
                                                  randomName|randomAge|randomAdress|randomPhoneNumber
                                                  randomName|randomAge|randomAdress|randomPhoneNumber
                                                  randomName|randomAge|randomAdress|randomPhoneNumber
                                                  ...
                                                  
You can obviously replace each field by the value that you want. After the creation of this file, you should be ready to go. 
You have now to open two terminal, from one run the following command: python server.py
This will start your server and make it listen to request, after that on the second terminal run the command: python client.py

Then, you can interact with the interface on the client terminal.
