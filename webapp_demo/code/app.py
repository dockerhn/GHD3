from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

server_name = ''
with open('/etc/hostname') as f:
    server_name = f.read()

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen {} times.'.format(redis.get('hits').decode('utf-8'))

@app.route('/server-name')
def get_server_name():
    return server_name

if __name__ == "__main__":
    app.run(host="0.0.0.0")

