# Server 

import zmq

PORT = 1488

context = zmq.Context()  # Create zmq ctx
socket = context.socket(zmq.REP)  # Create RESPONSE socket
socket.bind(f"tcp://*:{PORT}")  # Bind to port

while True:
    message = socket.recv_string()  # Receive something
    print(f"Received request: {message}")  # Print it
    socket.send_string("YOU ^_^")  # Send response


# Client

import zmq

PORT = 1488

context = zmq.Context()  # Create a context
socket = context.socket(zmq.REQ)  # Create REQUEST socket
socket.connect(f"tcp://127.0.0.1:{PORT}")  # Connect to TCP

socket.send_string("TNKAN")  # Send something
resp = socket.recv_string()  # Receive response
Pub-Sub

 
# PUBLISHER  
import zmq
import time

PORT = 1488
TOPIC = " J"

context = zmq.Context()
socket = context.socket(zmq.PUB)  # Create PUB socket
# IF YOU NEED MANY-TO-ONE (many pubs to one sub) - USE THIS
socket.connect(f"tcp://localhost:{PORT}")
# IF YOU NEED ONE-TO-MANY (one pub to many subs) - USE THIS
socket.bind(f"tcp://*:{PORT}")

while True:
    msg = f"Hy npNBET"
    socket.send_string(f'{TOPIC} {msg}')  # Send string with topic
    print(f'Sent: {msg}')
    time.sleep(1)
Subscriber (sub)


# SUBCRIPER  
import zmq

PORT = 1488
TOPIC = "J"

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, TOPIC)  # Set topic filter
# IF YOU NEED MANY-TO-ONE (many pubs to one sub) - USE THIS
socket.bind(f"tcp://*:{PORT}")
# IF YOU NEED ONE-TO-MANY (one pub to many subs) - USE THIS
socket.connect(f"tcp://localhost:{PORT}")

while True:
    topic, msg = socket.recv_string().split(TOPIC)
    print(f'Received: {msg}')





