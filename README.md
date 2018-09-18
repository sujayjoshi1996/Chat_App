# FreeChat
This is a simple chat application where people can create their login credentials, create channel, join channels and start chatting
The index.html page consists of 4 forms 1st to create the user name, 2nd create channel, 3r select channal and last one to send message to that channel
Application.py page requests the user name, channel creation request and selected channel, also creates the new channel.
The index.js page saves the username locally so the the user no need to type every time.
Then using websockets there is communication between server(application.py) and client(js and html pages)
