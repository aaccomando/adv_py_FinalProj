# Development

### to setup the environment (through command line):
  - first clone the repository
    - git clone "URL"
  - inside the main directory( adv_py_FinalProj ) run:
    - pip install -r requiredPackages.txt
  - then in same directory on command line, type:
    - . venv/bin/activate
  - then you can run the project by typing:
    - python routes.py

  - to see the project in browser go to:
    - localhost:8000
      - to change port, go to ~line: 77 and change the var
      - make sure to let us know if its changed


### Postgress (mac):
  - [download This](https://postgresapp.com/documentation/all-versions.html)
  - just do this:
    - `sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp`

### (window):
  - [instructions](https://www.postgresql.org/download/windows/) here
  - follow similar instructions as given below for general steps
    - you may have to add psql to your path environment variables

### (ubuntu):
  - follow [these](https://www.postgresql.org/download/linux/ubuntu/) instructions
  - in our active directory there is a db.sql file
  - make sure your psql server is running, then in terminal type:
    - `postgres -D /usr/local/pgsql/data`
    - `psql < db.sql`
  - then the database should be created and you can interact with it through the website in localhost

#### general steps to get database setup:
  - when you clone or pull the repo you should have a <filename>.db file in the directory
  - make sure you have a postgres server, and the server is running.
    - Instructions found [here](https://www.postgresql.org/download/)
  - dependant on your postgress server installation:
    - you'll have command line commands to import a database table
    - for ex. on mac -> we install the app above and in terminal run:
      - `psql < db.sql`
    - this creates the DB and tables necessary
