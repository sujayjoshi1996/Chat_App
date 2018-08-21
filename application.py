import os

from flask import Flask,render_template, jsonify, request
from flask_socketio import SocketIO, emit, leave_room, join_room
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#  create a list to hold channel name, messages and the user name
channel_list=[]
# data={"list":{"channels":channel_list,
                # "messages":[]
                # "user1":[]
        # } }

@app.route("/", methods=["Post","GET"])
def index():

 # to display the channels which already exists

        if request.method == "POST":
      # get user name and password entered by the user
            user = request.form.get("usr")
            channel = request.form.get("channel")
            cselect = request.form.get("cselect")
          # check if channel already exists, if doesnt add channel
          # and switch to taht channel
            for chl in channel_list:
                    if (str(channel) != str(chl)):
                            channel_list.append(channel)
        elif request.method == "GET":
            return render_template("index.html",channel_list=channel_list,cselected=cselect)
        else:
                return jsonify({"success":False})

@socketio.on("submit vote")
def vote(data):
    selection = data["msg"]
    emit("announce message", {"selection": msg}, broadcast=True)



if __name__=='__main__':
    socketio.run(app,debug=True)
