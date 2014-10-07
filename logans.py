from flask import Flask, url_for, render_template
from flask.ext import restful
from random import randint

app = Flask(__name__)
api = restful.Api(app)

names = ['Logan', 'Jennifer', 'Richard', 'Sam', 'Rumel', 'Rob', 'Alison']

class GenerateName(restful.Resource):
    def get(self):
        name = names[randint(0,6)] + ' ' + str(randint(1,30))
        return {'name': name}

@app.route('/')
def home():
    return render_template('home.html')

api.add_resource(GenerateName, '/generate')

if __name__ == '__main__':
    app.run(debug=True)