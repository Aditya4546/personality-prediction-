from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # Needed for local development
from model import run_personality_prediction

app = Flask(__name__)
# This is crucial for allowing your HTML/JS on one port to talk to Flask on another.
CORS(app) 

# --- NEW ROOT ROUTE ---
@app.route('/', methods=['GET'])
def serve_index():
    # This tells Flask to look for 'index.html' in the same directory and serve it
    return render_template('index.html')

# This route handles POST requests with the form data
@app.route('/predict_personality', methods=['POST'])
def predict_personality():
    # 1. Get the JSON data sent from the website
    data = request.get_json()
    
    # 2. Extract the 7 inputs
    gender = data.get('gender')
    age = data.get('age')
    openness = data.get('openness')
    neuroticism = data.get('neuroticism')
    conscientiousness = data.get('conscientiousness')
    agreeableness = data.get('agreeableness')
    extraversion = data.get('extraversion')
    print(gender , age, openness, neuroticism, conscientiousness, agreeableness ,extraversion)

    #calls the run_personality_prediction fun from model.py
    predicted_personality =  run_personality_prediction(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion)
    
    # Return the result as a JSON object



    return jsonify({
        'predicted_personality': predicted_personality[-1]
    })

if __name__ == '__main__':
    # Run the server on http://127.0.0.1:5000/
    app.run(debug=True)