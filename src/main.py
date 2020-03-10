"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Users, Quizes, Questions

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200


@app.route('/newuser',methods=['POST'])
def register():

    json = request.get_json()
    user = Users(
        email = json["email"],
        password = json["password"]
    )
    db.session.add(user)
    db.session.commit()
    return 'Welcome , fellow bender'


@app.route('/upload/quiz', methods=['POST'])
def upload_quiz():

    json = request.get_json()

    quiz = Quizes(
        name = json['name']
    )
    db.session.add( quiz )
    db.session.flush()

    for x in json['questions']:
        db.session.add( Questions(
            quiz_id = quiz.id,
            question = x['question'],
            a = x['options']['a'],
            b = x['options']['b'],
            c = x['options']['c'],
            d = x['options']['d']
        ))

    db.session.commit()
        



@app.route('/login', methods=['Post'])
def login():
    
    json = request.get_json()

    user = Person.query.filter_by(
        email = json['email'],
        password = json['password']
    ).first()

    if user is None:
        raise APIException('Bender not found',404)

    return 'Welcome back, we missed you'



@app.route('/quiz')
def quiz():

    quiz = [
        {
            "question": 'Which of these animals would you have as a mentor and a friend?',
            "options:": {
                '1': 'Dragons',
                '2': 'Flying bison',
                '3': 'Badger moles ',
                '4': 'Koi fish',
            }
        },
        {
            'question': '.  Which martial arts style would you practice?',
            "options": {
                '1': 'Eight trigram',
                '2': 'Hung gar style K.F',
                '3': 'Northern shaolin style',
                '4': 'Tai chi  ch’uan',
            }
        },
        {
            'question': 'What do you value more?',
            "options": {
                '1': 'Power',
                '2': 'spiritual enlightenment',
                '3': 'Strength',
                '4': 'compassion',
            }
        },
         {
            "question": 'How would you describe yourself?',
            "options:": {
                '1': 'Focused',
                '2': 'Free-spirited',
                '3': 'Dynamic',
                '4': 'Strong',
            }
        },
        {
            'question': 'What is most important to you?',
            "options": {
                '1': 'Knowledge',
                '2': 'Freedom',
                '3': 'Harmony',
                '4': 'Stability',
            }
        },
        {
            'question': 'Which special ability do you desire the most?',
            "options": {
                '1': 'Healing',
                '2': 'Flight',
                '3': 'Seismic Sense',
                '4': 'Lightning Generation',
            }
        },
         {
            "question": 'What is the ideal society?',
            "options:": {
                '1': 'Capitalist ',
                '2': 'Monarchist',
                '3': 'Tribal',
                '4': 'Nomadic',
            }
        },
        {
            'question': 'You’re under attack! How do you win?',
            "options": {
                '1': 'Strength',
                '2': 'Agility',
                '3': 'Intelligence',
                '4': 'Courage',
            }
        },
        {
            'question': 'Which dangerous place would you rather visit?',
            "options": {
                '1': 'The Artic',
                '2': 'volcano',
                '3': 'The Sahara ',
                '4': 'Mount Everest ',
            }
        },
         {
            "question": 'Are you more?',
            "options:": {
                '1': 'Clever ',
                '2': 'family-oriented',
                '3': 'Insightful',
                '4': 'strong willed ',
            }
        },
        {
            'question': 'I see myself as a?',
            "options": {
                '1': 'Unifier	',
                '2': 'expand-er',
                '3': 'Identifier',
                '4': 'stabiliser',
            }
        },
        {
            'question': 'What does your Zodiac sign stand for?',
            "options": {
                '1': 'fire',
                '2': 'Water',
                '3': 'Earth',
                '4': 'Wind',
            }
        },
         {
            "question": 'You would most want to be part of?',
            "options:": {
                '1': 'close and connected community',
                '2': 'strong and diverse population',
                '3': 'proud and powerful nation',
                '4': 'spiritually enlightened society',
            }
        },
        {
            'question': 'What hobby would you like to participate in?',
            "options": {
                '1': 'gardening',
                '2': 'reading ',
                '3': 'skydiving ',
                '4': 'camping ',
            }
        },
        {
            'question': 'Which of the following is your worst trait?',
            "options": {
                '1': 'extremely sensitive',
                '2': 'Can be very lethargic',
                '3': 'I can be quite stubborn',
                '4': 'can be quite temperamental',
            }
        },
         {
            "question": 'You are standing on a cliff facing the sea, at sunset, with a forest behind you. What do you first notice?',
            "options:": {
                '1': 'sea and the powerful waves',
                '2': 'wind blowing through your hair ',
                '3': 'soil beneath your feet',
                '4': 'suns fiery rays throwing light on everything',
            }
        },
   
    ]






    

    return jsonify(quiz)



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
