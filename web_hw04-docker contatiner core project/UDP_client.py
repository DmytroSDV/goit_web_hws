import socket
import json

UDP_IP = '127.0.0.1'
UDP_PORT = 5000
MESSAGE = ""

def run_client(data_to_transfer: dict, ip=UDP_IP, port=UDP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    data_to_send = json.dumps(data_to_transfer).encode('utf-8')
    sock.sendto(data_to_send, server)
    print(f'Send data: {data_to_send} to server: {server}')
    sock.close()

if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)
