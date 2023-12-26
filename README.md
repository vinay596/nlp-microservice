# NLP Microservice

## Overview

NLP Microservice is a backend application that provides Natural Language Processing (NLP) functionalities through RESTful APIs. The service can perform text tokenization, sentiment analysis, named entity recognition, and part-of-speech tagging. This project is open-sourced under the MIT License and is hosted on GitHub.

## Features

- **Text Tokenization:** Split input text into individual tokens.
- **Sentiment Analysis:** Determine the sentiment (positive, negative, or neutral) of the input text.
- **Named Entity Recognition (NER):** Identify entities (e.g., names, organizations) in the input text.
- **Part-of-Speech (POS) Tagging:** Assign grammatical parts of speech to words in the input text.

## Technology Stack

- Python
- Flask (Web framework)
- NLTK and TextBlob (NLP libraries)
- Other dependencies (see requirements.txt)

## Setup Instructions

### Prerequisites:

1. **Python:** Ensure that Python is installed on your system.
2. **Pip (Python package installer):** Verify that Pip is installed. If not, you can install it with the Python package.

### Clone the Repository:

Copy the Git link: `https://github.com/vinay596/nlp-microservice.git`

Use VS Code or any preferred Git client to clone the repository. Paste the URL and select "Clone from URL."

### Install Required Modules:

Open the command prompt and execute the following commands:

```bash
pip install flask
pip install flask_cors
pip install textblob
# Add any other dependencies mentioned in requirements.txt
