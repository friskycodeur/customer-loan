# Customer-Loan Application

## Objective -

Create an Interface for csv uploads of customer-loan data and show the details on screen via API.

## Application overview -

- Tables for Customer , Branch Data, Customer Home Address Data,Customer Office Data,Loan Amount Data.
- Functionality to upload a csv with the data for the above tables and saves data in all respective columns.
- Customer is the foreign key in all the other tables.
- CSV Format is at the end of this readme file.

## Live Links -

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

1. **Uploading CSV Files**

   `end-point: loan/csv`

   CSV Format : [https://easyupload.io/dm1vo4](https://easyupload.io/dm1vo4)

2. **GET Request:**

   `end-point: loan/customer/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

   `end-point: loan/branch/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found
   `end-point: loan/home/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found
   `end-point: loan/office/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found
   `end-point: loan/loan/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found
