# Name: Joshua Comfort
# File: server.py
# Date: 3/1/2023

from socket import * # Import everything from the socket package
import sys # Import the system package

if __name__ == "__main__":
    # Define constants to hold the hostname and port number
    HOSTNAME = "localhost"
    PORT_NUMBER = 8080 # This port number is not commonly used by traditional programs
    
    # Create a TCP server socket to listen for at most one connection
    server_socket = socket(AF_INET, SOCK_STREAM) # Create the socket
    server_socket.bind((HOSTNAME, PORT_NUMBER)) # Bind the socket with the localhost and port

    # Set the socket to listen for a single connection
    server_socket.listen(1)

    # After this line the server will be listening for a connection from a single client
    while True:
        print("Server is ready to serve...") # Print a prompt

        # Accept incoming connection from client
        connected_socket, address = server_socket.accept()
        
        # Get incoming message from the client
        try:
            message = connected_socket.recv(1024).decode() # Accept a 1024 byte (1KB) request from the client

            # We need to extract the file path from the second part of the HTTP header
            # The message variable holds the message requested
            filename = message.split()[1] # Get the filename from the incoming message
        
            file = open(filename[1:]) # Start reading from character 1 since it is a backslash

            file_content = file.read() # Read the file in and store its contents in  variable

            # Send an HTTP 200 response to the connected socket
            response = "HTTP/1.1 200 OK\r\n\r\n".encode()
            connected_socket.send(response)

            # Send the data
            for i in range(0, len(file_content)):
                connected_socket.send(file_content[i].encode())

            # Send the end of the message and close the socket
            connected_socket.send("\r\n".encode())
            connected_socket.close()
        except IOError:
            connected_socket.send("HTTP/1.1 404 Not Found\r\n\r\n")
            connected_socket.send("<!DOCTYPE html><html><title>Not Found</title><body><h1>Error 404. Page not found.</h1><p>The request resource was not found on the server.</p></body></html>".encode())
            connected_socket.close()

    server_socket.close() # Close the socket
    print("Script end...")
    sys.exit()
