# Name: Joshua Comfort
# File: client.py
# Date: 3/11/2023

from socket import * # Import everything from the socket package
import sys # Import the system package

if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print("Invalid number of arguments, please specify an IP, port, and file to retrieve.")
        sys.exit()

    serverName = sys.argv[1] # Server name passed in as a command line argument
    serverPort = int(sys.argv[2]) # Server port passed in as a command line argument
    filePath = sys.argv[3] # File name to be requested from the server

    clientSocket = socket(AF_INET, SOCK_STREAM) # Create client socket
    clientSocket.connect((serverName, serverPort)) # Connect to the server

    file_get_message = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filePath, serverName) # HTTP GET message for the file the user requested
    
    # Send the encoded message
    clientSocket.send(file_get_message.encode())

    # Receive file from the server
    status = clientSocket.recv(2048)
    
    requested_file = ""
   
    # Get the first bytes
    current_byte = clientSocket.recv(2048)

    # Get all the data from the server and append into one string 
    while current_byte:
        requested_file += current_byte
        current_byte = clientSocket.recv(2048)

    # Decode and print the requested file
    print("File from the server: ")
    print(requested_file.decode())
    
    # Close the socket
    clientSocket.close() 
    
    # Exit script
    print("Script end...")
    sys.exit()
