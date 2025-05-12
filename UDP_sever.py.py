import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
server_address = ('localhost', 10000)
server.bind(server_address)

print("UDP Server is listening on port 10000...")

while True:
    data, client_address = server.recvfrom(1024)  # Receive data from client
    message = data.decode()
    print(f"Received from {client_address}: {message}")

    if message.lower() == "end":
        print("Closing server...")
        break

    response = input("Enter response: ")
    server.sendto(response.encode(), client_address)  # Send response to client

server.close()
