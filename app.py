import os, smtplib
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, JWTManager
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET')
jwt = JWTManager(app)

#CORS(app)    # => allow all! 
# OBS ingen trailing / på urlar!
CORS(app, origins=["http://127.0.0.1:5500", "https://people.arcada.fi"])

@app.route("/")
def index():
    ret = {'msg': 'This is the email service.', 'v': 3}
    return ret

@app.route("/sendmail", methods = [ 'POST' ])
@jwt_required()
def send():
    """ POST send email
        See https://docs.csc.fi/cloud/rahti/tutorials/email/ for instructions"""
    ret = {'smtp': os.environ.get('MAIL_SMTP')}

    req = request.get_json()
    mail_from = os.environ.get('MAIL_FROM')
    mail_to = [req['to']]


    # Make sure TO-domain is allowed (skip this step when JWT is implemented)
    if not mail_to[0].endswith(os.environ.get('ALLOWED_MAILDOMAIN')):
        return { 'error': 'Forbidden recipient address' }, 403

    # Note: "Sender" header is required in the rahti manual
    msg = "From: {}\r\nTo: {}\r\nSender: {}\r\nSubject: {}\r\n\r\n{}".format(
        mail_from, 
        mail_to[0], 
        mail_from, 
        req['subject'], 
        req['body'])

    try:
        smtp_obj = smtplib.SMTP(os.environ.get('MAIL_SMTP'))
        smtp_obj.sendmail(mail_from, mail_to, msg)

        print(f"Mail sent from {mail_from} to {mail_to[0]} using {os.environ.get('MAIL_SMTP')}")
        ret = {'msg': 'Mail sent'}

    except Exception as e:
        print(e)
        ret =  {'error': 'Mail fail.'}, 500
    
    return ret

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
