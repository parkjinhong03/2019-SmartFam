import socket


def socket_send(a):
    with socket.socket() as s:
        bin_a = a.encode('utf-8')
        s.connect(('10.156.147.199', 7000))
        s.send(bin_a)


if __name__ == '__main__':
    while(1):
        a = input()
        socket_send(a)