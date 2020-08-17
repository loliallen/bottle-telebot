import datetime

from bottle import post, request, route, run

from telegram import Bot

tbot = Bot()
tbot.start()
def message_template(data):
    return """
    {1}:\t{2}\n
    u_id:\t{3}\n
    w_id:\t{4}\n
    h_id:\t{5}\n
    """.format(datetime.datetime.now().time(), data.location, data.u_id, data.w_id, data.h_id)

@post('/upload')
def hello():
    data = {}
    data.w_id = request.forms.get('w_id')
    data.u_id = request.forms.get('u_id')
    data.h_id = request.forms.get('h_id')
    img = request.files.get('image')

    tbot.sendMsg(ID, message_template(data))
    tbot.sendPhoto(ID, img);
    return "Hello WOrld!"

run(host="localhost", port="8080", debug="TRUE")
