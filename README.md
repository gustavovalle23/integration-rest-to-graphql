# Integration System between Rest API and GraphQL

> This project use [FastAPI](https://fastapi.tiangolo.com/) as web framework and [Strawberry](https://strawberry.rocks/) GraphQL library

## Dependencies

All the dependencies for this project are listed in [requirements.txt](requirements.txt).

In order to make your global Python dependencies untouched locally use the [virtualenv](https://virtualenv.pypa.io/en/latest/):

```sh
# Create a virtual env
python3 -m venv venv

# Activate the virtual env
source venv/bin/activate

# Install dependencies inside virtual env
pip3 install -r requirements.txt

# To exit the virtual env you could execute the following command
deactivate
```

## Running server

To run server, just run:
```sh
python3 main.py
```
Or for auto reload:
```sh
uvicorn main:app --reload
```
