# moulakhasatyAPI
an API programmed with Django Rest Framework for the molakhasaty app.

molakhasaty is a platform that helps university students exchange notes and course resumés.
this is an api that can serve the necessary data to single page application clients

Challenges and key features:
-Authentification: 
non authenticated users can only view existing notes before registration. autenticated users can post new notes, delete them and leave likes and comments. only admin superusers can see or edit the list of users.
this was garanteed with the use of rest_framework default TokenAuthentication and custom permissions.

-each note is accompanied with files that can be pictures of notes, pdfs... these files have to be sent in a compressed zip file for security measures and the api verifies this before storing them.

-the api also provides a complete schema and documentation at /api/schema and /api/documentation.
