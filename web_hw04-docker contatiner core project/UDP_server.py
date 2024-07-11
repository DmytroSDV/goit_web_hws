import socket
import json
import datetime
import pathlib
import logging

UDP_IP = '127.0.0.1'
UDP_PORT = 5000
BASE_DIR = pathlib.Path()

def run_server_socket(ip=UDP_IP, port=UDP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    logging.info("Starting socket server")
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Received data: {data} from: {address}')  
            data = data.decode('utf-8')
            data_dict = json.loads(data)      
            json_update(data_dict)
            
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()

def json_update(data_dict: dict):
        
        data_path = BASE_DIR.joinpath('storage/data.json')
        temp_dict = {}
        current_time = datetime.datetime.now()
        current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        if data_path.is_file() and data_path.stat().st_size > 0:
            with open(data_path, 'r', encoding='utf-8') as existing_file:
                temp_dict = json.load(existing_file)
                
        temp_dict[current_time] = data_dict
        with open(data_path, 'w', encoding='utf-8') as fh:
            json.dump(temp_dict, fh, indent=4, ensure_ascii=False, default=str)

if __name__ == '__main__':
    run_server_socket(UDP_IP, UDP_PORT)
