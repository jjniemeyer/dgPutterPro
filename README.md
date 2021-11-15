## DG Putter Pro

Disc Golf Putting practice app written in python using Flask

This app is not currently deployed anywhere. 
To run it locally:
1. clone this repo and navigate to that directory
2. create a virtual environment `python3 -m venv venv`
3. activate virtual environment `source venv/bin/activate`
4. Prior to installing requirements install wheel `python3 -m pip install wheel`
5. Install requirements `python3 -m pip install -r requirements.txt`
6. run the app on localhost port 5000 `flask run`
7. point browser to `http://localhost:5000`

### What's currently working

0. basic database models for User and putting Drill
1. register user
2. login user
3. allow user to record putting drill
4. display putting drills on user page
5. crude stats summary page
    

### TODO to get to version 0.1

[x] - email support for password reset

[x] -prettify datetimes and handle timezones (flask-moment)

[x] - logging

[ ] - testing

[x] - refactor to use blueprints and app factory pattern

[x] - styles

[ ] - visualizations for user progress

[ ] - Containerization

    [ ] - Dockerize this app

    [ ] - provision and persist MySQL container

[ ] - Deployment

    [ ] - decide where? (AWS, Google cloud, or Linode)

    [ ] - set up a CI/CD workflow
