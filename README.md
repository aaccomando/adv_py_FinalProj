# Project Overview
  Website that allows a user to search by ingredients!

  ![alt tag](static/img/homepage.png)

# Development

## Setting up the environment (through command line):
  - first clone the repository
    - git clone "URL-HERE"
  - inside the main directory( adv_py_FinalProj ) run:
    - pip install -r requirements.txt
      - might need to install a load of stuff including
        - pip sqlalchemy flask-sqlalchemy postgres flask-wtf
  - then in same directory on command line, type:
    - `source venv/bin/activate`
  - then you can run the project by typing:
    - python routes.py

  - to see the project in browser go to:
    - localhost:8000
      - to change port-> in routes.py, go to main function at bottom

####  Follow the instructions below to integrate the database.

# Setting up The Database
#### More Specific Instructions Below..
  - when you clone or pull the repo you should have a "db.sql" file in the directory
  - make sure you have a postgres server, and the server is running.
    - Instructions found [here](https://www.postgresql.org/download/)
  - dependant on your postgres server installation:
    - you'll have command line commands to import a database table
    - for example on mac
      - we install the app above and when the postgres server is running,
        go to the project directory and run (in terminal):
      - `psql < db.sql`
    - the server should now have a database called "fooddb"
      - this is where we are reading and writing our users information
      - soon to have multiple tables to incorportate more advanced
       features on the front end

## Postgres (mac):
  - [download This](https://postgresapp.com/documentation/all-versions.html)
  - Run this command to add postgres cli commands to the Path environment:
    - `sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`
  - Make sure postgres server is running then in terminal, within the project directory:
  - run: `psql < db.sql`
    - This script initiates the database on your machine.

## Postgres (window):
  - [instructions](https://www.postgresql.org/download/windows/) here
  - follow similar instructions as given below for general steps
    - you may have to add psql to your path environment variables

## Postgres (ubuntu):
  - follow [these](https://www.postgresql.org/download/linux/ubuntu/) instructions
  - in our active directory there is a db.sql file
  - make sure your psql server is running, then in terminal type:
    - `postgres -D /usr/local/pgsql/data`
    - `psql < db.sql`
  - then the database should be created and you can interact with it through the website in localhost
  - if you get a <username> fatal error or something:
    - do `sudo su - postgres psql`
    - in bash: `CREATE DATABASE template1`
    - then: `CREATE DATABASE <username>`
    - [permission help](https://dba.stackexchange.com/questions/33285/granting-a-user-account-permission-to-create-databases-in-postgresql)
