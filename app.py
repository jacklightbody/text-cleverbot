# File: app.py
# Author: jack
# Created at:   2017-01-15 
# Modified at:   2017-01-16
import os
import plivo
import logging

from sms_adapter import SmsAdapter
from flask import Flask, render_template, request, redirect
from cleverbot import Cleverbot
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False
logging.basicConfig(filename='notifier_errors.log',level=logging.INFO)


sms = SmsAdapter()
@app.route("/notifier/receive_sms", methods=['GET','POST'])
def receive_sms():
    recipient, sender, message = sms.receive(request)
    cb = Cleverbot()
    response = cb.ask(message)
    sms.send(sender, recipient, response)
    return response

if __name__ == '__main__':
    app.run()