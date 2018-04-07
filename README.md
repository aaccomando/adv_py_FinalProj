# Development

### to setup the environment (through command line):
  - first clone the repository
    - git clone "URL"
  - inside the main directory( adv_py_FinalProj ) run:
    - pip install -r requirments.txt
    - pip install -r requiredPackages.txt
  - then in same directory on command line, type:
    - . venv/bin/activate
  - then you can run the project by typing:
    - python routes.py

  - to see the project in browser go to:
    - localhost:5000


### Postgress (mac):
  - [download This](https://postgresapp.com/documentation/all-versions.html)
  - just do this:
    - sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
### (window):
  - finding alternatives ..
### (ubuntu):
  - finding alternatives ..
#### general steps to get database setup:
  - when you clone or pull the repo you should have a <filename>.db file in the directory
  - make sure you have a postgress server, and the server is running.
  - create a database and call it -> foodDB
  - dependant on your postgress server installation:
    - you'll have command line shit to import a database table
    - for ex on mac -> we install the app above and in terminal run:
      - psql "databaseName" < db.sql
      - remove quotes above
    - this creates and updates the DB so we all have the same crap
