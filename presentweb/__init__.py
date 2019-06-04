from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'enter-your-mail',
	MAIL_PASSWORD = 'enter-your-password^'
	)
mail = Mail(app)


@app.route("/")
def helloworld():
    return "Hello World"

@app.route('/send-mail/')
def send_mail():
	try:
		msg = Message("Send Mail Tutorial!",
		  sender="enter-your-mail",
		  recipients=["where-to-send"])
		msg.body = "Sending mail test"           
		mail.send(msg)
		return 'Mail sent'
	except Exception as e:
		return(str(e)) 