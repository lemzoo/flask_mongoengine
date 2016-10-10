# http://docs.mongoengine.org/tutorial.html
from mongoengine import *
from flask import Flask

from model import User
from model_api import Comment
from model_api import Post
from model_api import ImagePost
from model_api import LinkPost

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

if __name__ == '__main__':
    app.run(debug=True)


connect('tumblelog')
ross = User(email='ross@example.com',
			first_name='Ross',
			last_name='Lawley'
			)
ross.save()