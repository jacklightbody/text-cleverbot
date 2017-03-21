# File: plivo_adapter.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-01-15
import os
import plivo
class PlivoAdapter: 
	api = plivo.RestAPI(os.getenv('PLIVO_AUTH_ID', ''), os.getenv('PLIVO_AUTH_TOKEN', ''))

	def send(recipient, sender, message):
		api.send_message(message_params = {
	        'src':sender,
	        'dst':recipient,
	        'text':message,
	      })
	def receive(request):
		message = request.values.get('Text')
  		sender = request.values.get('From')
  		recipient = request.value.get('To')
  		return recipient, sender, message