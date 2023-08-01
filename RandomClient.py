
# import RandomCall
# import RandomQuoteGUI
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 2259  # The port used by the server

RandomSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RandomSocket.connect((HOST, PORT))
print(f"connected to:  {HOST}  Port:  {PORT}")


def get_quote():

    quote = b'quote'
    RandomSocket.sendall(quote)
    print('message sent:', quote.decode())
    data = RandomSocket.recv(1024).decode()
    print(f"Received {data!r}")
    return data


# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

