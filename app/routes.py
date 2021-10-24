from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Soon to be home of Dg Putter Pro!"