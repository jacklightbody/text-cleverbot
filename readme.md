# Text Cloverbot

Text cleverbot is a simple flask based app to allow you to communicate with the [cleverbot](http://www.cleverbot.com) chat bot via texting. 

### Installation
After cloning the repo, first install the required packages with 

	pip install -r requirements.txt
	
Next, configure plivo by setting the auth id and auth token in plivo_adapter.py. These values can be found at the [plivo dashboard](https://manage.plivo.com/dashboard/) once you have signed up for an account. 

Then you can run a simple server with 
	
	# For macs
	export FLASK_APP=app.py 
	# For windows
	set FLASK_APP=app.py
	flask run
	
To have a conversation with cleverbot, just text the number you bought from plivo and you should receive a response from cleverbot.

### Deployment
Flask has good documentation on deploying flask apps with [mod_wsgi](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)

### Testing 
If you want to test before going live, switch to using the dummy\_adapter. Directions on how to do so can be found in sms_adapter.py

### Extending
If you want to use a sms service other than plivo, use the dummy adapter and plivo adapter files as a starting point. The two method signatures that are neccessary to implement are 

	send(recipient, sender, message) -> void
	receive(request) -> recipient, sender, message
	
Where recipient and sender are phone numbers, and request is a [flask request](http://flask.pocoo.org/docs/0.12/api/#incoming-request-data)