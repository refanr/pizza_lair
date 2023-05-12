# Pizza Lair

This is a student project for T-220-VLN2 - Verklegt Námskeið 2 at RU, Reykjavik University


## Authors

- Birgir Rafn Stefánsson
- Emil Árnason
- Reynir Gunnarsson

## The Project

This project is a Django web app, using the MTV pattern and Django Model API, it uses a PostgreSQL database, 
hosted at Google Cloud. It is an e-commerce website for the Pizza Lair imaginary restaurant, users can view a 
Pizza menu, special offers, and register as users of the site, complete with a customizable profile page. 

## Installation and running server

Clone this repository into a clean directory, using:
`git clone https://github.com/refanr/pizza_lair.git`

Install required packages from included requirements.txt file, using:
`python -m pip install -r requirements.txt`

Run the server from the root directory pizza_lair, using:
`python manage.py runserver <port>` - port number is optional, default is 8000

Using any browser (Google Chrome recommended), go to: `http://localhost:8000` or `http://127.0.0.1:8000`


## Packages in requirements.txt

- asgiref==3.6.0
- Django==4.2
- django-countries==7.5.1
- Pillow==9.5.0
- psycopg2-binary==2.9.6
- sqlparse==0.4.4
- typing_extensions==4.5.0
