import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
server_address = ('localhost', 10000)

while True:
    message = input("Enter message: ")
    client.sendto(message.encode(), server_address)  # Send data to server

    if message.lower() == "end":
        print("Closing client...")
        break

    data, _ = client.recvfrom(1024)  # Receive response from server
    print("Server:", data.decode())

client.close()
