from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS # CORS
import config

app = Flask(__name__)
app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = config.EMAIL_CONFIG['email'],
	MAIL_PASSWORD = config.EMAIL_CONFIG['password']
	)
CORS(app) # CORS
mail = Mail(app)


@app.route("/")
def helloworld():
    return "Hello World"

@app.route('/send-mail/', methods=["POST"])
def send_mail():
	try:
		msg = Message(request.form['subject'],
		  sender='('+request.form['name']+')'+request.form['email'],
		  recipients=[config.EMAIL_CONFIG['email']])
		msg.body = request.form['message']
		mail.send(msg)
		return 'Mail sent'
	except Exception as e:
		return(str(e)) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)