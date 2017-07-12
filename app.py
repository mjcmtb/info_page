from flask import Flask, request
import time, subprocess, socket
app = Flask(__name__)


@app.route('/')
def hello():



    msg = """<html>
            <body>

            <h1>Hello ZestFinance!!!</h1>

            <p>Node IP: {}</p>
            <p>Caller IP: {}</p>
            <p>Timestamp: {}</p>

            </body>
            </html>""".format(get_interface_ip(),request.remote_addr,get_dt())

    return msg

def get_dt():

    return time.strftime("%Y-%m-%d %H:%M:%S")

def get_interface_ip():
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    app.run()