import socket
import threading

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

accounts = {'account_holder1': {'balance': 1000, 'fixed_deposit': 0, 'maturity_amount':0}, 'account_holder2': {'balance': 1000, 'fixed_deposit': 0, 'maturity_amount':0}}


def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(1024).decode()
            command, *args = request.split()

            if command == 'balance':
                account = args[0]
                if account in accounts:
                    balance = accounts[account]['balance']
                    fixed_deposit = accounts[account]['fixed_deposit']

                    maturity_amount = accounts[account]['maturity_amount']

                    response = f"Balance: {balance}, Fixed Deposit: {fixed_deposit}, Maturity Amount: {maturity_amount}"

                    client_socket.send(response.encode())
                else:
                    client_socket.send(b'Account not found')

            elif command == 'credit':
                account, amount = args
                if account in accounts:
                    accounts[account]['balance'] += int(amount)
                    client_socket.send(b'Credit successful')
                else:
                    client_socket.send(b'Account not found')

            elif command == 'debit':
                account1, account, amount = args
                if account in accounts and accounts[account]['balance'] >= int(amount):
                    if account1 in accounts:
                        accounts[account1]['balance'] += int(amount)
                        accounts[account]['balance'] -= int(amount)
                        client_socket.send(b'Debit successful')
                        
                elif account in accounts and (accounts[account]['balance']+accounts[account]['fixed_deposit']) >= int(amount):
                    temp = int(amount) - accounts[account]['balance']
                    accounts[account]['balance'] = 0
                    accounts[account]['fixed_deposit'] -= temp
                    accounts[account1]['balance'] += int(amount)
                    
                    accounts[account]['maturity_amount'] = (accounts[account]['fixed_deposit'] + (0.06* accounts[account]['fixed_deposit'] *(int(duration)/12)))
                    
                    client_socket.send(b'Debit successful')
                    
                else:
                    client_socket.send(b'Insufficient funds or account not found')

            elif command == 'fixed_deposit':
                account, amount, duration = args
                if account in accounts and int(amount) and accounts[account]['balance']> int(amount) > 0:
                    accounts[account]['fixed_deposit'] += int(amount)
                    accounts[account]['balance'] -= int(amount)
                    
                    
                    accounts[account]['maturity_amount'] = accounts[account]['fixed_deposit']+(0.06*accounts[account]['fixed_deposit']*(int(duration)/12))
                    
                    client_socket.send(b'Fixed deposit successful')
                    
                else:
                    client_socket.send(b'Invalid amount or account not found')

            elif command == 'loan':
                account, amount = args
                if account in accounts and int(amount) > 0:
                    accounts[account]['balance'] += int(amount)
                    client_socket.send(b'Loan successfully credited to your account')
                else:
                    client_socket.send(b'Invalid amount or account not found')

            elif command == 'quit':
                client_socket.close()
                break

            else:
                client_socket.send(b'Invalid command')

        except Exception as e:
            print("Error:", e)
            client_socket.close()
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()