NLP Microservice

Overview

NLP Microservice is a backend application that provides Natural Language Processing (NLP) functionalities through RESTful APIs. The service can perform text tokenization, sentiment analysis, named entity recognition, and part-of-speech tagging. This project is open-sourced under the MIT License and is hosted on GitHub.

 Features

- Text Tokenization : Split input text into individual tokens.
- Sentiment Analysis : Determine the sentiment (positive, negative, or neutral) of the input text.
- Named Entity Recognition (NER) : Identify entities (e.g., names, organizations) in the input text.
- Part-of-Speech (POS) Tagging : Assign grammatical parts of speech to words in the input text.

Technology Stack

- Python
- Flask (Web framework)
- NLTK and TextBlob (NLP libraries)
- Other dependencies (see requirements.txt)

Setup Instructions

Requirements:

1. Python: Ensure that Python is installed on your system.
2. Pip (Python package installer): Verify that Pip is installed. If not, you can install it with the Python package.

Clone the Repository:

Copy the Git link: `https://github.com/vinay596/nlp-microservice.git`

Use VS Code or any preferred Git client to clone the repository. Paste the URL and select "Clone from URL."

Install Required Modules:

Open the command prompt and execute the following commands:

pip install flask
pip install flask_cors
pip install textblob
pip install spacy


How to Run  Application :

Follow these steps to set up and run the NLP Microservice on your local machine:

Step 1: Clone the Repository
git clone https://github.com/vinay596/nlp-microservice.git
cd nlp-microservice


Step 2: Install Dependencies
Make sure you have Python installed. Then, install the required modules:
pip install -r requirements.txt


Step 3: Configure Environment Variables
Create a .env file in the root directory and configure any necessary environment variables. For example:
env
Copy code
FLASK_APP=app.py
FLASK_ENV=development


Step 4: Run the Application
flask run


This will start the Flask development server. Open your web browser and navigate to http://localhost:5000 to access the NLP Microservice.


API Endpoints
The NLP Microservice provides the following API endpoints:

Text Tokenization: http://localhost:5000/tokenize

Method: POST
Payload: {"text": "Your input text here"}
Sentiment Analysis: http://localhost:5000/sentiment

Method: POST
Payload: {"text": "Your input text here"}
Named Entity Recognition (NER): http://localhost:5000/ner

Method: POST
Payload: {"text": "Your input text here"}
Part-of-Speech (POS) Tagging: http://localhost:5000/pos

Method: POST
Payload: {"text": "Your input text here"}

