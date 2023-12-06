# NLP Microservice API Documentation

## Introduction

The NLP Microservice provides various natural language processing (NLP) functionalities through RESTful APIs. The available functionalities include text tokenization, sentiment analysis, named entity recognition, and part-of-speech tagging.

## Base URL

The base URL for the API is `http://localhost:5000`.

## Endpoints

### 1. Tokenize Text

#### Endpoint

POST /tokenize


#### Description

Tokenizes the provided text.

#### Request

- **Method**: POST
- **Content Type**: application/json

#### Request Body

json
{
  "text": "The input text to tokenize."
}
Responses
200 OK

Successful response containing the tokenized text.

Example:

json

{
 "tokens": ["The", "input", "text", "to", "tokenize", "."]
}
2. Sentiment Analysis
Endpoint
bash
Copy code
POST /sentiment
Description
Analyzes the sentiment of the provided text.

Request
Method: POST
Content Type: application/json
Request Body
json
{
  "text": "The input text for sentiment analysis."
}
Responses
200 OK

Successful response containing the sentiment analysis result.

Example:

json
{
  "sentiment": "positive",
  "polarity": 0.5,
  "subjectivity": 0.6
}
3. Named Entity Recognition (NER)
Endpoint
bash
Copy code
POST /ner
Description
Performs Named Entity Recognition (NER) on the provided text.

Request
Method: POST
Content Type: application/json
Request Body
{
  "text": "The input text for named entity recognition."
}
Responses
200 OK

Successful response containing the NER result.

Example:

{
  "entities": [
    {"text": "John Doe", "label": "PERSON"},
    {"text": "New York", "label": "GPE"}
  ]
}
4. Part of Speech (POS) Tagging
Endpoint

POST /pos

Description
Performs Part of Speech (POS) tagging on the provided text.

Request
Method: POST
Content Type: application/json
Request Body

{
  "text": "The input text for part of speech tagging."
}
Responses
200 OK

Successful response containing the POS tagging result.

Example:

{
  "pos_tags": [
    {"text": "The", "pos": "DET"},
    {"text": "input", "pos": "NOUN"},
    {"text": "text", "pos": "NOUN"},
    {"text": "for", "pos": "ADP"},
    {"text": "part", "pos": "NOUN"},
    {"text": "of", "pos": "ADP"},
    {"text": "speech", "pos": "NOUN"},
    {"text": "tagging", "pos": "NOUN"},
    {"text": ".", "pos": "PUNCT"}
  ]
}
Error Handling
In case of an error, the API will return an appropriate HTTP status code along with a JSON object containing details about the error.

400 Bad Request: Invalid request or missing required parameters.

Example:

{
  "error": "Bad Request",
  "message": "Missing 'text' parameter in the request body."
}
500 Internal Server Error: An unexpected error occurred on the server.

Example:

{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred while processing the request."
}
