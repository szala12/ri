import flask
from flask_socketio import SocketIO, emit, send, disconnect
from flask import Flask, render_template, redirect, request
import os
import json
import pymongo
import re
from module import chat

app = Flask(__name__)
app.config['SERVER_URL'] = os.environ.get('SERVER_URL', "http://localhost:5000//")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY","wellthisisbadandyouknowit")
socketio = SocketIO(app)

@app.route('/bot')
def serve_bot_page(methods=["GET"]):
    if request.method == "GET":
        print("fetching bot page template")
        bot_load_data = {}
        bot_load_data["SERVER_URL"] = app.config["SERVER_URL"]
        return render_template('bot.html',bot_load=bot_load_data)

@socketio.on('message')
def handle_message(message):
    chat.handle_message_text(message)
    send(message)

def main():
    print("booting up the bot babey")
    socketio.run(app, use_reloader=True)

if __name__ == '__main__':
    main()