import socket


def run_server(host="10.156.147.138", port=5000):
    with socket.socket() as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        msg = conn.recv(1024)
        print(f'{msg.decode()}')
        conn.sendall(msg)
        conn.close()


if __name__ == '__main__':
    while(1):
        run_server()