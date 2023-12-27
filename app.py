from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import spacy
from textblob import TextBlob

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tokenize', methods=['POST'])
def tokenize():
    text = request.json['text']
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return jsonify({'tokens': tokens})

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json['text']
    blob = TextBlob(text)
    sentiment = 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
    return jsonify({'sentiment': sentiment, 'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity})

@app.route('/ner', methods=['POST'])
def named_entity_recognition():
    text = request.json['text']
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return jsonify({'entities': entities})

@app.route('/pos', methods=['POST'])
def part_of_speech():
    text = request.json['text']
    doc = nlp(text)
    pos_tags = [{'text': token.text, 'pos': token.pos_} for token in doc]
    return jsonify({'pos_tags': pos_tags})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
