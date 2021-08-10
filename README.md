# Django - Authentication

## Objective -

Create an API Interface for user authentication.

## Application overview -

- User registration , login , list of all users with appropriate errors and status.

## Live Links -

**Postman Collections:** [https://www.getpostman.com/collections/13abf8632b5f2983a733](https://www.getpostman.com/collections/13abf8632b5f2983a733)
**Heroku Hosted Link** : [https://customer-loan.herokuapp.com/](https://customer-loan.herokuapp.com/)

## Demo Credentials -

**Username:** admin
**Email:** admin@gmail.com
**Password:** pass

## Setup Instructions

First make sure that you have the following installed.

- Python 3 and virtualenv

Now do the following to setup project

```bash
# assuming that the project is already cloned.

cd patients

# one time
virtualenv -p $(which python3) pyenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements/dev.txt

# update settings
cp nursery/settings/local.sample.env nursery/settings/local.env

# generate a secret key or skip(has a default value) and then replace the value of `SECRET_KEY` in environment file(here local.env)
./scripts/generate_secret_key.sh

# update relevant variables in environment file

# run migrate
python manage.py migrate
```

To access webserver, run the following command

```bash
python manage.py runserver
```

## Endpoints

1. **GET Request:**

   `end-point: accounts/api/register/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

   `end-point: accounts/api/users/<username>`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

2. **Post Request:**

   `accounts/api/register/`

   Accepted Response : status 201 Created

   Error Response : status 400 Bad Request

   `accounts/api/login/`

   Accepted Response : status 201 Created

   Error Response :status 400 Bad Request
