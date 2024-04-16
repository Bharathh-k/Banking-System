import socket

SERVER_HOST = '' #add server's IPv4 addres here 
SERVER_PORT = '' #add server's Port Number here

def send_request(request):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(request.encode())

        response = client_socket.recv(1024).decode()

        return response

    finally:
        client_socket.close()

def main():
    while True:
        print("1. Check Balance")
        print("2. Credit")
        print("3. Debit")
        print("4. Fixed Deposit")
        print("5. Loan")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = input("Enter account name: ")
            response = send_request(f"balance {account}")
            print("Balance:", response)

        elif choice == '2':
            account = input("Enter account name: ")
            amount = input("Enter amount to credit: ")
            response = send_request(f"credit {account} {amount}")
            print(response)

        elif choice == '3':
            account = input("Enter account name: ")
            amount = input("Enter amount to debit: ")
            response = send_request(f"debit {account} {amount}")
            print(response)

        elif choice == '4':
            account = input("Enter account name: ")
            amount = input("Enter amount to deposit: ")
            response = send_request(f"fixed_deposit {account} {amount}")
            print(response)

        elif choice == '5':
            account = input("Enter account name: ")
            amount = input("Enter loan amount: ")
            response = send_request(f"loan {account} {amount}")
            print(response)

        elif choice == '6':
            send_request("quit")
            break

        else:
            print("Invalid choice")

main()
