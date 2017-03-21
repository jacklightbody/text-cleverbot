# File: sms_adapter.py
# Author: jack
# Created at:   2017-01-15
# Modified at:   2017-03-20
# Purpose of this file is to abstract away some of the sending functionality from main
# So that if we need to switch providers we can do so painlessly
from plivo_adapter import PlivoAdapter
from dummy_sms import DummySms
class SmsAdapter:
	def __init__(self):
		# self.provider = DummySms()
		# For testing use, uncomment the above and comment the following
		self.provider = PlivoAdapter()

	def send(self, recipient, sender, message):
		self.provider.send(recipient, sender, message)

	def receive(self,request):
		return self.provider.receive(request)