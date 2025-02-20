from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your full name
    full_name = "Mahamad Sakeeb M Gadyal"
    
    # Get the system username
    try:
        system_username = os.getlogin()
    except Exception:
        system_username = "PES2UG21CS266"
    
    # Get the server time in IST
    # Note: Adjust if your server is not set to IST; this is a simple example
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    server_time = now.strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get the output of the top command
    top_output = subprocess.getoutput("top -b -n 1")
    
    return f"""
    <html>
      <head><title>System Info</title></head>
      <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <pre>{top_output}</pre>
      </body>
    </html>
    """

# Optional: Add a home route for convenience
@app.route('/')
def home():
    return "<h1>Welcome</h1><p>Visit <a href='/htop'>/htop</a> to see system info.</p>"

if __name__ == '__main__':
    # Run the app on all addresses (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
