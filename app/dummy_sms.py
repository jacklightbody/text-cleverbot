# File: dummy_sms.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-01-15

class DummySms: 

	def send(self, recipient, sender, message):
		print("recipient: "+recipient)
		print("sender: "+sender)
		print("message: "+message)

	def receive(self, request):
		message = "message"
  		sender = "from"
  		recipient = "to"
  		return recipient, sender, message