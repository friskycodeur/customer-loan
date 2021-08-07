# Django - Authentication

## Objective -

Create an API Interface for user authentication.

<!-- ## Application overview -

- Patient data can be added , deleted , updated or retrieved.
- On homepage there is a list of all the patients.
- The patient object has the following fields :
  -First Name
  -Last Name
  -Gender
  -Age
  -Disease (Problem)
  -Doctor name
  -Doctor fees (default 500)
  -Started meds on date

## Live Links -

**Heroku Hosted Link** : [https://patient-backend-django.herokuapp.com/](https://patient-backend-django.herokuapp.com/)

## Demo Credentials -

**Username:** admin
**Password:** pass -->

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
