## DG Putter Pro

Disc Golf Putting practice app written in python using Flask

This app is not currently deployed anywhere. 
### To work on it locally:
1. clone this repo and navigate to that directory
2. create a virtual environment `python3.10 -m venv venv`
3. activate virtual environment `source venv/bin/activate`
4. upgrade pip inside active venv `python -m pip install --upgrade pip`
5. Prior to installing requirements install wheel `python -m pip install wheel`
6. Install requirements `python -m pip install -r requirements.txt`

### To run locally
`docker-compose up --build`

### Stop and remove containers

`docker-compose down` or `docker-compose down -v` to remove named volumes also.
in either case you will lose any saved data, so probably might as well remove the volume.


### What's currently working

0. basic database models for User and putting Drill
1. register user
2. login user
3. send reset user password email
4. reset user password
5. logging to file
6. sending logs to email
7. allow user to record putting drill
8. display putting drills on user page
9. crude stats summary page
10. Docker 
    

### TODO to get to version 0.0.0.0.0.0.0.1

[x] - email support for password reset

[x] -prettify datetimes and handle timezones (flask-moment)

[x] - logging

[ ] - testing

[x] - refactor to use blueprints and app factory pattern

[x] - styles

[ ] - expose API

[ ] - visualizations for user progress

[X] - provision a real DB: postgres

[X] - Containerization

[ ] - Deployment

  