# Emergency Contacts API

This API is for storing emergency contacts

## Setting up the project locally

To set up the project locally, clone the repository to your local machine. Since the SQLite3 file is in the repository, 
you should be able to use the database without initializing the database and performing migrations. Make sure Django is
installed on your machine or in your virtual environment. Then navigate to the outermost repo folder.

To start the Django server locally:

If in a virtual environment, use:
### `manage.py runserver`

Otherwise, use:
### `python3 manage.py runserver`

This should open a port to your localhost, accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Interacting with with API endpoints

### use [this link](https://emergency-contacts-73f6d01ca190.herokuapp.com/emergency_contacts/contacts/) for creating contacts

Use this base link to create new contacts. You can make a POST request through Django's GUI, or you can use something like curl in the command line.
### `curl -X POST -H "Content-Type: application/json" -d '{"first_name": "myfirstname", "last_name": "mylastname", "phone_number": "myphonenumber"}' https://emergency-contacts-73f6d01ca190.herokuapp.com/emergency_contacts/contacts/`

### use https://emergency-contacts-73f6d01ca190.herokuapp.com/emergency_contacts/contacts/<id> for deleting contacts

This also has the option of using the Django GUI or a terminal request, like:
### `curl -X DELETE https://emergency-contacts-73f6d01ca190.herokuapp.com/emergency_contacts/contacts/4`

This does require the knowledge of an id number for the user.
