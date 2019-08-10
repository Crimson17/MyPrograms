import socket, time

print("Send 'q' if you want to stop the server!")

i = 0
HOST = '192.168.1.9'
PORT = 1709

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()

    while True:
        acceptedSOCKET, acceptedADDRESS = s.accept()
        data = acceptedSOCKET.recv(1024)

        print(data.decode())

        if data.decode() == "q":
            break
        time.sleep(0.2)
