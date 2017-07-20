from flask import Flask, request
import time, subprocess, socket
app = Flask(__name__)

@app.route('/')
def hello():

    try:
        source_ip = request.headers.getlist("X-Forwarded-For")[0]
    except:
        source_ip = request.remote_addr

    if source_ip == "127.0.0.1":
        source_ip = request.remote_addr

    msg = """<html>
            <body>

            <h1>Hello ZestFinance!!!</h1>

            <p>Node IP: {}</p>
            <p>Caller IP: {}</p>
            <p>Timestamp: {}</p>

            </body>
            </html>""".format(get_interface_ip(),source_ip,get_dt())

    return msg

def get_dt():

    return time.strftime("%Y-%m-%d %H:%M:%S")

def get_interface_ip():
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
