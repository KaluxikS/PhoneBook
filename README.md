# PhoneBook
This application is backend of a PhoneBook API made using FastApi.

Description
---
This project is a phone book application. First, we have to register a user using POST route '/user/'. When we have created user (login and password which is hashed), we have to login and then we have access to contacts, that was made by this user. You can have multiple users. I'm using JWT TOKEN and fastapi.sercurity to provide the authentication.

How to use
---
There are several routes that you can see at http://127.0.0.1:8000/docs after lunching the app.

'/contact/': (all work only on data of logged user)
- GET - shows all contacts
- POST - adds new contact
  
'/contact/{id}':
- GET - shows contact with specific id
- PUT - edits contact with specific id
- DELETE - delete contact with specific id

'/user/':
- GET - shows all users
- POST - adds new user

'/login/':
- POST - is used for authentication

How to install
---
1. Clone repository.
2. Make sure that your python version is 3.7 or above (if not update it)
3. In project file, using terminal and provided commands create new virtual environment for this project: "python -m venv venv" and "venv\Scripts\activate.bat"
   Now your virtual environment is created.
4. Using "pip install -r requirements.txt" install all required packages.
5. Use "uvicorn main:app --reload" to start app.
6. Use http://127.0.0.1:8000/docs to see all possible routes.
