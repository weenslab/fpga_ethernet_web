import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break  # If no data is received, close the connection

        # Echo the data back to the client
        client_socket.send(data)

    # Close the client socket
    client_socket.close()

def start_server(host='192.168.2.99', port=5000):
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

if __name__ == "__main__":
    start_server()
