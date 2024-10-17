# Recettes

## Projet

Ce projet a pour but de regrouper un grand nombre de plats afin d'en proposer aléatoirement aux utilisateurs lorsqu'ils cherchent quoi manger.
Il est possble de sélectionner le nombre de plats souhaité et de créer une liste de favoris.

## Technologies

**Backend** : Django
**Frontend**: React

## Set up

1. Create a virtual environment

`python3 -m venv .venv`

2. Activate the environment

`source .venv/bin/activate`

3. Install requirements

`pip install -r requirements.txt`

3. Create a .env file into the frontend folder and define the api url :
   `VITE_API_URL="http://127.0.0.1:8000"`

4. Install the frontend dependencies

`npm install`

5. Start the server

`npm run dev`
