# Reddit Sarcasm Detector

An ML model developed for the purpose of detecting sarcasm in texts using training data from Reddit

Requirements are specified in the requirements.txt file, please run

```
pip install -r requirements.txt
```

This is a dockerized version of the application, run it on docker using

```
docker compose up -d
```
in the bash shell

The weights of the model are available here - 

```
https://huggingface.co/MadElf1337/reddit_sarcasm_lstm/blob/main/hope.h5
```

Make sure to add the .h5 file to `models/`
