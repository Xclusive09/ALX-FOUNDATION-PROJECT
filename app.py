from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.debug = True

# Email Configuration
sender_email = 'your_email@example.com'
receiver_email = 'abdulquddus51@gmail.com'
subject = 'Contact Form Submission'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_smtp_username'
smtp_password = '@Xclusive09'

def send_email(name, email, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Create the HTML message
    body = f'''
    <h3>Contact Form Submission</h3>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong> {message}</p>
    '''

    msg.attach(MIMEText(body, 'html'))

    # Setup SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    print("Email sent successfully!")

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        send_email(name, email, message)
        
        return 'Email sent successfully!'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
