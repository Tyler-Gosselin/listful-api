# Flask Api Listful

​
This is the back end to Listful. Please follow the below to set up your structure
​

## Setup

- Setup Virtual Environment

```
$ python -m venv venv
$ source venv/bin/activate (Mac)
$ venv\Scripts\activate (Windows)
(venv) $ _
```

​

- Install the packages

```
(venv) $ pip install -r requirements.txt
```

​

## Database Setup

​
We're using `flask-migrate` with `alembic` to do our database migrations. You will notice there is already a migrations folder. This keeps track of our migrations. For more information read the [flask-migrate docs](https://flask-migrate.readthedocs.io/en/latest/), [alembic](https://alembic.sqlalchemy.org/en/latest/), or [this tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database).
​

- Run the upgrade command to start your database

```
(venv) $ flask db upgrade
```

## Running The Server

```
(venv) $ flask run
```

# Test routes

> Please follow these steps to test if routes work

- go to http://localhost:5000
- this route will test in Postman: http://localhost:5000/create-user
- use this to test:

```JSON
{
  "username": "username",
  "email": "email",
  "password": "password"
}
```

- finally go to http://localhost:5000/users to get all users

# Updating models/database

- After changing or adding a model run the migrate command

```
(venv) $ flask db migrate -m "Message"
```

- After running the migrate command, run the upgrade command

```
(venv) $ flask db updgrade
```

# Adding packages

- run the following command after installing new packages:

```
$ pip freeze > requirements.txt
```
