# Flask Sentiment Analysis Application

This is a Flask web application that predicts the sentiment of a given message using a pre-trained machine learning model.

## Description

This application provides a web interface to input a message and get a sentiment prediction. The model used for prediction is a Logistic Regression model stored in a pickle file.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```


## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Endpoints

- **GET /**: Renders the home page.
- **POST /predict**: Accepts a message and returns the sentiment prediction.

## Example

To use the `/predict` endpoint, you can use the following `curl` command:

```bash
curl -X POST -F 'message=Your message here' http://127.0.0.1:5000/predict
