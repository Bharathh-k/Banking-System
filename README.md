This project implements a simple banking system using Python's socket programming. It consists of a single server host capable of handling multiple clients concurrently. 
Clients can connect to the server to perform various banking operations such as account balance inquiry, deposit, withdrawal, and account creation.

Features

-Multi-client support: The server is designed to handle multiple client connections simultaneously, allowing multiple users to interact with the banking system concurrently.
-Secure communication: All communication between the clients and the server is encrypted to ensure data privacy and integrity.
-Account management: Users can create new accounts, inquire about their account balances, deposit funds, and withdraw funds.
-Error handling: The system incorporates robust error handling mechanisms to gracefully handle unexpected events and ensure reliability.
-Logging: Comprehensive logging functionality is implemented to keep track of system activities and facilitate troubleshooting.

Usage

-Start the server by running server.py.
-Connect to the server using client.py, add the server's IPv4 address in the code
