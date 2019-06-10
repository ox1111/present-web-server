from flask import Flask, request
from flask_mail import Mail, Message
import config

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = config.EMAIL_CONFIG['email'],
	MAIL_PASSWORD = config.EMAIL_CONFIG['password']
	)
mail = Mail(app)


@app.route("/")
def helloworld():
    return "Hello World"

@app.route('/send-mail/', methods=["POST"])
def send_mail():
	try:
		msg = Message("Send Mail Tutorial!",
		  sender=config.EMAIL_CONFIG['email'],
		  recipients=[request.form['email']])
		msg.body = request.form['content']
		mail.send(msg)
		return 'Mail sent'
	except Exception as e:
		return(str(e)) 

if __name__ == "__main__":
    app.run(host="0.0.0.0")