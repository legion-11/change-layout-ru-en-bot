# Change layout ru-en bot

Corrects selected messages with the wrong layout (eng -> ru / ru -> eng).

## How to start

Create and activate a virtual environment

```commandline
virtual venv --python=python3.7
source venv/bin/activate
```
Install the required modules
```commandline
pip install flask
pip install pyTelegramBotAPI
```
Set environment variables
```commandline
set FLASK_APP=run_bot.py
set TOKEN=<your-token>
```
Set the tunnel to localhost (https://ngrok.com/download)
```commandline
ngrok http 5000
set HOST_URL=<your-tunnel-url>
```
Run flask on localhost
```commandline
flask run
```