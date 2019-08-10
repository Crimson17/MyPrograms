import socket, time

print("Send 'q' if you want to stop the server!")

message = ""

HOST = '192.168.1.9'
PORT = 1709

while message != "q":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Input your message: ")
        s.sendall(str.encode(message))
        time.sleep(1)
