# MyMenus

## Projet

Ce projet a pour but de regrouper un grand nombre de plats afin d'en proposer aléatoirement aux utilisateurs lorsqu'ils cherchent quoi manger.

## Technologies

**Backend** : Django

**Frontend**: React

## Contribitions

If you want to contribute to the project, please follows guilines of [CONTRIBUTING.md](./CONTRIBUTING.md)

## Set up

1. Create a virtual environment

`python3 -m venv .venv`

2. Activate the environment

`source .venv/bin/activate`

3. Install requirements

`pip install -r requirements.txt`

4. Import the data in DB

`python3 manage.py shell`
`from data import import_receipts_from_csv`
`import_receipts_from_csv('api/menus.csv')`

6. Create a .env file into the frontend folder and define the api url :
   `VITE_API_URL="http://127.0.0.1:8000"`

7. Install the frontend dependencies

`npm install`

6. Start the servers

`npm run dev`

`python3 manage.py runserver`
