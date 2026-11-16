# Final project

The Emotion Detector is a Flask app that uses IBM Watson NLP to score anger, disgust, fear, joy, and sadness and report the dominant emotion.

## Run in Skills Network Labs

```sh
python3 -m pip install -r requirements.txt
python3 server.py
```

Open port 5000 in the lab to use the form. The app and its integration tests require access to the Skills Network Watson NLP endpoint.

```sh
python3 -m unittest -v
```
