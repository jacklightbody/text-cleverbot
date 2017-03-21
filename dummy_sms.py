# File: dummy_sms.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-03-20

class DummySms: 

	def send(self, recipient, sender, message):
		print("Recipient: "+recipient)
		print("Sender: "+sender)
		print("Message: "+message)

	def receive(self, request):
		message = "Message"
  		sender = "From"
  		recipient = "To"
  		return recipient, sender, message