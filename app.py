from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from textblob import TextBlob
import spacy

app = Flask(__name__)
CORS(app)
nlp = spacy.blank("en")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tokenize', methods=['POST'])
def tokenize():
    text = request.json['text']
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return jsonify({'tokens': tokens})

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (-1 to 1) and subjectivity (0 to 1)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    # Classify sentiment based on polarity
    if sentiment_polarity > 0:
        sentiment = 'positive'
    elif sentiment_polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, sentiment_polarity, sentiment_subjectivity

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json['text']
    sentiment_result, polarity, subjectivity = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment_result, 'polarity': polarity, 'subjectivity': subjectivity})

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
