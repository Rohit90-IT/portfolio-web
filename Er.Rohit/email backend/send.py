from flask import Flask, request, render_template_string

import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_ADDRESS = 'it.rohit9019@gmail.com'
EMAIL_PASSWORD = 'hsbb mana nbjg faqi'

@app.route('/')
def home():
    # Ideally serve your full HTML page here or just redirect to the static file or template.
    return "Go to your website page with the form."

@app.route('/submit-email', methods=['POST'])
def submit_email():
    user_email = request.form['email']

    msg = EmailMessage()
    msg['Subject'] = 'New Email Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"You received a new email: {user_email}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return "Thank you! Your email has been sent."
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
