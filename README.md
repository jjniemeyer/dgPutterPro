## DG Putter Pro

Disc Golf Putting practice app written in python using Flask

This app is not currently deployed anywhere. 
To run it locally:
1. clone this repo and navigate that directory
2. create virtual environment `python3 venv venv`
3. Install requirements `pip install -r requirements.txt`
4. run the app on localhost port 5000 `flask run`
5. point browser to `http://localhost:5000`

### What's currently working

0. basic database models for User and putting Drill
1. register user
2. login user
3. allow user to record putting drill
4. display putting drills on user page
    

### TODO to get to version 1.0

[ ] - email support for password reset
[ ] - logging
[ ] - testing
[ ] - refactor to use blueprints and app factory pattern
[ ] - stylesheets
[ ] - visualizations for user progress
[ ] - Containerization
    [ ] - Dockerize this app
    [ ] - provision and persist MySQL container
[ ] - Deployment
    [ ] - decide where? (AWS, Google cloud, or Linode)
    [ ] - set up a CI/CD workflow