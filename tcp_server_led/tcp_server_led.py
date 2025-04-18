from pynq import Overlay
from pynq import MMIO
import socket
import threading

def program_fpga():
    global gpio_obj
    overlay = Overlay('/home/xilinx/workspace/gpio_led.bit')
    gpio_obj = MMIO(0x41200000, 0x10000)
    gpio_obj.write(0x0, 0x0)

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break  # If no data is received, close the connection

        # Process the command
        cmd = data.decode('utf-8').strip()
        if cmd == "1":
            gpio_obj.write(0x0, 0xf)
            response = "The LED has been turned on\n"
        elif cmd == "0":
            gpio_obj.write(0x0, 0x0)
            response = "The LED has been turned off\n"
        else:
            response = "Invalid command!\n"

        # Send response
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

def start_server(host='192.168.1.122', port=5000):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

print("Programming the FPGA...")
program_fpga()
print("FPGA programming done")

if __name__ == "__main__":
    start_server()
